#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.action_flows import AddVlanFlow
from cloudshell.networking.huawei.command_actions.add_remove_vlan_actions import AddRemoveVlanActions
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions


class HuaweiRemoveVlanFlow(AddVlanFlow):
    def __init__(self, cli_handler, logger):
        super(HuaweiRemoveVlanFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """ Configures VLANs on multiple ports or port-channels """

        self._logger.info("Remove VLAN(s) {} configuration started".format(vlan_range))

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            add_vlan_actions = AddRemoveVlanActions(config_session, self._logger)
            system_actions = SystemActions(config_session, self._logger)
            port_name = add_vlan_actions.get_port_name(port_name)

            current_config = system_actions.display_running_config(port_name=port_name)
            add_vlan_actions.configure_interface(port_name=port_name)
            system_actions.clean_current_configuration_on_interface(configuration=current_config)
            system_actions.commit()

            current_config = system_actions.display_running_config(port_name=port_name)
            if "vlan {vlan_range}".format(vlan_range=vlan_range) in current_config:
                raise Exception("[FAIL] VLAN(s) {} removing failed".format(vlan_range))
            self._logger.info("VLAN(s) {} removing completed successfully".format(vlan_range))
            return "[ OK ] VLAN(s) {} removing completed successfully".format(vlan_range)
