from cloudshell.snmp.quali_snmp import QualiMibTable
from cloudshell.networking.autoload.networking_autoload_resource_structure import Port, PortChannel, PowerPort, \
    Chassis, Module
from cloudshell.networking.operations.interfaces.autoload_operations_interface import AutoloadOperationsInterface
import inject
import os,re

class MibAttributes(AutoloadOperationsInterface):


    def __init__(self, snmp_handler=None, logger=None, supported_os=None):
        self._snmp = snmp_handler
        self.module_list = []
        self.chassis_list = []
        self.exclusion_list = []
        self.port_list = []
        self.vendor = 'Huawei'



    @property
    def snmp(self):
        if self._snmp is None:
            try:
                self._snmp = inject.instance('snmp_handler')
            except:
                raise Exception('HuaweiAutoload', 'Snmp handler is none or empty')
        return self._snmp


    def load_huawei_mib(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
        self.snmp.update_mib_sources(path)




    def _load_snmp_objects_and_tables(self):
        """ Load all Huawei  interface entries objects from MIB tables

        :return: ''
        """
        self.sys_name = self.snmp.get_property('SNMPv2-MIB', 'sysName', 0)
        self.snmp_object_id = self.snmp.get_property('SNMPv2-MIB', 'sysObjectID', 0)
        self.sys_descr = self.snmp.get(('SNMPv2-MIB', 'sysDescr'))['sysDescr']
        self.logger.info('Start loading MIB objects: ')
        self.if_descr = self.snmp.get_table('IF-MIB', 'ifDescr')
        self.logger.info('IfDescr object loaded')
        self.entity_mib_table = self._get_entity_table()
        if len(self.entity_mib_table.keys()) < 1:
            raise Exception('Cannot load entPhysicalTable. Autoload cannot continue')
        self.logger.info('Entity table loaded')

        self.lldp_loc_port_desc = self.snmp.get_table('LLDP-MIB', 'lldpLocPortDesc')
        self.lldp_rem_table = self.snmp.get_table('LLDP-MIB', 'lldpRemTable')
        self.dot3_stats_index = self.snmp.get_table('EtherLike-MIB', 'dot3StatsIndex')
        self.ip_v4_table = self.snmp.get_table('IP-MIB','ipAddrTable') #  'ipAddressAddr'
        self.ip_v6_entry = self.snmp.get_table('IPV6-MIB', 'ipv6AddrEntry')  #  'ipv6IfDescr'
        self.port_channel_ports = self.snmp.get_table('IEEE8023-LAG-MIB', 'dot3adAggPortAttachedAggID')

        self.sys_location = self.snmp.get_property('SNMPv2-MIB', 'sysLocation', 0)
        self.sys_contact = self.snmp.get_property('SNMPv2-MIB', 'sysContact', 0),

        self.logger.info('MIB Tables loaded successfully')


    def _get_entity_table(self):
        """Read Entity-MIB and filter out device's structure and all it's elements, like ports, modules, chassis, etc.

        :rtype: QualiMibTable
        :return: structured and filtered EntityPhysical table.
        """

        result_dict = QualiMibTable('entPhysicalTable')

        entity_table_critical_port_attr = {'entPhysicalContainedIn': 'str', 'entPhysicalClass': 'str',
                                           'entPhysicalVendorType': 'str'}
        entity_table_optional_port_attr = {'entPhysicalDescr': 'str', 'entPhysicalName': 'str'}

        physical_indexes = self.snmp.get_table('ENTITY-MIB', 'entPhysicalParentRelPos')
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

            for item in self.entity_table_black_list:
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
                    if port_id and port_id in self.if_table and port_id not in self.port_mapping.values():
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
            if_table = self.if_table[self.port_mapping[port]].copy()
            if_table.update(self.snmp.get_properties('IF-MIB', self.port_mapping[port], if_table_port_attr))
            interface_name = self.if_table[self.port_mapping[port]]['ifDescr']
            if interface_name == '':
                interface_name = self.entity_table[port]['entPhysicalName']
            if interface_name == '':
                continue
            interface_type = if_table[self.port_mapping[port]]['ifType'].replace('/', '').replace("'", '')
            attribute_map = {'l2_protocol_type': interface_type,
                             'mac': if_table[self.port_mapping[port]]['ifPhysAddress'],
                             'mtu': if_table[self.port_mapping[port]]['ifMtu'],
                             'bandwidth': if_table[self.port_mapping[port]]['ifSpeed'],
                             'description': self.snmp.get_property('IF-MIB', 'ifAlias', self.port_mapping[port]),
                             'adjacent': self._get_adjacent(self.port_mapping[port])}
            attribute_map.update(self._get_interface_details(self.port_mapping[port]))
            attribute_map.update(self._get_ip_interface_details(self.port_mapping[port]))
            port_object = Port(name=interface_name, relative_path=self.relative_path[port], **attribute_map)
            self._add_resource(port_object)
            self.logger.info('Added ' + interface_name + ' Port')
        self.logger.info('Finished Loading Ports')

