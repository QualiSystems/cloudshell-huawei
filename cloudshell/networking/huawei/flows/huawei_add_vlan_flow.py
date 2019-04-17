#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.action_flows import AddVlanFlow
from cloudshell.networking.huawei.command_actions.add_remove_vlan_actions import AddRemoveVlanActions
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions


class HuaweiAddVlanFlow(AddVlanFlow):
    def __init__(self, cli_handler, logger):
        super(HuaweiAddVlanFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """ Configures VLANs on multiple ports or port-channels """

        self._logger.info("Add VLAN(s) {} configuration started".format(vlan_range))
        if port_mode not in ["trunk", "access"]:
            raise Exception("Unsupported port mode '{}'. Should be 'trunk' or 'access'".format(port_mode))

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            add_vlan_actions = AddRemoveVlanActions(config_session, self._logger)
            system_actions = SystemActions(config_session, self._logger)
            port_name = add_vlan_actions.get_port_name(port_name)

            # Preparation
            current_config = system_actions.display_running_config(port_name=port_name)
            add_vlan_actions.configure_interface(port_name=port_name)
            system_actions.clean_current_configuration_on_interface(configuration=current_config)
            add_vlan_actions.activate_port()
            add_vlan_actions.activate_port_mode()

            # VLAN configuration
            if "-" in vlan_range:  # means that it is range
                start_vlan, end_vlan = vlan_range.split("-")
                add_vlan_actions.create_vlan_range(start_vlan, end_vlan)
                add_vlan_actions.set_vlan_range_to_interface(start_vlan, end_vlan, port_mode)
            else:  # single VLAN
                add_vlan_actions.create_vlan(vlan_range)
                add_vlan_actions.set_vlan_to_interface(vlan_range, port_mode, qnq)

            system_actions.commit()
            current_config = system_actions.display_running_config(port_name=port_name)
            if not "vlan {vlan_range}".format(vlan_range=vlan_range) in current_config:
                raise Exception("[FAIL] VLAN(s) {} configuration failed".format(vlan_range))
            self._logger.info("VLAN(s) {} configuration completed successfully".format(vlan_range))
            return "[ OK ] VLAN(s) {} configuration completed successfully".format(vlan_range)
