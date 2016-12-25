#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.networking.huawei.huawei_command_actions import get_port_name, create_vlan, \
    get_current_interface_config, set_vlan_to_interface, verify_interface_configured
from cloudshell.networking.devices.flows.action_flows import AddVlanFlow


class HuaweiAddVlanFlow(AddVlanFlow):
    def __init__(self, cli_handler, logger):
        super(HuaweiAddVlanFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """ Configures VLANs on multiple ports or port-channels

        :param vlan_range: VLAN or VLAN range
        :param port_mode: mode which will be configured on port. Possible Values are trunk and access
        :param port_name: full port name
        :param qnq:
        :param c_tag:
        :return:
        """

        port_name = get_port_name(self._logger, port_name)
        self._logger.info("Add VLAN(s) {} configuration started".format(vlan_range))
        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as session:
            with session.enter_mode(self._cli_handler.config_mode) as config_session:
                create_vlan(config_session, self._logger, vlan_range)
            with session.enter_mode(self._cli_handler.config_mode) as config_sesison:
                set_vlan_to_interface(config_sesison, self._logger, vlan_range, port_mode,
                                      port_name, qnq, c_tag)

            current_config = get_current_interface_config(session,
                                                          port_name=port_name)
            if not verify_interface_configured(vlan_range, current_config):
                raise Exception(self.__class__.__name__, "[FAIL] VLAN(s) {} configuration failed".format(vlan_range))
            self._logger.info("VLAN(s) {} configuration completed successfully".format(vlan_range))
            return "[ OK ] VLAN(s) {} configuration completed successfully".format(vlan_range)
