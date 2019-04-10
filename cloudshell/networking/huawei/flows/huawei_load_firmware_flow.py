#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.action_flows import LoadFirmwareFlow
from cloudshell.devices.networking_utils import UrlParser
from cloudshell.networking.huawei.command_actions.firmware_actions import FirmwareActions
from cloudshell.networking.huawei.command_actions.save_restore_actions import SaveRestoreActions
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions


class HuaweiLoadFirmwareFlow(LoadFirmwareFlow):
    FILE_SYSTEM = "flash"

    def __init__(self, cli_handler, logger):
        super(HuaweiLoadFirmwareFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, path, vrf, timeout):
        """Load a firmware onto the device

        :param path: The path to the firmware file, including the firmware file name
        :param vrf: Virtual Routing and Forwarding Name
        :param timeout:
        :return:
        """

        url = UrlParser().parse_url(path)
        firmware_file_name = url.get(UrlParser.FILENAME)
        if not firmware_file_name:
            raise Exception("Unable to find firmware file")

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            self._logger.info("Start updating firmware")
            config_actions = SaveRestoreActions(config_session, self._logger)
            firmware_actions = FirmwareActions(config_session, self._logger)
            system_actions = SystemActions(config_session, self._logger)

            scheme = url.get(UrlParser.SCHEME).lower()
            if not scheme:
                dst_file = "{file_system}:/{file_path}".format(file_system=self.FILE_SYSTEM, file_path=path.lstrip("/"))
            elif scheme == self.FILE_SYSTEM:
                dst_file = path
            elif scheme in ["ftp", "tftp"]:
                dst_file = "{file_system}:/{file_name}".format(file_system=self.FILE_SYSTEM,
                                                               file_name=firmware_file_name)
                config_actions.get_file(server_address=url.get(UrlParser.HOSTNAME),
                                        src_file="{path}/{file}".format(path=url.get(UrlParser.PATH),
                                                                        file=firmware_file_name),
                                        dst_file=dst_file)
            else:
                raise Exception(
                    "Unsupported protocol. "
                    "Updating firmware possible from tftp, ftp or local storage({}) only".format(self.FILE_SYSTEM))

            firmware_actions.update_firmware(firmware_file=dst_file)
            system_actions.reboot()

            if firmware_file_name not in system_actions.display_running_config(boot=""):
                raise Exception("Can't add firmware '{}' for boot!".format(firmware_file_name))
            if firmware_file_name not in system_actions.display_os_version():
                raise Exception("Failed to load firmware, Please check logs")
