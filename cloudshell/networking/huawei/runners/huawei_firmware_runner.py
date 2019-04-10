#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.firmware_runner import FirmwareRunner
from cloudshell.networking.huawei.flows.huawei_load_firmware_flow import HuaweiLoadFirmwareFlow


class HuaweiFirmwareRunner(FirmwareRunner):
    @property
    def load_firmware_flow(self):
        return HuaweiLoadFirmwareFlow(self.cli_handler, self._logger)
