#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import re
from cloudshell.networking.huawei.huawei_command_actions import restore_configuration
from cloudshell.networking.devices.flows.action_flows import RestoreConfigurationFlow


class HuaweiRestoreFlow(RestoreConfigurationFlow):
    STARTUP_LOCATION = "nvram:startup_config"

    def __init__(self, cli_handler, logger):
        super(HuaweiRestoreFlow, self).__init__(cli_handler, logger)

    def execute_flow(self, path, configuration_type, restore_method, vrf_management_name):
        """ Execute flow which save selected file to the provided destination

        :param path: the path to the configuration file, including the configuration file name
        :param restore_method: the restore method to use when restoring the configuration file.
                               Possible Values are append and override
        :param configuration_type: the configuration type to restore. Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            copy_action_map = self._prepare_action_map(path, configuration_type)
            if restore_method == "override":
                output = restore_configuration(session=enable_session, logger=self._logger,
                                  source_path=path, configuration_type=configuration_type,restore_method=restore_method,action_map=copy_action_map)

            else:
                raise Exception('huawei', "huawei do no yet support append operations on configuration files")
        return output


    def _prepare_action_map(self, source_file, destination_file):
        action_map = OrderedDict()
        host = None
        if "://" in source_file:
            source_file_data_list = re.sub("/+", "/", source_file).split("/")
            host = source_file_data_list[1]
            destination_file_name = destination_file.split("/")[-1]
            action_map[r"[\[\(]{}[\)\]]".format(
                source_file_data_list[-1])] = lambda session, logger: session.send_line("", logger)

            action_map[r"[\[\(]{}[\)\]]".format(destination_file_name)] = lambda session, logger: session.send_line("",
                                                                                                               logger)
        else:
            source_file_name = destination_file.split("/")[-1]
            destination_file_name = source_file.split("/")[-1]
            action_map[r"(?!/)[\[\(]{}[\)\]]".format(
                source_file_name)] = lambda session, logger: session.send_line("", logger)
            action_map[r"(?!/)[\[\(]{}[\)\]]".format(
                destination_file_name)] = lambda session, logger: session.send_line("", logger)
        if host:
            if "@" in host:
                storage_data = re.search(r"^(?P<user>\S+):(?P<password>\S+)@(?P<host>\S+)", host)
                if storage_data:
                    storage_data_dict = storage_data.groupdict()
                    host = storage_data_dict["host"]
                    password = storage_data_dict["password"]

                    action_map[r"[Pp]assword:".format(
                        source_file)] = lambda session, logger: session.send_line(password, logger)

                else:
                    host = host.split("@")[-1]
            action_map[r"(?!/){}(?!/)".format(host)] = lambda session, logger: session.send_line("", logger)
        return action_map
