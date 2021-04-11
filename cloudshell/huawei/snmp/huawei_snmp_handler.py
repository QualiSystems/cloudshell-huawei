#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.snmp.snmp_configurator import (
    EnableDisableSnmpConfigurator,
    EnableDisableSnmpFlowInterface,
)

from cloudshell.huawei.flows.huawei_disable_snmp_flow import HuaweiDisableSnmpFlow
from cloudshell.huawei.flows.huawei_enable_snmp_flow import HuaweiEnableSnmpFlow


class HuaweiEnableDisableSnmpFlow(EnableDisableSnmpFlowInterface):
    DEFAULT_SNMP_VIEW = "quali_snmp_view"
    DEFAULT_SNMP_GROUP = "quali_snmp_group"

    def __init__(self, cli_handler, logger):
        """Enable snmp flow."""
        self._logger = logger
        self._cli_handler = cli_handler

    def enable_snmp(self, snmp_parameters):
        HuaweiEnableSnmpFlow(self._cli_handler, self._logger).enable_flow(
            snmp_parameters
        )

    def disable_snmp(self, snmp_parameters):
        HuaweiDisableSnmpFlow(self._cli_handler, self._logger).disable_flow(
            snmp_parameters
        )


class HuaweiSnmpHandler(EnableDisableSnmpConfigurator):
    def __init__(self, resource_config, logger, cli_handler):
        self.cli_handler = cli_handler
        enable_disable_snmp_flow = HuaweiEnableDisableSnmpFlow(self.cli_handler, logger)
        super(HuaweiSnmpHandler, self).__init__(
            enable_disable_snmp_flow, resource_config, logger
        )
