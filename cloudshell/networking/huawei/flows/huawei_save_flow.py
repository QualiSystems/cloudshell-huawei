#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.networking_utils import UrlParser

from cloudshell.devices.flows.action_flows import SaveConfigurationFlow
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions
from cloudshell.networking.huawei.command_actions.save_restore_actions import SaveRestoreActions


class HuaweiSaveFlow(SaveConfigurationFlow):
    def __init__(self, cli_handler, logger, file_system):
        super(HuaweiSaveFlow, self).__init__(cli_handler, logger)
        self.file_system = file_system

    def execute_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """ Execute flow which save selected file to the provided destination

        :param folder_path: destination path where file will be saved
        :param configuration_type: source file, which will be saved
        :param vrf_management_name: Virtual Routing and Forwarding Name
        :return: saved configuration file name
        """

        if not configuration_type:
            configuration_type = "running-config"
        elif "-config" not in configuration_type:
            configuration_type = configuration_type.lower() + "-config"

        if configuration_type not in ["running-config", "startup-config"]:
            raise Exception(self.__class__.__name__,
                            "Device doesn't support saving '{}' configuration type".format(configuration_type))

        url = UrlParser().parse_url(folder_path)

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            save_action = SaveRestoreActions(enable_session, self._logger)

            if configuration_type == "running-config":
                # src_file = "{file_system}:/qualirunconfig.cfg".format(file_system=self.file_system)
                src_file = "quali_run_config.cfg"
                save_action.save_runninig_config(dst_file=src_file)
            else:
                startup_config = system_action.display_startup_config()
                src_file = save_action.get_startup_config_filename(startup_config=startup_config)

            scheme = url.get(UrlParser.SCHEME).lower()

            if (not scheme or scheme == self.file_system) and src_file != folder_path:
                save_action.copy_file(src_file=src_file, dst_file=folder_path)
            elif scheme in ["ftp", "tftp"]:
                save_action.put_file(server_address=url.get(UrlParser.HOSTNAME),
                                     src_file=src_file,
                                     dst_file=url.get(UrlParser.FILENAME))
            else:
                raise Exception("Unsupported backup protocol {scheme}. "
                                "Supported types are ftp, tftp of local({file_system})".format(scheme=scheme,
                                                                                               file_system=self.file_system))
