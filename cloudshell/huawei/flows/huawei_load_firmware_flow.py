#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.firmware.basic_flow import AbstractFirmwareFlow
from cloudshell.shell.flows.utils.url import RemoteURL

from cloudshell.huawei.command_actions.firmware_actions import FirmwareActions
from cloudshell.huawei.command_actions.save_restore_actions import SaveRestoreActions
from cloudshell.huawei.command_actions.system_actions import SystemActions
from cloudshell.huawei.helpers.exceptions import HuaweiFirmwareException


class HuaweiLoadFirmwareFlow(AbstractFirmwareFlow):
    FILE_SYSTEM = "flash"

    def __init__(self, cli_handler, logger, resource_config):
        super().__init__(logger, resource_config)
        self._cli_handler = cli_handler

    def _load_firmware_flow(self, firmware_url, vrf_management_name, timeout):
        """Load a firmware onto the device.

        :param firmware_url: The URL of the firmware file, including the firmware
            file name
        :param vrf_management_name: Virtual Routing and Forwarding Name
        :param timeout:
        :return:
        """
        firmware_file_name = firmware_url.filename
        if not firmware_file_name:
            raise HuaweiFirmwareException("Unable to find firmware file")

        with self._cli_handler.get_cli_service(
            self._cli_handler.config_mode
        ) as config_session:
            self._logger.info("Start updating firmware")
            config_actions = SaveRestoreActions(config_session, self._logger)
            firmware_actions = FirmwareActions(config_session, self._logger)
            system_actions = SystemActions(config_session, self._logger)

            if isinstance(firmware_url, RemoteURL):
                scheme = firmware_url.scheme.lower()
                if scheme not in ["ftp", "tftp"]:
                    raise HuaweiFirmwareException(
                        "Unsupported protocol. "
                        "Updating firmware possible from tftp, "
                        "ftp or local storage({}) only".format(self.FILE_SYSTEM)
                    )
                dst_file = "{file_system}:/{file_name}".format(
                    file_system=self.FILE_SYSTEM, file_name=firmware_file_name
                )
                config_actions.get_file(
                    server_address=firmware_url.host,
                    src_file=firmware_url.path.lstrip("/"),
                    dst_file=dst_file,
                )
            else:
                dst_file = firmware_url.url
                if not firmware_url.scheme:
                    dst_file = "{file_system}:/{file_path}".format(
                        file_system=self.FILE_SYSTEM,
                        file_path=firmware_url.path.lstrip("/"),
                    )

            firmware_actions.update_firmware(firmware_file=dst_file)
            system_actions.reboot()

            if firmware_file_name not in system_actions.display_running_config(boot=""):
                raise HuaweiFirmwareException(
                    "Can't add firmware '{}' for boot!".format(firmware_file_name)
                )
            if firmware_file_name not in system_actions.display_os_version():
                raise HuaweiFirmwareException(
                    "Failed to load firmware, Please check logs"
                )
