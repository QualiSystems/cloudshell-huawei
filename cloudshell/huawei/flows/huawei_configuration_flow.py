#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.configuration.basic_flow import AbstractConfigurationFlow
from cloudshell.shell.flows.utils.networking_utils import UrlParser

from cloudshell.huawei.command_actions.save_restore_actions import SaveRestoreActions
from cloudshell.huawei.command_actions.system_actions import SystemActions
from cloudshell.huawei.helpers.exceptions import HuaweiSaveRestoreException


class HuaweiConfigurationFlow(AbstractConfigurationFlow):
    def __init__(self, cli_handler, resource_config, logger):
        super(HuaweiConfigurationFlow, self).__init__(logger, resource_config)
        self._cli_handler = cli_handler

    @property
    def _file_system(self):
        """Determine device file system type."""
        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            startup_config_filename = system_action.display_startup_config()

            return startup_config_filename.split(":")[0]

    def _save_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """Execute flow which save selected file to the provided destination.

        :param folder_path: destination path where file will be saved
        :param configuration_type: source file, which will be saved
        :param vrf_management_name: Virtual Routing and Forwarding Name
        :return: saved configuration file name
        """
        if not configuration_type.endswith("-config"):
            configuration_type += "-config"

        if configuration_type not in ["running-config", "startup-config"]:
            raise HuaweiSaveRestoreException(
                "Device doesn't support saving '{}' configuration type".format(
                    configuration_type
                ),
            )

        url = UrlParser().parse_url(folder_path)

        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            save_action = SaveRestoreActions(enable_session, self._logger)

            if configuration_type == "running-config":
                src_file = "quali_run_config.cfg"
                save_action.save_runninig_config(dst_file=src_file)
            else:
                src_file = system_action.display_startup_config()

            scheme = url.get(UrlParser.SCHEME).lower()

            if (not scheme or scheme == self.file_system) and src_file != folder_path:
                save_action.copy_file(src_file=src_file, dst_file=folder_path)
            elif scheme in ["ftp", "tftp"]:
                save_action.put_file(
                    server_address=url.get(UrlParser.HOSTNAME),
                    src_file=src_file,
                    dst_file=url.get(UrlParser.FILENAME),
                )
            else:
                raise HuaweiSaveRestoreException(
                    "Unsupported backup protocol {scheme}. "
                    "Supported types are ftp, tftp of local({file_system})".format(
                        scheme=scheme, file_system=self.file_system
                    )
                )

    def _restore_flow(
        self, path, configuration_type, restore_method, vrf_management_name
    ):
        """Execute flow which save selected file to the provided destination.

        :param path: the path to the configuration file, including the configuration
            file name
        :param restore_method: the restore method to use when restoring the
            configuration file. Possible Values are append and override
        :param configuration_type: the configuration type to restore.
            Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """
        if not configuration_type:
            configuration_type = "running-config"
        elif "-config" not in configuration_type:
            configuration_type = configuration_type.lower() + "-config"

        if configuration_type not in ["running-config", "startup-config"]:
            raise HuaweiSaveRestoreException(
                "Device doesn't support restoring '{}' configuration type".format(
                    configuration_type
                )
            )

        if not restore_method:
            restore_method = "override"

        url = UrlParser().parse_url(path)

        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            restore_action = SaveRestoreActions(enable_session, self._logger)

            if restore_method == "override":
                dst_file = "{file_system}:/{file_name}".format(
                    file_system=self.file_system, file_name=url.get(UrlParser.FILENAME)
                )

                scheme = url.get(UrlParser.SCHEME).lower()
                if not scheme or scheme == self.file_system:
                    restore_action.setup_startup_config(path)
                elif scheme in ["ftp", "tftp"]:
                    restore_action.get_file(
                        server_address=url.get(UrlParser.HOSTNAME),
                        src_file="{path}/{file}".format(
                            path=url.get(UrlParser.PATH).rstrip("/"),
                            file=url.get(UrlParser.FILENAME),
                        ),
                        dst_file=dst_file,
                    )
                    restore_action.setup_startup_config(dst_file)

                if configuration_type == "running-config":
                    system_action.reboot()

            else:
                raise HuaweiSaveRestoreException(
                    "Huawei do no yet support append operations on configuration files"
                )
