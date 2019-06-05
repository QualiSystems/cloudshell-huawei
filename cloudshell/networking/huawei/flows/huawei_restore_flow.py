#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.action_flows import RestoreConfigurationFlow
from cloudshell.devices.networking_utils import UrlParser
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions
from cloudshell.networking.huawei.command_actions.save_restore_actions import SaveRestoreActions


class HuaweiRestoreFlow(RestoreConfigurationFlow):

    def __init__(self, cli_handler, logger, file_system):
        super(HuaweiRestoreFlow, self).__init__(cli_handler, logger)
        self.file_system = file_system

    def execute_flow(self, path, configuration_type, restore_method, vrf_management_name=None):
        """ Execute flow which save selected file to the provided destination

        :param path: the path to the configuration file, including the configuration file name
        :param restore_method: the restore method to use when restoring the configuration file.
                               Possible Values are append and override
        :param configuration_type: the configuration type to restore. Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """

        if not configuration_type:
            configuration_type = "running-config"
        elif "-config" not in configuration_type:
            configuration_type = configuration_type.lower() + "-config"

        if configuration_type not in ["running-config", "startup-config"]:
            raise Exception(self.__class__.__name__,
                            "Device doesn't support restoring '{}' configuration type".format(configuration_type))

        if not restore_method:
            restore_method = "override"

        url = UrlParser().parse_url(path)

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            restore_action = SaveRestoreActions(enable_session, self._logger)

            if restore_method == "override":
                dst_file = "{file_system}:/{file_name}".format(file_system=self.file_system,
                                                               file_name=url.get(UrlParser.FILENAME))

                scheme = url.get(UrlParser.SCHEME).lower()
                if not scheme or scheme == self.file_system:
                    restore_action.setup_startup_config(path)
                elif scheme in ["ftp", "tftp"]:
                    restore_action.get_file(server_address=url.get(UrlParser.HOSTNAME),
                                            src_file="{path}/{file}".format(path=url.get(UrlParser.PATH).rstrip("/"),
                                                                            file=url.get(UrlParser.FILENAME)),
                                            dst_file=dst_file)
                    restore_action.setup_startup_config(dst_file)

                if configuration_type == "running-config":
                    system_action.reboot()

            else:
                raise Exception("Huawei do no yet support append operations on configuration files")
