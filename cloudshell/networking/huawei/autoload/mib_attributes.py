from cloudshell.snmp.quali_snmp import QualiMibTable
from cloudshell.networking.huawei.vrp.structures.autoload_structure import HuaweiRootDevice, \
    GenericPortChannel,GenericPort,GenericPowerPort,GenericModule,GenericChassis

import os,re


class MibAttributes():

#
    def __init__(self, snmp_handler, logger, supported_os,resource_name):
        self.snmp = snmp_handler
        self.logger = logger
        self.module_list = []
        self.chassis_list = []
        self.exclusion_list = []
        self.port_list = []
        self.power_supply_list = []
        self.port_mapping = {}
        self.port_list = []
        self.relative_path = {}
        self.root_model = HuaweiRootDevice()

        self.entity_mib_table_black_list = ['alarm', 'fan', 'sensor']
        self.port_exclude_pattern = 'serial|stack|engine|management|MEth'
        self.module_exclude_pattern = 'cevsfp'
        self.physicaldescriptionexcludepattern = 'Flexible Line Processing Unit'
        self.resources = list()
        self.attributes = list()

        self.vendor = 'huawei'

        self.resource_name = resource_name
        self.root_model.set_system_name(self.snmp.get_property('SNMPv2-MIB', 'sysName', 0))
        self.root_model.set_system_desc(self.snmp.get(('SNMPv2-MIB', 'sysDescr'))['sysDescr'])
        self.snmp_object_id = self.snmp.get_property('SNMPv2-MIB', 'sysObjectID', 0)
        self.if_descr = self.snmp.get_table('IF-MIB', 'ifDescr') #ifDescr
        self.sys_descr = self.snmp.get(('SNMPv2-MIB', 'sysDescr'))['sysDescr']
        self.lldp_loc_port_desc,self.lldp_rem_table,self.dot3_stats_index,self.ip_v4_table,self.ip_v6_entry ,\
        self.port_channel_ports ,self.sys_location ,self.sys_contact ,self.physical_parent_rel_pos = ['']*9



    def load_huawei_mib(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
        self.snmp.update_mib_sources(path)




    def _load_snmp_objects_and_tables(self):
        """ Load all huawei  interface entries objects from MIB tables

        :return: ''
        """



        self.logger.info('Start loading MIB objects: ')



        self.lldp_loc_port_desc = self.snmp.get_table('LLDP-MIB', 'lldpLocPortTable')
        self.lldp_rem_table = self.snmp.get_table('LLDP-MIB', 'lldpRemTable')
        self.dot3_stats_index = self.snmp.get_table('EtherLike-MIB', 'dot3StatsIndex')
        self.ip_v4_table = self.snmp.get_table('RFC1213-MIB','ipAddrTable')
        self.ip_v6_entry = self.snmp.get_table('IPV6-MIB', 'ipv6AddrTable')
        self.port_channel_ports = self.snmp.get_table('IEEE8023-LAG-MIB', 'dot3adAggPortAttachedAggID')

        self.sys_location = self.snmp.get_property('SNMPv2-MIB', 'sysLocation', 0)
        self.sys_contact = self.snmp.get_property('SNMPv2-MIB', 'sysContact', 0)
        self.physical_parent_rel_pos = self.snmp.get_table('ENTITY-MIB', 'entPhysicalParentRelPos')

        self.logger.info('IfDescr object loaded')
        self.entity_mib_table = self._get_entity_table()
        if len(self.entity_mib_table.keys()) < 1:
            raise Exception('Cannot load entPhysicalTable. Autoload cannot continue')
        self.logger.info('Entity table loaded')

        self.logger.info('MIB Tables loaded successfully')

    def get_physical_model_name(self,key):
        return self.snmp.get_property('ENTITY-MIB', 'entPhysicalModelName', key)

    def get_physical_serial_name(self,key):
        return self.snmp.get_property('ENTITY-MIB', 'entPhysicalSerialNum', key)

    def get_interface_duplex(self,key):

       res =  self.snmp.get_property('HUAWEI-PORT-MIB', 'hwEthernetDuplex', key)
       return res

    def get_physical_software_rev(self,key):
        return self.snmp.get_property('ENTITY-MIB', 'entPhysicalSoftwareRev', key)

    def get_module_list(self):
        """Set list of all modules from entity mib table for provided list of ports

        :return:
        """

        for port in self.port_list:
            modules = []
            modules.extend(self._get_module_parents(port))
            for module in modules:
                entPhysicalDescr = self.entity_mib_table[module]['entPhysicalDescr']
                if re.search(self.physicaldescriptionexcludepattern, entPhysicalDescr):
                    self._excluded_models.append(module)
                if module in self.module_list:
                    continue

                vendor_type = self.snmp.get_property('ENTITY-MIB', 'entPhysicalVendorType', module)
                if not re.search(self.module_exclude_pattern, vendor_type.lower()):
                    if module not in self.exclusion_list and module not in self.module_list:
                        self.module_list.append(module)
                else:
                    self._excluded_models.append(module)


    def _get_module_parents(self, module_id):
        result = []
        parent_id = int(self.entity_mib_table[module_id]['entPhysicalContainedIn'])
        if parent_id > 0 and parent_id in self.entity_mib_table:
            if re.search('module', self.entity_mib_table[parent_id]['entPhysicalClass']):
                result.append(parent_id)
                result.extend(self._get_module_parents(parent_id))
            elif re.search('chassis', self.entity_mib_table[parent_id]['entPhysicalClass']):
                return result
            else:
                result.extend(self._get_module_parents(parent_id))
        return result

    def _get_resource_id(self, item_id):

        parent_id = int(self.entity_mib_table[item_id]['entPhysicalContainedIn'])
        if parent_id > 0 and parent_id in self.entity_mib_table:
            if re.search('container|backplane', self.entity_mib_table[parent_id]['entPhysicalClass']):
                    result = self.entity_mib_table[parent_id]['entPhysicalParentRelPos']
            elif parent_id in self._excluded_models:
                result = self._get_resource_id(parent_id)
            else:
                result = self.entity_mib_table[item_id]['entPhysicalParentRelPos']
        else:
            result = self.entity_mib_table[item_id]['entPhysicalParentRelPos']
        return result

    def _get_port_channels(self):
        """Get all port channels and set attributes for them

        :return:
        """

        if not self.if_descr:
            return
        port_channel_dic = {index: port for index, port in self.if_descr.iteritems() if
                            'channel' in port['ifDescr'] and '.' not in port['ifDescr']}
        self.logger.info('Start loading Port Channels')
        for key, value in port_channel_dic.iteritems():
            interface_model = value['ifDescr']
            match_object = re.search('\d+$', interface_model)
            if match_object:
                interface_id = 'PC{0}'.format(match_object.group(0))
            else:
                self.logger.error('Adding of {0} failed. Name is invalid'.format(interface_model))
                continue
            attribute_map = {'description': self.snmp.get_property('IF-MIB', 'ifAlias', key),
                             'associated_ports': self._get_associated_ports(key)}
            attribute_map.update(self._get_ip_interface_details(key))
            port_channel = GenericPortChannel(name=interface_model, relative_address=interface_id, **attribute_map)


            self._add_resource(port_channel)

            self.logger.info('Added ' + interface_model + ' Port Channel')
        self.logger.info('Finished Loading Port Channels')

    def _get_associated_ports(self, item_id):
        """Get all ports associated with provided port channel
        :param item_id:
        :return:
        """

        result = ''
        for key, value in self.port_channel_ports.iteritems():
            if str(item_id) in value['dot3adAggPortAttachedAggID']:
                result += self.if_table[key]['ifDescr'].replace('/', '-').replace(' ', '') + '; '
        return result.strip(' \t\n\r')

    def _get_ip_interface_details(self, port_index):
        """Get IP address details for provided port

        :param port_index: port index in ifTable
        :return interface_details: detected info for provided interface dict{'IPv4 Address': '', 'IPv6 Address': ''}
        """

        interface_details = {'ipv4_address': '', 'ipv6_address': ''}
        if self.ip_v4_table and len(self.ip_v4_table) > 1:
            for key, value in self.ip_v4_table.iteritems():
                if 'ipAdEntIfIndex' in value and int(value['ipAdEntIfIndex']) == port_index:
                    interface_details['IPv4 Address'] = key
                break
        if self.ip_v6_entry and len(self.ip_v6_entry) > 1:
            for key, value in self.ip_v6_entry.iteritems():
                if 'ipAdEntIfIndex' in value and int(value['ipAdEntIfIndex']) == port_index:
                    interface_details['IPv6 Address'] = key
                break
        return interface_details

    def _get_interface_details(self, port_index):
        """Get interface attributes

        :param port_index: port index in ifTable
        :return interface_details: detected info for provided interface dict{'Auto Negotiation': '', 'Duplex': ''}
        """

        interface_details = {'duplex': 'Full', 'auto_negotiation': 'False'}
        try:
            auto_negotiation = self.snmp.get(('MAU-MIB', 'ifMauAutoNegAdminStatus', port_index, 1)).values()[0]
            if 'enabled' in auto_negotiation.lower():
                interface_details['auto_negotiation'] = 'True'
        except Exception as e:
            self.logger.error('Failed to load auto negotiation property for interface {0}'.format(e.message))
        for key, value in self.dot3_stats_index.iteritems():
            if 'dot3StatsIndex' in value.keys() and value['dot3StatsIndex'] == str(port_index):
                interface_duplex = self.get_interface_duplex(key)
                if 'halfDuplex' in interface_duplex:
                    interface_details['duplex'] = 'Half'
        return interface_details


    def get_relative_path(self, item_id):
        """Build relative path for received item

        :param item_id:
        :return:
        """

        result = ''

        if item_id not in self.chassis_list:
            parent_id = int(self.entity_mib_table[item_id]['entPhysicalContainedIn'])
            if parent_id  in self._excluded_models:
                parent_id = int(self.entity_mib_table[parent_id]['entPhysicalContainedIn'])
            if parent_id not in self.relative_path.keys():
                if parent_id in self.module_list:
                    result = self._get_resource_id(parent_id)
                if result != '':
                    result = self.get_relative_path(parent_id) + '/' + result
                else:
                    result = self.get_relative_path(parent_id)
            else:
                result = self.relative_path[parent_id]
        else:
            result = self.relative_path[item_id]

        return result



    def _get_entity_table(self):
        """Read Entity-MIB and filter out device's structure and all it's elements, like ports, modules, chassis, etc.

        :rtype: QualiMibTable
        :return: structured and filtered EntityPhysical table.
        """

        result_dict = QualiMibTable('entPhysicalTable')

        entity_table_critical_port_attr = {'entPhysicalContainedIn': 'str', 'entPhysicalClass': 'str',
                                           'entPhysicalVendorType': 'str'}
        entity_table_optional_port_attr = {'entPhysicalDescr': 'str', 'entPhysicalName': 'str'}

        physical_indexes = self.physical_parent_rel_pos
        for index in physical_indexes.keys():
            is_excluded = False
            if physical_indexes[index]['entPhysicalParentRelPos'] == '':
                self.exclusion_list.append(index)
                continue
            temp_entity_table = physical_indexes[index].copy()
            temp_entity_table.update(self.snmp.get_properties('ENTITY-MIB', index, entity_table_critical_port_attr)
                                     [index])
            if temp_entity_table['entPhysicalContainedIn'] == '':
                is_excluded = True
                self.exclusion_list.append(index)

            for item in self.entity_mib_table_black_list:
                if item in temp_entity_table['entPhysicalVendorType'].lower():
                    is_excluded = True
                    break

            if is_excluded is True:
                continue

            temp_entity_table.update(self.snmp.get_properties('ENTITY-MIB', index, entity_table_optional_port_attr)
                                     [index])

            if temp_entity_table['entPhysicalClass'] == '':
                vendor_type = self.snmp.get_property('ENTITY-MIB', 'entPhysicalVendorType', index)
                index_entity_class = None
                if vendor_type == '':
                    continue
                if 'cevcontainer' in vendor_type.lower():
                    index_entity_class = 'container'
                elif 'cevchassis' in vendor_type.lower():
                    index_entity_class = 'chassis'
                elif 'cevmodule' in vendor_type.lower():
                    index_entity_class = 'module'
                elif 'cevport' in vendor_type.lower():
                    index_entity_class = 'port'
                elif 'cevpowersupply' in vendor_type.lower():
                    index_entity_class = 'powerSupply'
                if index_entity_class:
                    temp_entity_table['entPhysicalClass'] = index_entity_class
            else:
                temp_entity_table['entPhysicalClass'] = temp_entity_table['entPhysicalClass'].replace("'", "")

            if re.search('stack|chassis|module|port|powerSupply|container|backplane',
                         temp_entity_table['entPhysicalClass']):
                result_dict[index] = temp_entity_table

            if temp_entity_table['entPhysicalClass'] == 'chassis':
                self.chassis_list.append(index)
            elif temp_entity_table['entPhysicalClass'] == 'port':
                if not re.search(self.port_exclude_pattern, temp_entity_table['entPhysicalName']) \
                        and not re.search(self.port_exclude_pattern, temp_entity_table['entPhysicalDescr']):
                    port_id = self._get_mapping(index, temp_entity_table['entPhysicalDescr'])
                    if port_id and port_id in self.if_descr and port_id not in self.port_mapping.values():
                        self.port_mapping[index] = port_id
                        self.port_list.append(index)
            elif temp_entity_table['entPhysicalClass'] == 'powerSupply':
                self.power_supply_list.append(index)

        self._filter_entity_table(result_dict)
        return result_dict


    def _get_ports_attributes(self):
        """Get resource details and attributes for every port in self.port_list

        :return:
        """

        self.logger.info('Start loading Ports')
        for port in self.port_list:
            if_table_port_attr = {'ifType': 'str', 'ifPhysAddress': 'str', 'ifMtu': 'int', 'ifSpeed': 'int'}
            if_table = self.if_descr[self.port_mapping[port]].copy()
            if_table.update(self.snmp.get_properties('IF-MIB', self.port_mapping[port], if_table_port_attr))
            interface_name = self.if_descr[self.port_mapping[port]]['ifDescr']
            if interface_name == '':
                interface_name = self.entity_mib_table[port]['entPhysicalName']
            if interface_name == '':
                continue
            interface_type = if_table[self.port_mapping[port]]['ifType'].replace('/', '').replace("'", '')


            attribute_map = {'l2_protocol_type': interface_type,
                             'mac_address': if_table[self.port_mapping[port]]['ifPhysAddress'],
                             'mtu': if_table[self.port_mapping[port]]['ifMtu'],
                             'bandwidth': int(if_table[self.port_mapping[port]]['ifSpeed'])/1000000,
                             'port_description': self.snmp.get_property('IF-MIB', 'ifAlias', self.port_mapping[port]),
                             'adjacent': self._get_adjacent(self.port_mapping[port])}
            attribute_map.update(self._get_interface_details(self.port_mapping[port]))
            attribute_map.update(self._get_ip_interface_details(self.port_mapping[port]))

            unique_id = '{}.{}.{}'.format(self.resource_name, 'port', port)

            port_object = GenericPort(name=interface_name.replace('/', '-'), relative_address=self.relative_path[port],unique_id=unique_id, **attribute_map)


            self._add_resource(port_object)
            self.logger.info('Added ' + interface_name + ' Port')
        self.logger.info('Finished Loading Ports')

    def get_ent_alias_mapping_identifier(self,port_index):
        res = self.snmp.get(('ENTITY-MIB', 'entAliasMappingIdentifier', port_index, 1))
        return  res


    def _get_power_ports(self):
        """Get attributes for power ports provided in self.power_supply_list

        :return:
        """

        self.logger.info('Start loading Power Ports')
        for port in self.power_supply_list:
            port_id = self.entity_mib_table[port]['entPhysicalParentRelPos']
            parent_index = int(self.entity_mib_table[port]['entPhysicalContainedIn'])
            if re.search('powerSupply', self.entity_mib_table[port]['entPhysicalClass']):
                if re.search('container|backplane', self.entity_mib_table[parent_index]['entPhysicalClass']):
                    port_id = self.entity_mib_table[parent_index]['entPhysicalParentRelPos']
                    parent_index = int(self.entity_mib_table[parent_index]['entPhysicalContainedIn'])

            parent_id = int(self.entity_mib_table[parent_index]['entPhysicalParentRelPos'])
            chassis_id = self.get_relative_path(parent_index)
            relative_path = '{0}/PP{1}-{2}'.format(chassis_id, parent_id, port_id)
            port_name = 'PP{0}'.format(self.power_supply_list.index(port))
            port_details = {'model': self.get_physical_model_name(port),
                            'port_description': self.snmp.get_property('ENTITY-MIB', 'entPhysicalDescr', port, 'str'),
                            'version': self.snmp.get_property('ENTITY-MIB', 'entPhysicalHardwareRev', port),
                            'serial_number': self.get_physical_serial_name(port)
                            }
            unique_id = '{}.{}.{}'.format(self.resource_name, 'power_port', port)

            power_port_object = GenericPowerPort(name=port_name, relative_address=relative_path,unique_id=unique_id, **port_details)
            self._add_resource(power_port_object)

            self.logger.info('Added ' + self.entity_mib_table[port]['entPhysicalName'].strip(' \t\n\r') + ' Power Port')
        self.logger.info('Finished Loading Power Ports')


    def add_relative_paths(self):
        """Builds dictionary of relative paths for each module and port

        :return:
        """

        port_list = list(self.port_list)
        module_list = list(self.module_list)
        for module in module_list:


            if module not in self.exclusion_list and module not in self._excluded_models:
                self.relative_path[module] = self.get_relative_path(module) + '/' + self._get_resource_id(module)
            else:
                self.module_list.remove(module)
        for port in port_list:
            if port not in self.exclusion_list:
                self.relative_path[port] = self.get_relative_path(port) + '/' + self._get_resource_id(port)
            else:
                self.port_list.remove(port)

    def _get_chassis_attributes(self, chassis_list):
        """
        Get Chassis element attributes
        :param chassis_list: list of chassis to load attributes for
        :return:
        """

        self.logger.info('Start loading Chassis')
        for chassis in chassis_list:
            chassis_id = self.relative_path[chassis]
            chassis_details_map = {
                'model': self.get_physical_model_name(chassis),
                'serial_number': self.get_physical_serial_name(chassis)
            }
            if chassis_details_map['model'] == '':
                chassis_details_map['model'] = self.entity_mib_table[chassis]['entPhysicalDescr']
            relative_address = '{0}'.format(chassis_id)
            name = 'Chassis {}'.format(chassis_id)
            unique_id = '{}.{}.{}'.format(self.resource_name, 'chassis', chassis)
            chassis_object = GenericChassis(name=name,
                                          relative_address=relative_address,
                                          unique_id=unique_id,
                                          **chassis_details_map)

            self._add_resource(chassis_object)
            self.logger.info('Added ' + self.entity_mib_table[chassis]['entPhysicalDescr'] + ' Chass')
        self.logger.info('Finished Loading Modules')


    def _get_module_attributes(self):
        """Set attributes for all discovered modules

        :return:
        """

        self.logger.info('Start loading Modules')
        for module in self.module_list:
            module_id = self.relative_path[module]
            module_index = self._get_resource_id(module)
            module_details_map = {
                'model': self.entity_mib_table[module]['entPhysicalDescr'],
                'version': self.get_physical_software_rev(module),
                'serial_number': self.get_physical_serial_name(module)
            }

            if '/' in module_id and len(module_id.split('/')) < 3:
                module_name = 'Module {0}'.format(module_index)
                model = 'Generic Module'
                unique_id = '{}.{}.{}'.format(self.resource_name, 'module', module)
            else:
                module_name = 'Sub Module {0}'.format(module_index)
                model = 'Generic Sub Module'
                unique_id = '{}.{}.{}'.format(self.resource_name, 'sub-module', module)


            module_object = GenericModule(name=module_name,resource_model = model, unique_id=unique_id,relative_address=module_id, **module_details_map)



            self._add_resource(module_object)

            self.logger.info('Added ' + self.entity_mib_table[module]['entPhysicalDescr'] + ' Module')
        self.logger.info('Finished Loading Modules')

    def _get_mapping(self, port_index, port_descr):
        """ Get mapping from entPhysicalTable to ifTable.
        Build mapping based on ent_alias_mapping_table if exists else build manually based on
        entPhysicalDescr <-> ifDescr mapping.

        :return: simple mapping from entPhysicalTable index to ifTable index:
        |        {entPhysicalTable index: ifTable index, ...}
        """

        port_id = None
        try:
            ent_alias_mapping_identifier = self.get_ent_alias_mapping_identifier(port_index)
            port_id = int(ent_alias_mapping_identifier['entAliasMappingIdentifier'].split('.')[-1])
        except Exception as e:
            self.logger.error(e.message)
            module_index, port_index = re.findall('\d+', port_descr)
            if_table_re = '^.*' + module_index + '/' + port_index + '$'
            for interface in self.if_table.values():
                if re.search(if_table_re, interface['ifDescr']):
                    port_id = int(interface['suffix'])
                    break
        return port_id


    def _get_adjacent(self, interface_id):
        """Get connected device interface and device name to the specified port id, using lldp protocols (or cdp)

        :param interface_id: port id
        :return: device's name and port connected to port id
        :rtype string
        """

        result = ''
        if self.lldp_rem_table:
            for key, value in self.lldp_loc_port_desc.iteritems():
                interface_name = self.if_descr[interface_id]['ifDescr']
                if interface_name == '':
                    break
                if 'lldpLocPortDesc' in value and interface_name in value['lldpLocPortDesc']:
                    if 'lldpRemSysName' in self.lldp_rem_table and 'lldpRemPortDesc' in self.lldp_rem_table:
                        result = '{0} through {1}'.format(self.lldp_rem_table[key]['lldpRemSysName'],
                                                          self.lldp_rem_table[key]['lldpRemPortDesc'])
        return result