#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.shell.flows.connectivity.basic_flow import AbstractConnectivityFlow

from cloudshell.networking.huawei.command_actions.add_remove_vlan_actions import (
    AddRemoveVlanActions,
)


class HuaweiConnectivityFlow(AbstractConnectivityFlow):
    CISCO_SUB_INTERFACE_ERROR = "Vlan range is not supported for IOS Router devices"

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

    def _add_vlan_flow(self, vlan_range, port_mode, port_name, qnq, c_tag):
        """Add VLAN, has to be implemented."""
        pass

    def _remove_vlan_flow(self, vlan_range, port_name, port_mode):
        """Remove VLAN, has to be implemented."""
        pass
