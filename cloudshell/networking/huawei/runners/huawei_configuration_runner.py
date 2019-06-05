#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.configuration_runner import ConfigurationRunner

from cloudshell.networking.huawei.flows.huawei_restore_flow import HuaweiRestoreFlow
from cloudshell.networking.huawei.flows.huawei_save_flow import HuaweiSaveFlow
from cloudshell.networking.huawei.flows.huawei_file_system_flow import HuaweiFileSystemFlow


class HuaweiConfigurationRunner(ConfigurationRunner):
    @property
    def restore_flow(self):
        return HuaweiRestoreFlow(self.cli_handler, self._logger, self.file_system)

    @property
    def save_flow(self):
        return HuaweiSaveFlow(self.cli_handler, self._logger, self.file_system)

    @property
    def file_system(self):
        return HuaweiFileSystemFlow(self.cli_handler, self._logger).execute_flow()
        # return "flash"
