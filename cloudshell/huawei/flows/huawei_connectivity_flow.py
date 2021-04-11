#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.connectivity.basic_flow import AbstractConnectivityFlow


class HuaweiConnectivityFlow(AbstractConnectivityFlow):
    def __init__(
        self,
        cli_handler,
        logger,
        support_vlan_range_str=False,
        support_multi_vlan_str=False,
    ):
        super(HuaweiConnectivityFlow, self).__init__(logger)
        self._cli_handler = cli_handler
        self.IS_VLAN_RANGE_SUPPORTED = support_vlan_range_str
        self.IS_MULTI_VLAN_SUPPORTED = support_multi_vlan_str

    def _add_vlan_flow(self, vlan_range, port_mode, full_name, qnq, c_tag, vm_uid):
        """Configures VLANs on multiple ports or port-channels.

        :param vlan_range: VLAN or VLAN range
        :param port_mode: mode which will be configured on port.
            Possible Values are trunk and access
        :param port_name: full port name
        :param qnq:
        :param c_tag:
        :return:
        """
        pass

    #         with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
    #             add_vlan_actions = AddRemoveVlanActions(config_session, self._logger)
    #             system_actions = SystemActions(config_session, self._logger)
    #             port_name = add_vlan_actions.get_port_name(port_name)
    #
    #             # Preparation
    #             current_config = system_actions.display_running_config(port_name=port_name)
    #             add_vlan_actions.configure_interface(port_name=port_name)
    #             system_actions.clean_current_configuration_on_interface(configuration=current_config)
    #             add_vlan_actions.activate_port()
    #             add_vlan_actions.activate_port_mode()
    #
    #             # VLAN configuration
    #             if "-" in vlan_range:  # means that it is range
    #                 start_vlan, end_vlan = vlan_range.split("-")
    #                 add_vlan_actions.create_vlan_range(start_vlan, end_vlan)
    #                 add_vlan_actions.set_vlan_range_to_interface(start_vlan, end_vlan, port_mode)
    #             else:  # single VLAN
    #                 add_vlan_actions.create_vlan(vlan_range)
    #                 add_vlan_actions.set_vlan_to_interface(vlan_range, port_mode, qnq)
    #
    #             system_actions.commit()
    #             current_config = system_actions.display_running_config(port_name=port_name)
    #             if not "vlan {vlan_range}".format(vlan_range=vlan_range) in current_config:
    #                 raise Exception("[FAIL] VLAN(s) {} configuration failed".format(vlan_range))
    #             self._logger.info("VLAN(s) {} configuration completed successfully".format(vlan_range))
    #             return "[ OK ] VLAN(s) {} configuration completed successfully".format(vlan_range)

    def _remove_vlan_flow(self, vlan_range, full_name, port_mode, vm_uid):
        """Remove configuration of VLANs on multiple ports or port-channels.

        :param vlan_range: VLAN or VLAN range
        :param full_name: full port name
        :param port_mode: mode which will be configured on port.
            Possible Values are trunk and access
        :return:
        """
        pass

    #         self._logger.info("Remove VLAN(s) {} configuration started".format(vlan_range))
    #
    #         with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
    #             add_vlan_actions = AddRemoveVlanActions(config_session, self._logger)
    #             system_actions = SystemActions(config_session, self._logger)
    #             port_name = add_vlan_actions.get_port_name(port_name)
    #
    #             current_config = system_actions.display_running_config(port_name=port_name)
    #             add_vlan_actions.configure_interface(port_name=port_name)
    #             system_actions.clean_current_configuration_on_interface(configuration=current_config)
    #             system_actions.commit()
    #
    #             current_config = system_actions.display_running_config(port_name=port_name)
    #             if "vlan {vlan_range}".format(vlan_range=vlan_range) in current_config:
    #                 raise Exception("[FAIL] VLAN(s) {} removing failed".format(vlan_range))
    #             self._logger.info("VLAN(s) {} removing completed successfully".format(vlan_range))
    #             return "[ OK ] VLAN(s) {} removing completed successfully".format(vlan_range)

    def _remove_all_vlan_flow(self, full_name, vm_uid):
        """Remove configuration of VLANs on multiple ports or port-channels.

        :param port_name: full port name
            Possible Values are trunk and access
        :return:
        """
        pass
