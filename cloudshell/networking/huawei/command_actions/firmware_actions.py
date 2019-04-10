#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor
from cloudshell.networking.huawei.command_templates import firmware


class FirmwareActions(object):

    def __init__(self, cli_service, logger):
        """ Update firmware actions """

        self._cli_service = cli_service
        self._logger = logger

    def update_firmware(self, firmware_file):
        """ Update firmware """

        output = CommandTemplateExecutor(self._cli_service,
                                         firmware.STARTUP_SYSTEM_SOFTWARE).execute_command(dst_file=firmware_file)

        if not re.search(r"Succeeded", output, re.IGNORECASE | re.DOTALL):
            raise Exception("Failed to upgrade firmware")
