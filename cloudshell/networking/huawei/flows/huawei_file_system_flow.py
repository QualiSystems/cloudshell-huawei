#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.action_flows import BaseFlow
from cloudshell.networking.huawei.command_actions.system_actions import SystemActions
from cloudshell.networking.huawei.command_actions.save_restore_actions import SaveRestoreActions


class HuaweiFileSystemFlow(BaseFlow):
    def __init__(self, cli_handler, logger):
        super(HuaweiFileSystemFlow, self).__init__(cli_handler, logger)

    def execute_flow(self):
        """ Execute flow which determine file system """

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            system_action = SystemActions(enable_session, self._logger)
            save_action = SaveRestoreActions(enable_session, self._logger)
            startup_config = system_action.display_startup_config()

            src_file = save_action.get_startup_config_filename(startup_config=startup_config)

            return src_file.split(":")[0]
