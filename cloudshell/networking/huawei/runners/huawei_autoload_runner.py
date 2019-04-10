#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.autoload_runner import AutoloadRunner
from cloudshell.networking.huawei.flows.huawei_autoload_flow import HuaweiSnmpAutoloadFlow


class HuaweiAutoloadRunner(AutoloadRunner):
    def __init__(self, resource_config, logger, snmp_handler):
        super(HuaweiAutoloadRunner, self).__init__(resource_config, logger)
        self.snmp_handler = snmp_handler

    @property
    def autoload_flow(self):
        return HuaweiSnmpAutoloadFlow(self.snmp_handler, self._logger)


# class HuaweiAutoloadRunner(AutoloadRunner):
#     def __init__(self, resource_config, logger, snmp_handler):
#         super(HuaweiAutoloadRunner, self).__init__(resource_config)
#         self._logger = logger
#         self.snmp_handler = snmp_handler
#
#     @property
#     def autoload_flow(self):
#         return HuaweiSnmpAutoloadFlow(self.snmp_handler, self._logger)
