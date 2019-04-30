#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from cloudshell.snmp.quali_snmp import QualiMibTable


class HuaweiSNMPEntityTable(object):
    IF_ENTITY = "ifDescr"
    ENTITY_PHYSICAL = "entPhysicalName"
    ENTITY_VENDOR_TYPE_TO_CLASS_MAP = {"cevcontainer": "container", "cevchassis": "chassis", "cevmodule": "module",
                                       "cevport": "port", "cevpowersupply": "powerSupply"}

    def __init__(self, snmp_handler, logger, if_table):
        self._snmp = snmp_handler
        self._logger = logger
        self._if_table = if_table
        self._entity_table = None
        self._port_list = []
        self._chassis_list = []
        self._module_list = []
        self.relative_address = {}
        self.port_mapping = {}
        self.exclusion_list = []
        self._excluded_models = []
        self._filtered_chassis_list = []
        self._sorted_module_list = []
        self._power_supply_list = []
        self._filtered_power_supply_list = []
        self.port_exclude_pattern = r'stack|engine|management|mgmt|voice|foreign|' \
                                    r'cpu|control\s*ethernet\s*port|console\s*port'
        # self.module_exclude_pattern = r''
        self.entity_to_container_pattern = "hwvirtualentityoid"
        # self.ignore_entity_pattern = "cevModule$|cevModuleDaughterCard$"
        # self.ignore_entities_dict = dict()

    @property
    def chassis_list(self):
        if not self._filtered_chassis_list:
            if len(self._chassis_list) < 1:
                self._logger.error('Entity table error, no chassis found')
                raise Exception('Cannot load entPhysicalTable. Autoload cannot continue')

            for chassis in self._chassis_list:
                if chassis not in self.exclusion_list:
                    self._filtered_chassis_list.append(chassis)

        return self._filtered_chassis_list

    @property
    def port_list(self):
        return self._port_list

    @property
    def power_port_list(self):
        return self._power_supply_list

    @property
    def module_list(self):
        """Set list of all modules from entity mib table for provided list of ports

        :return:
        """
        if not self._sorted_module_list:
            self._get_sorted_modules_with_ports()
        return self._sorted_module_list

    def _get_sorted_modules_with_ports(self):
        for port in self._port_list:
            modules = list(self._get_module_parents(port))[::-1]
            if modules and modules[0] not in self._module_list:
                self._analyze_module(modules[0])
            if len(modules) > 1 and modules[-1] not in self._module_list:
                self._analyze_module(modules[-1])
        module_relative_paths = sorted(self.relative_address, key=self.relative_address.get)
        self._sorted_module_list = [module for module in module_relative_paths if
                                    module in self._module_list and module not in self.exclusion_list]

    def _analyze_module(self, module):
        if module not in self.exclusion_list:
            module_parent_address = self.get_relative_address(module)
            if not module_parent_address:
                self._excluded_models.append(module)
                return
            module_parent_address_list = module_parent_address.split("/")
            if len(module_parent_address_list) > 2:
                module_parent_address = '{0}/{1}'.format(module_parent_address[0], module_parent_address[1])

            module_rel_path = module_parent_address + '/' + self.get_resource_id(module)
            i = 1
            while module_rel_path in self.relative_address.values():
                i += 1
                module_rel_path = '{0}/{1}'.format(module_parent_address, (int(self.get_resource_id(module)) + i))
            self.relative_address[module] = module_rel_path
            self._module_list.append(module)
            self._logger.debug("Added {0} with relative path {1}".format(self._entity_table[module]["entPhysicalDescr"],
                                                                         module_rel_path))
        else:
            self._excluded_models.append(module)

    def get_entity_table(self):
        self._entity_table = self._get_entity_table()
        # self._filter_lower_bay_containers()
        self._get_sorted_modules_with_ports()
        self._populate_relative_addresses()
        self._filter_power_port_list()
        return self._entity_table

    def _get_entity_table(self):
        """Read Entity-MIB and filter out device's structure and all it's elements, like ports, modules, chassis, etc.

        :rtype: QualiMibTable
        :return: structured and filtered EntityPhysical table.
        """

        result_dict = QualiMibTable('entPhysicalTable')

        # entity_table_critical_port_attr = {'entPhysicalContainedIn': 'str', 'entPhysicalClass': 'str',
        #                                    'entPhysicalVendorType': 'str'}
        entity_table_optional_port_attr = {'entPhysicalDescr': 'str', 'entPhysicalName': 'str'}

        physical_indexes = self._snmp.get_table('ENTITY-MIB', 'entPhysicalParentRelPos')
        vendor_type_match_pattern = r"|".join(self.ENTITY_VENDOR_TYPE_TO_CLASS_MAP.keys())
        for index in physical_indexes.keys():

            if physical_indexes[index]['entPhysicalParentRelPos'] == '':
                self.exclusion_list.append(index)
                continue
            temp_entity_table = physical_indexes[index].copy()

            temp_entity_table.update(self._snmp.get_properties('ENTITY-MIB', index, {"entPhysicalClass": "str"})
                                     [index])
            if re.search(r"cpu|fan|sensor", temp_entity_table['entPhysicalClass'].lower()):
                self._logger.debug("Loaded {}, skipping.".format(temp_entity_table['entPhysicalClass']))
                continue

            temp_entity_table.update(self._snmp.get_properties('ENTITY-MIB', index, {"entPhysicalContainedIn": "str"})
                                     [index])
            if temp_entity_table['entPhysicalContainedIn'] == '':
                self.exclusion_list.append(index)
                continue

            temp_entity_table.update(self._snmp.get_properties('ENTITY-MIB', index, {"entPhysicalVendorType": "str"})
                                     [index])
            ent_physical_class = temp_entity_table.get("entPhysicalClass")
            if not ent_physical_class or ent_physical_class == "''" or "other" in ent_physical_class:
                vendor_type = temp_entity_table['entPhysicalVendorType']
                if not vendor_type:
                    continue
                vendor_type_match = re.search(vendor_type_match_pattern, vendor_type.lower())
                index_entity_class = None
                if vendor_type_match:
                    index_entity_class = self.ENTITY_VENDOR_TYPE_TO_CLASS_MAP[vendor_type_match.group()]
                if index_entity_class:
                    temp_entity_table['entPhysicalClass'] = index_entity_class
                elif not ent_physical_class or ent_physical_class == "''":
                    self.exclusion_list.append(index)
                    continue
            if "module" in temp_entity_table['entPhysicalClass'].lower() \
                    and re.search(self.entity_to_container_pattern, temp_entity_table['entPhysicalVendorType'].lower(),
                                  re.IGNORECASE):
                temp_entity_table['entPhysicalClass'] = 'container'
            else:
                temp_entity_table['entPhysicalClass'] = temp_entity_table['entPhysicalClass'].replace("'", "")

            temp_entity_table.update(self._snmp.get_properties('ENTITY-MIB', index, entity_table_optional_port_attr)
                                     [index])

            if re.search(r'stack|chassis|module|port|powerSupply|container|backplane',
                         temp_entity_table['entPhysicalClass']):
                result_dict[index] = temp_entity_table
                self._logger.debug("Successfully loaded '{0}'".format(temp_entity_table["entPhysicalDescr"]))
            else:
                continue

            if temp_entity_table['entPhysicalClass'] == 'chassis':
                self._chassis_list.append(index)
                chassis_id = temp_entity_table['entPhysicalParentRelPos']
                if chassis_id == '-1':
                    chassis_id = '0'
                self.relative_address[index] = chassis_id
            elif temp_entity_table['entPhysicalClass'] == 'port':
                if not re.search(self.port_exclude_pattern, temp_entity_table['entPhysicalName'], re.IGNORECASE) \
                        and not re.search(self.port_exclude_pattern, temp_entity_table['entPhysicalDescr'],
                                          re.IGNORECASE):
                    port_entity = self._get_mapping(index, temp_entity_table[self.ENTITY_PHYSICAL])
                    if not port_entity:
                        port_entity = self._get_mapping(index, temp_entity_table["entPhysicalName"])
                    if port_entity and port_entity not in self.port_mapping.values():
                        self.port_mapping[index] = port_entity
                        self._port_list.append(index)
            elif temp_entity_table['entPhysicalClass'] == 'powerSupply':
                self._power_supply_list.append(index)

        self._filter_entity_table(result_dict)
        return result_dict

    # def _filter_lower_bay_containers(self):
    #     """
    #     Filter rare cases when device have multiple bays with separate containers in each bay
    #
    #     """
    #     upper_container = None
    #     lower_container = None
    #     containers = self._entity_table.filter_by_column('Class', "container").sort_by_column('ParentRelPos').keys()
    #     for container in containers:
    #         vendor_type = self._entity_table[container].get("entPhysicalVendorType", "")
    #         if 'uppermodulebay' in vendor_type.lower():
    #             upper_container = container
    #         if 'lowermodulebay' in vendor_type.lower():
    #             lower_container = container
    #     if lower_container and upper_container:
    #         child_upper_items_len = len(self._entity_table.filter_by_column('ContainedIn', str(upper_container)
    #                                                                         ).sort_by_column('ParentRelPos').keys())
    #         child_lower_items = self._entity_table.filter_by_column('ContainedIn', str(lower_container)
    #                                                                 ).sort_by_column('ParentRelPos').keys()
    #         for child in child_lower_items:
    #             self._entity_table[child]['entPhysicalContainedIn'] = upper_container
    #             self._entity_table[child]['entPhysicalParentRelPos'] = str(child_upper_items_len + int(
    #                 self._entity_table[child]['entPhysicalParentRelPos']))

    def get_resource_id(self, item_id):
        parent_id = int(self._entity_table[item_id]['entPhysicalContainedIn'])
        if parent_id > 0 and parent_id in self._entity_table:
            if re.search(r'container|backplane', self._entity_table[parent_id]['entPhysicalClass']):
                result = self._entity_table[parent_id]['entPhysicalParentRelPos']
            elif parent_id in self._excluded_models:
                result = self.get_resource_id(parent_id)
            else:
                result = self._entity_table[item_id]['entPhysicalParentRelPos']
        else:
            result = self._entity_table[item_id]['entPhysicalParentRelPos']
        return result

    def get_relative_address(self, item_id):
        """Build relative path for received item

        :param item_id:
        :return:
        """

        result = ''
        if int(item_id) not in self._filtered_chassis_list:
            parent_id = int(self._entity_table[item_id]['entPhysicalContainedIn'])
            if parent_id in self.exclusion_list:
                return result
            if parent_id not in self.relative_address:
                if parent_id in self._sorted_module_list:
                    result = self.get_resource_id(parent_id)
                if result != '':
                    result = "{}/{}".format(self.get_relative_address(parent_id), result)
                else:
                    result = self.get_relative_address(parent_id)
            else:
                result = self.relative_address[parent_id]
        else:
            result = self.relative_address[item_id]

        return result

    def _filter_entity_table(self, raw_entity_table):
        """Filters out all elements if their parents, doesn't exist, or listed in self.exclusion_list

        :param raw_entity_table: entity table with unfiltered elements
        """

        elements = raw_entity_table.sort_by_column('ParentRelPos').keys()
        for element in reversed(elements):
            parent_id = int(raw_entity_table[element]['entPhysicalContainedIn'])
            element_class = raw_entity_table.get(element, dict()).get("entPhysicalClass")
            if (parent_id not in raw_entity_table and element_class not in ["chassis",
                                                                            "stack"]) or parent_id in self.exclusion_list:
                self.exclusion_list.append(element)
        return raw_entity_table

    def _populate_relative_addresses(self):
        """Build dictionary of relative paths for each module and port

        :return:
        """

        port_list = list(self._port_list)
        for port in port_list:
            if port not in self.exclusion_list:
                self.relative_address[port] = self.get_relative_address(port) + '/' + self.get_resource_id(port)
            else:
                self._port_list.remove(port)

    def _get_module_parents(self, module_id):
        """
        Retrieve all parent modules for a specific module

        :param module_id:
        :return list: parent modules
        """

        result = []
        parent_id = int(self._entity_table[module_id]['entPhysicalContainedIn'])
        if parent_id > 0 and parent_id in self._entity_table:
            parent_physical_class = self._entity_table.get(parent_id, {}).get("entPhysicalClass", "")
            if parent_physical_class == "module":
                result.append(parent_id)
                result.extend(self._get_module_parents(parent_id))
            elif parent_physical_class == "chassis":
                return result
            else:
                result.extend(self._get_module_parents(parent_id))
        return result

    def _get_mapping(self, port_index, port_descr):
        """Get mapping from entPhysicalTable to ifTable.
        Build mapping based on ent_alias_mapping_table if exists else build manually based on
        entPhysicalDescr <-> ifDescr mapping.

        :return: simple mapping from entPhysicalTable index to ifTable index:
        |        {entPhysicalTable index: ifTable index, ...}
        """

        port_exclude_list = self.port_exclude_pattern.replace("|", "|.*")
        port_if_entity = None
        ent_alias_mapping_identifier = None
        index_template = "{}.{}"
        try:
            index = index_template.format(port_index, 0)
            ent_alias_mapping_identifier = int(self._snmp.get_property('ENTITY-MIB',
                                                                       'entAliasMappingIdentifier',
                                                                       index).split('.')[-1])
        except ValueError:
            try:
                index = index_template.format(port_index, 1)
                ent_alias_mapping_identifier = int(self._snmp.get_property('ENTITY-MIB',
                                                                           'entAliasMappingIdentifier',
                                                                           index).split('.')[-1])
            except ValueError:
                self._logger.debug("Failed to get entAliasMappingIdentifier")
        if ent_alias_mapping_identifier:
            port_id = ent_alias_mapping_identifier
            port_if_entity = self._if_table.get_if_entity_by_index(int(port_id))

        if not port_if_entity:
            port_if_entity = self._if_table.get_if_index_from_port_name(port_descr, port_exclude_list)
        return port_if_entity

    def _filter_power_port_list(self):
        """Get power supply relative path

        :return: string relative path
        """

        power_supply_list = list(self._power_supply_list)
        for power_port in power_supply_list:
            parent_index = int(self._entity_table[power_port]['entPhysicalContainedIn'])
            if 'powerSupply' in self._entity_table[parent_index]['entPhysicalClass']:
                if parent_index in self._power_supply_list:
                    self._power_supply_list.remove(power_port)
