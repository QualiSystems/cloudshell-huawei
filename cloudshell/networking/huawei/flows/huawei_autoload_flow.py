#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.networking.cisco.autoload.cisco_generic_snmp_autoload import CiscoGenericSNMPAutoload
from cloudshell.networking.cisco.cisco_command_actions import get_current_snmp_communities, disable_snmp, enable_snmp
from cloudshell.networking.devices.flows.action_flows import BaseFlow
from cloudshell.snmp.quali_snmp import QualiSnmp
from cloudshell.snmp.snmp_parameters import SNMPV2Parameters


class CiscoAutoloadFlow(BaseFlow):
    def __init__(self, cli_handler, logger, resource_name, autoload_class):
        super(CiscoAutoloadFlow, self).__init__(cli_handler, logger)
        self._resource_name = resource_name
        self._cisco_autoload_class = autoload_class
        self._snmp_command_actions = CiscoGenericSNMPAutoload

    def execute_flow(self, bool_enable_snmp, bool_disable_snmp, snmp_parameters, supported_os):
        """Facilitate SNMP autoload, enable and disable SNMP if needed.

        :param bool_enable_snmp: bool Enable SNMP Attribute
        :param bool_disable_snmp: bool Disable SNMP Attribute
        :param SNMPParameters snmp_parameters: snmp parameters class
        :param supported_os: supported os regexp
        :return: AutoloadDetails
        """

        try:
            if bool_enable_snmp and isinstance(snmp_parameters, SNMPV2Parameters):
                with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as session:
                    current_snmp_config = get_current_snmp_communities(session)
                    with session.enter_mode(self._cli_handler.config_mode) as config_session:
                        if snmp_parameters.snmp_community not in current_snmp_config:
                            enable_snmp(config_session, snmp_parameters.snmp_community)
            else:
                self._logger.info("Enable SNMP skipped: Enable SNMP attribute set to False or SNMP Version = v3")
            result = self.run_autoload(snmp_parameters, supported_os)
        finally:
            if bool_disable_snmp and isinstance(snmp_parameters, SNMPV2Parameters):
                with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
                    disable_snmp(config_session, snmp_parameters.snmp_community)
            else:
                self._logger.info(
                    "Disable SNMP skipped: Disable SNMP attribute set to False and/or SNMP Version = v3")

        return result

    def run_autoload(self, snmp_parameters, supported_os):
        """Executes device autoload discovery

        :param SNMPParameters snmp_parameters: snmp parameters class
        :param supported_os: supported os regexp
        :return: AutoloadDetails
        """

        snmp_handler = QualiSnmp(snmp_parameters, self._logger)
        snmp_command_actions = self._cisco_autoload_class(snmp_handler=snmp_handler,
                                                          logger=self._logger,
                                                          supported_os=supported_os,
                                                          resource_name=self._resource_name)
        return snmp_command_actions.discover()
