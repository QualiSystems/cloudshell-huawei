#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.snmp_handler import SnmpHandler

from cloudshell.networking.huawei.flows.huawei_enable_snmp_flow import HuaweiEnableSnmpFlow
from cloudshell.networking.huawei.flows.huawei_disable_snmp_flow import HuaweiDisableSnmpFlow


class HuaweiSnmpHandler(SnmpHandler):
    def __init__(self, resource_config, logger, api, cli_handler):
        super(HuaweiSnmpHandler, self).__init__(resource_config, logger, api)
        self.cli_handler = cli_handler

    def _create_enable_flow(self):
        return HuaweiEnableSnmpFlow(self.cli_handler, self._logger)

    def _create_disable_flow(self):
        return HuaweiDisableSnmpFlow(self.cli_handler, self._logger)
