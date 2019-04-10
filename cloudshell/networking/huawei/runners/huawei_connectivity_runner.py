#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.connectivity_runner import ConnectivityRunner

from cloudshell.networking.huawei.flows.huawei_add_vlan_flow import HuaweiAddVlanFlow
from cloudshell.networking.huawei.flows.huawei_remove_vlan_flow import HuaweiRemoveVlanFlow


class HuaweiConnectivityRunner(ConnectivityRunner):

    @property
    def add_vlan_flow(self):
        return HuaweiAddVlanFlow(self.cli_handler, self._logger)

    @property
    def remove_vlan_flow(self):
        return HuaweiRemoveVlanFlow(self.cli_handler, self._logger)
