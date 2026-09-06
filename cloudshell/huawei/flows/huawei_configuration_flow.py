#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.shell.flows.configuration.basic_flow import (
    AbstractConfigurationFlow,
    ConfigurationType,
    RestoreMethod,
)
from cloudshell.shell.flows.utils.url import RemoteURL

from cloudshell.huawei.command_actions.save_restore_actions import SaveRestoreActions
from cloudshell.huawei.command_actions.system_actions import SystemActions
from cloudshell.huawei.helpers.exceptions import HuaweiSaveRestoreException


class HuaweiConfigurationFlow(AbstractConfigurationFlow):
    SUPPORTED_RESTORE_METHODS = {RestoreMethod.OVERRIDE}

    def __init__(self, cli_handler, resource_config, logger):
        super().__init__(logger, resource_config)
        self._cli_handler = cli_handler

    @property
    def file_system(self):
        """Determine device file system type."""
        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            startup_config_filename = system_action.display_startup_config()

            return startup_config_filename.split(":")[0]

    def _save_flow(self, file_dst_url, configuration_type, vrf_management_name=None):
        """Execute flow which save selected file to the provided destination.

        :param file_dst_url: destination URL where file will be saved
        :param configuration_type: source file, which will be saved
        :param vrf_management_name: Virtual Routing and Forwarding Name
        :return: saved configuration file name
        """
        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            save_action = SaveRestoreActions(enable_session, self._logger)

            if configuration_type == ConfigurationType.RUNNING:
                src_file = "quali_run_config.cfg"
                save_action.save_runninig_config(dst_file=src_file)
            else:
                src_file = system_action.display_startup_config()

            scheme = file_dst_url.scheme.lower().rstrip(":/")

            if isinstance(file_dst_url, RemoteURL):
                if scheme not in ["ftp", "tftp"]:
                    raise HuaweiSaveRestoreException(
                        "Unsupported backup protocol {scheme}. "
                        "Supported types are ftp, tftp or "
                        "local({file_system})".format(
                            scheme=scheme, file_system=self.file_system
                        )
                    )
                save_action.put_file(
                    server_address=file_dst_url.host,
                    src_file=src_file,
                    dst_file=file_dst_url.filename,
                )
            else:
                dst_file = file_dst_url.url
                if src_file != dst_file:
                    save_action.copy_file(src_file=src_file, dst_file=dst_file)

    def _restore_flow(
        self, config_path, configuration_type, restore_method, vrf_management_name
    ):
        """Execute flow which restores selected file to the provided destination.

        :param config_path: the URL of the configuration file, including the
            configuration file name
        :param restore_method: the restore method to use when restoring the
            configuration file. Possible Values are append and override
        :param configuration_type: the configuration type to restore.
            Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """
        if restore_method != RestoreMethod.OVERRIDE:
            raise HuaweiSaveRestoreException(
                "Huawei do no yet support append operations on configuration files"
            )

        with self._cli_handler.get_cli_service(
            self._cli_handler.enable_mode
        ) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            restore_action = SaveRestoreActions(enable_session, self._logger)

            if isinstance(config_path, RemoteURL):
                scheme = config_path.scheme.lower()
                if scheme not in ["ftp", "tftp"]:
                    raise HuaweiSaveRestoreException(
                        "Unsupported restore protocol {scheme}. "
                        "Supported types are ftp, tftp or "
                        "local({file_system})".format(
                            scheme=scheme, file_system=self.file_system
                        )
                    )
                dst_file = "{file_system}:/{file_name}".format(
                    file_system=self.file_system, file_name=config_path.filename
                )
                restore_action.get_file(
                    server_address=config_path.host,
                    src_file=config_path.path.lstrip("/"),
                    dst_file=dst_file,
                )
                restore_action.setup_startup_config(dst_file)
            else:
                restore_action.setup_startup_config(config_path.url)

            if configuration_type == ConfigurationType.RUNNING:
                system_action.reboot()
