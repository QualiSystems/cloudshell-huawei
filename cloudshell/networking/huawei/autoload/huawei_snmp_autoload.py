#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os

from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder
from cloudshell.devices.standards.networking.autoload_structure import *
from cloudshell.networking.huawei.autoload.snmp_entity_table import HuaweiSNMPEntityTable
from cloudshell.networking.huawei.autoload.snmp_if_table import SnmpIfTable


class HuaweiGenericSNMPAutoload(object):
    VENDOR = "Huawei"
    IF_ENTITY = "ifDescr"
    ENTITY_PHYSICAL = "entPhysicalDescr"
    SNMP_ERRORS = [r'No\s+Such\s+(Object|Instance)\s+currently\s+exists']
    # DEVICE_NAMES_MAP_FILE = os.path.join(os.path.dirname(__file__), os.pardir, "mibs", "device_names_map.csv")

    def __init__(self, snmp_handler, shell_name, shell_type, resource_name, logger):
        """Basic init with injected snmp handler and logger

        :param snmp_handler:
        :param logger:
        :return:
        """

        self.snmp_handler = snmp_handler
        self.shell_name = shell_name
        self.shell_type = shell_type
        self.resource_name = resource_name
        self.logger = logger
        self.elements = {}
        self.snmp_handler.set_snmp_errors(self.SNMP_ERRORS)
        self.resource = GenericResource(shell_name=shell_name,
                                        shell_type=shell_type,
                                        name=resource_name,
                                        unique_id=resource_name)

    def load_mibs(self):
        """
        Loads specific mibs inside snmp handler

        """
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mibs"))
        self.snmp_handler.update_mib_sources(path)

    def discover(self, supported_os):
        """General entry point for autoload,
        read device structure and attributes: chassis, modules, submodules, ports, port-channels and power supplies

        :return: AutoLoadDetails object
        """

        if not self._is_valid_device_os(supported_os):
            raise Exception(self.__class__.__name__, 'Unsupported device OS')

        self.logger.info("*" * 70)
        self.logger.info("Start SNMP discovery process .....")
        self.load_mibs()
        self.snmp_handler.load_mib(["HUAWEI-PORT-MIB", "HUAWEI-TC-MIB"])
        self._get_device_details()
        self._load_snmp_tables()

        if self.huawei_entity.chassis_list:
            self._get_chassis_attributes(self.huawei_entity.chassis_list)
            self._get_power_ports(self.huawei_entity.power_port_list)
            self._get_module_attributes(self.huawei_entity.module_list)
            self._get_ports_attributes(self.huawei_entity.port_list)
            self._get_port_channels()
        else:
            self.logger.error("Entity table error, no chassis found")

        autoload_details = AutoloadDetailsBuilder(self.resource).autoload_details()
        if not self.shell_name:
            root_model_name = [x for x in autoload_details.attributes if
                               x.relative_address == "" and x.attribute_name == "Model Name"][0]
            if root_model_name:
                autoload_details.attributes.remove(root_model_name)
        self._log_autoload_details(autoload_details)
        return autoload_details

    def _log_autoload_details(self, autoload_details):
        """
        Logging autoload details
        :param autoload_details:
        :return:
        """
        self.logger.debug("-------------------- <RESOURCES> ----------------------")
        for resource in autoload_details.resources:
            self.logger.debug(
                "{0:15}, {1:20}, {2}".format(resource.relative_address, resource.name, resource.unique_identifier))
        self.logger.debug("-------------------- </RESOURCES> ----------------------")

        self.logger.debug("-------------------- <ATTRIBUTES> ---------------------")
        for attribute in autoload_details.attributes:
            self.logger.debug("-- {0:15}, {1:60}, {2}".format(attribute.relative_address, attribute.attribute_name,
                                                              attribute.attribute_value))
        self.logger.debug("-------------------- </ATTRIBUTES> ---------------------")

    def _is_valid_device_os(self, supported_os):
        """Validate device OS using snmp
            :return: True or False
        """

        system_description = self.snmp_handler.get_property('SNMPv2-MIB', 'sysDescr', '0')
        self.logger.debug('Detected system description: \'{0}\''.format(system_description))
        result = re.search(r"({0})".format("|".join(supported_os)),
                           system_description,
                           flags=re.DOTALL | re.IGNORECASE)

        if result:
            return True
        else:
            error_message = 'Incompatible driver! Please use this driver for \'{0}\' operation system(s)'. \
                format(str(tuple(supported_os)))
            self.logger.error(error_message)
            return False

    def _get_device_model(self):
        """Get device model from the SNMPv2 mib

        :return: device model
        :rtype: str
        """
        result = ''
        match_name = re.search(r'::(?P<model>\S+$)', self.snmp_handler.get_property('SNMPv2-MIB', 'sysObjectID', '0'))
        if match_name:
            result = match_name.group('model')

        return result

    def _get_device_model_name(self, device_model):
        """Get device model name from the CSV file map

        :param str device_model:  device model
        :return: device model model
        :rtype: str
        """

        # return get_device_name(file_name=self.DEVICE_NAMES_MAP_FILE, sys_obj_id=device_model)
        return device_model

    def _get_device_os_version(self):
        """Get device OS Version form snmp SNMPv2 mib

        :return: device model
        :rtype: str
        """

        result = ""
        matched = re.search(r"Version (?P<os_version>[^\s,]+)",
                            self.snmp_handler.get_property('SNMPv2-MIB', 'sysDescr', '0'))
        if matched:
            result = matched.groupdict().get("os_version", "")
        return result

    def _get_device_details(self):
        """ Get root element attributes """

        self.logger.info("Building Root")

        self.resource.contact_name = self.snmp_handler.get_property('SNMPv2-MIB', 'sysContact', '0')
        self.resource.system_name = self.snmp_handler.get_property('SNMPv2-MIB', 'sysName', '0')
        self.resource.location = self.snmp_handler.get_property('SNMPv2-MIB', 'sysLocation', '0')
        self.resource.os_version = self._get_device_os_version()
        self.resource.model = self._get_device_model()
        self.resource.model_name = self._get_device_model_name(self.resource.model)
        self.resource.vendor = self.VENDOR

    def _load_snmp_tables(self):
        """ Load all Huawei required snmp tables

        :return:
        """

        self.logger.info('Start loading MIB tables:')
        self.if_table = SnmpIfTable(snmp_handler=self.snmp_handler, logger=self.logger)
        self.logger.info('{0} table loaded'.format(self.IF_ENTITY))
        self.huawei_entity = HuaweiSNMPEntityTable(self.snmp_handler, self.logger, self.if_table)
        self.entity_table = self.huawei_entity.get_entity_table()
        self.logger.info('Entity table loaded')

        self.logger.info('MIB Tables loaded successfully')

    def _add_element(self, relative_path, resource, parent_id=""):
        """Add object data to resources and attributes lists

        :param resource: object which contains all required data for certain resource
        """

        rel_seq = relative_path.split("/")

        if len(rel_seq) == 1:  # Chassis connected directly to root
            self.resource.add_sub_resource(relative_path, resource)
        else:
            if parent_id:
                parent_object = self.elements.get(parent_id, self.resource)
            else:
                parent_object = self.elements.get("/".join(rel_seq[:-1]), self.resource)

            rel_path = re.search(r"\d+", rel_seq[-1]).group()
            parent_object.add_sub_resource(rel_path, resource)
            # parent_object.add_sub_resource(rel_seq[-1], resource)

        self.elements.update({relative_path: resource})

    def _get_chassis_attributes(self, chassis_list):
        """ Get Chassis element attributes """

        self.logger.info("Building Chassis")
        for chassis in chassis_list:
            chassis_id = self.huawei_entity.relative_address[chassis]

            chassis_object = GenericChassis(shell_name=self.shell_name,
                                            name="Chassis {}".format(chassis_id),
                                            unique_id="{}.{}.{}".format(self.resource_name, "chassis", chassis))

            chassis_object.model = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalModelName", chassis) or \
                                   self.entity_table[chassis]["entPhysicalDescr"]
            chassis_object.serial_number = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalSerialNum", chassis)

            relative_address = "{0}".format(chassis_id)

            self._add_element(relative_path=relative_address, resource=chassis_object)

            self.logger.info("Added " + self.entity_table[chassis]["entPhysicalDescr"] + " Chassis")
        self.logger.info("Building Chassis completed")

    def _get_module_attributes(self, module_list):
        """ Set attributes for all discovered modules """

        self.logger.info("Building Modules")
        for module in module_list:
            module_id = self.huawei_entity.relative_address.get(module)
            if not module_id:
                continue

            module_index = module_id.split("/")[-1]
            if "/" in module_id and len(module_id.split("/")) < 3:
                module_object = GenericModule(shell_name=self.shell_name,
                                              name="Module {}".format(module_index),
                                              unique_id="{0}.{1}.{2}".format(self.resource_name, "module", module))

            else:
                module_object = GenericSubModule(shell_name=self.shell_name,
                                                 name="Sub Module {}".format(module_index),
                                                 unique_id="{0}.{1}.{2}".format(self.resource_name, "sub_module",
                                                                                module))

            module_object.model = self.entity_table[module]["entPhysicalDescr"]
            module_object.version = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalSoftwareRev", module)
            module_object.serial_number = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalSerialNum", module)

            self._add_element(relative_path=module_id, resource=module_object)
            self.logger.info("Module {} added".format(self.entity_table[module]["entPhysicalDescr"]))

        self.logger.info("Building Modules completed")

    def _get_power_ports(self, power_supply_list):
        """Get attributes for power ports provided in self.power_supply_list

        :return:
        """

        self.logger.info("Building PowerPorts")
        for port in power_supply_list:
            port_id = self.entity_table[port]["entPhysicalParentRelPos"]
            parent_index = int(self.entity_table[port]["entPhysicalContainedIn"])
            chassis_id = self.huawei_entity.get_relative_address(parent_index)
            if "/" in chassis_id:
                chassis_id = chassis_id.split("/")[0]
            relative_address = "{0}/PP{1}".format(chassis_id, port_id)

            power_port = GenericPowerPort(shell_name=self.shell_name,
                                          name="PP{0}".format(power_supply_list.index(port)),
                                          unique_id="{0}.{1}.{2}".format(self.resource_name, "power_port", port))

            power_port.model = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalModelName", port)
            power_port.port_description = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalDescr", port)
            power_port.version = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalHardwareRev", port)
            power_port.serial_number = self.snmp_handler.get_property("ENTITY-MIB", "entPhysicalSerialNum", port)

            self._add_element(relative_path=relative_address, resource=power_port, parent_id=chassis_id)

            self.logger.info("Added " + self.entity_table[port]["entPhysicalName"].strip(" \t\n\r") + " Power Port")
        self.logger.info("Building Power Ports completed")

    def _get_port_channels(self):
        """Get all port channels and set attributes for them

        :return:
        """

        if not self.if_table.if_port_channels:
            return
        self.logger.info("Building Port Channels")
        for if_port_channel in self.if_table.if_port_channels:
            interface_model = if_port_channel.if_name
            match_object = re.search(r"\d+$", interface_model)
            if match_object:
                interface_id = "{0}".format(match_object.group(0))
                associated_ports = ""
                for port in if_port_channel.associated_port_list:
                    if_port_name = self.if_table.get_if_entity_by_index(port).if_name
                    associated_ports = if_port_name.replace('/', '-').replace(' ', '') + '; '

                port_channel = GenericPortChannel(shell_name=self.shell_name,
                                                  name=interface_model,
                                                  unique_id="{0}.{1}.{2}".format(self.resource_name,
                                                                                 "port_channel",
                                                                                 interface_id))

                port_channel.associated_ports = associated_ports.strip(' \t\n\r')
                port_channel.port_description = if_port_channel.if_port_description
                port_channel.ipv4_address = if_port_channel.ipv4_address
                port_channel.ipv6_address = if_port_channel.ipv6_address

                self._add_element(relative_path=interface_id, resource=port_channel)
                self.logger.info("Added " + interface_model + " Port Channel")

            else:
                self.logger.error("Adding of {0} failed. Name is invalid".format(interface_model))

        self.logger.info("Building Port Channels completed")

    def _get_ports_attributes(self, port_list):
        """Get resource details and attributes for every port in self.port_list

        :return:
        """

        self.logger.info("Load Ports:")
        for port in port_list:
            port_if_entity = self.huawei_entity.port_mapping.get(port)
            if not port_if_entity:
                continue
            interface_name = port_if_entity.if_name or self.entity_table[port]['entPhysicalName']
            if interface_name == '':
                continue

            port_object = GenericPort(shell_name=self.shell_name,
                                      name=interface_name.replace("/", "-"),
                                      unique_id="{0}.{1}.{2}".format(self.resource_name, "port", port))
            port_object.mac_address = port_if_entity.if_mac
            port_object.l2_protocol_type = port_if_entity.if_type
            port_object.ipv4_address = port_if_entity.ipv4_address
            port_object.ipv6_address = port_if_entity.ipv6_address
            port_object.port_description = port_if_entity.if_port_description
            port_object.bandwidth = port_if_entity.if_speed
            port_object.mtu = port_if_entity.if_mtu
            port_object.duplex = port_if_entity.duplex
            port_object.adjacent = port_if_entity.adjacent
            port_object.auto_negotiation = port_if_entity.auto_negotiation
            port_object.mac_address = port_if_entity.if_mac

            self._add_element(relative_path=self.huawei_entity.relative_address[port], resource=port_object)
            self.logger.info("Added " + interface_name + " Port")

        self.logger.info("Building Ports completed")
