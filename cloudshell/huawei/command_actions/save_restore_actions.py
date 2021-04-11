#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.huawei.command_templates import configuration
from cloudshell.huawei.helpers.exceptions import HuaweiSaveRestoreException


class SaveRestoreActions(object):
    def __init__(self, cli_service, logger):
        """Save and Restore actions."""
        self._cli_service = cli_service
        self._logger = logger

    def get_file(self, server_address, src_file, dst_file):
        """Download file from remote server to device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.TFTP_GET
        ).execute_command(host=server_address, src=src_file, dst=dst_file)
        if not re.search(r"Downloading the file successfully", output, re.DOTALL):
            raise HuaweiSaveRestoreException(
                "Failed to download configuration/software file {src_file}"
                " from remote server {host}".format(
                    src_file=src_file, host=server_address
                )
            )

    def put_file(self, server_address, src_file, dst_file):
        """Upload file to remote server from device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.TFTP_PUT
        ).execute_command(host=server_address, src=src_file, dst=dst_file)
        self._device_response_verification(output)

    def copy_file(self, src_file, dst_file):
        """Copy configuration/software file inside local device storage."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.COPY
        ).execute_command(src=src_file, dst=dst_file)
        self._device_response_verification(output)

    def _device_response_verification(self, output):
        match = re.search(
            r"\d+ bytes copied|copied.*[\[\(].*[0-9]* bytes.*[\)\]]|[Cc]opy complete",
            output,
            re.IGNORECASE,
        )

        if not match:
            match_error = re.search(
                r"%.*|TFTP put operation failed.*|sysmgr.*not supported.*\n",
                output,
                re.IGNORECASE,
            )
            message = "Save Command failed. "
            if match_error:
                self._logger.error(message)
                message += re.sub(r"^%|\\n", "", match_error.group())
            else:
                error_match = re.search(r"error.*\n|fail.*\n", output, re.IGNORECASE)
                if error_match:
                    self._logger.error(message)
                    message += error_match.group()
            raise HuaweiSaveRestoreException("Save Operation", message)

    def save_runninig_config(self, dst_file):
        """Save running configuration to device local storage."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.SAVE_RUNNING
        ).execute_command(dst_file=dst_file)

        match = re.search(
            r"Save the configuration successfully", output, re.IGNORECASE | re.DOTALL
        )

        if not match:
            self._logger.error(
                "Failed to save running configuration to local storage: {}".format(
                    output
                )
            )
            raise HuaweiSaveRestoreException(
                "Failed to save running configuration to local storage"
            )

    def setup_startup_config(self, dst_file):
        """Specifies the system configuration file for next startup."""
        output = CommandTemplateExecutor(
            self._cli_service, configuration.SAVE_RUNNING
        ).execute_command(dst_file=dst_file)

        match = re.search(
            r"Succeeded in setting the configuration for booting system",
            output,
            re.IGNORECASE | re.DOTALL,
        )

        if not match:
            msg = "Failed to specifies the system configuration file for next startup"
            self._logger.error("{}: {}".format(msg, output))
            raise HuaweiSaveRestoreException(msg)
