#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.connectivity.basic_flow import AbstractConnectivityFlow
from cloudshell.shell.flows.connectivity.models.connectivity_model import (
    ConnectivityActionModel,
)
from cloudshell.shell.flows.connectivity.models.driver_response import (
    ConnectivityActionResult,
)
from cloudshell.shell.flows.connectivity.parse_request_service import (
    ParseConnectivityRequestService,
)


class HuaweiConnectivityFlow(AbstractConnectivityFlow):
    def __init__(
        self,
        cli_handler,
        logger,
        support_vlan_range_str=False,
        support_multi_vlan_str=False,
    ):
        parse_connectivity_service = ParseConnectivityRequestService(
            is_vlan_range_supported=support_vlan_range_str,
            is_multi_vlan_supported=support_multi_vlan_str,
        )
        super().__init__(parse_connectivity_service, logger)
        self._cli_handler = cli_handler

    def _set_vlan(self, action: ConnectivityActionModel) -> ConnectivityActionResult:
        vlan_range = action.connection_params.vlan_id
        port_mode = action.connection_params.mode.value
        full_name = action.action_target.name
        qnq = action.connection_params.vlan_service_attrs.qnq
        c_tag = action.connection_params.vlan_service_attrs.ctag
        self._add_vlan_flow(vlan_range, port_mode, full_name, qnq, c_tag)
        return ConnectivityActionResult.success_result(
            action, f"VLAN(s) {vlan_range} configuration completed"
        )

    def _remove_vlan(self, action: ConnectivityActionModel) -> ConnectivityActionResult:
        vlan_range = action.connection_params.vlan_id
        full_name = action.action_target.name
        self._remove_vlan_flow(vlan_range, full_name)
        return ConnectivityActionResult.success_result(
            action, f"VLAN(s) {vlan_range} removal completed"
        )

    def _add_vlan_flow(self, vlan_range, port_mode, full_name, qnq, c_tag):
        """Configure VLANs on multiple ports or port-channels.

        :param vlan_range: VLAN or VLAN range
        :param port_mode: mode which will be configured on port.
            Possible Values are trunk and access
        :param full_name: full port name
        :param qnq:
        :param c_tag:
        :return:
        """
        pass

    def _remove_vlan_flow(self, vlan_range, full_name):
        """Remove configuration of VLANs on multiple ports or port-channels.

        :param vlan_range: VLAN or VLAN range
        :param full_name: full port name
        :return:
        """
        pass
