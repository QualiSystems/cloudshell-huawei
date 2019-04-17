#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.configuration_runner import ConfigurationRunner

from cloudshell.networking.huawei.flows.huawei_restore_flow import HuaweiRestoreFlow
from cloudshell.networking.huawei.flows.huawei_save_flow import HuaweiSaveFlow


class HuaweiConfigurationRunner(ConfigurationRunner):
    @property
    def restore_flow(self):
        return HuaweiRestoreFlow(self.cli_handler, self._logger)

    @property
    def save_flow(self):
        return HuaweiSaveFlow(self.cli_handler, self._logger)

    @property
    def file_system(self):
        return "flash:"
