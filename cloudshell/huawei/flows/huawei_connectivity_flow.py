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

    def _remove_vlan_flow(self, vlan_range, full_name, port_mode, vm_uid):
        """Remove configuration of VLANs on multiple ports or port-channels.

        :param vlan_range: VLAN or VLAN range
        :param full_name: full port name
        :param port_mode: mode which will be configured on port.
            Possible Values are trunk and access
        :return:
        """
        pass

    def _remove_all_vlan_flow(self, full_name, vm_uid):
        """Remove configuration of VLANs on multiple ports or port-channels.

        :param port_name: full port name
            Possible Values are trunk and access
        :return:
        """
        pass
