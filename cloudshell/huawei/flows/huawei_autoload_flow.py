#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from cloudshell.shell.flows.autoload.basic_flow import AbstractAutoloadFlow

from cloudshell.huawei.autoload.huawei_generic_snmp_autoload import (
    HuaweiGenericSNMPAutoload,
)


class HuaweiSnmpAutoloadFlow(AbstractAutoloadFlow):
    MIBS_FOLDER = os.path.join(os.path.dirname(__file__), os.pardir, "mibs")

    def __init__(self, logger, snmp_handler):
        super().__init__(logger)
        self._snmp_handler = snmp_handler

    def _autoload_flow(self, supported_os, resource_model):
        with self._snmp_handler.get_service() as snmp_service:
            snmp_service.add_mib_folder_path(self.MIBS_FOLDER)
            snmp_service.load_mib_tables(
                [
                    "HUAWEI-PORT-MIB",
                    "HUAWEI-TC-MIB",
                ]
            )
            snmp_autoload = HuaweiGenericSNMPAutoload(
                snmp_handler=snmp_service,
                logger=self._logger,
                resource_model=resource_model,
            )

            return snmp_autoload.discover(supported_os)
