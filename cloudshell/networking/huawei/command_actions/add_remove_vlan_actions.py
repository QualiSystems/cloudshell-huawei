#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor
from cloudshell.networking.huawei.command_templates import add_remove_vlan


class AddRemoveVlanActions(object):
    SESSION_RECONNECT_TIMEOUT = 300

    def __init__(self, cli_service, logger):
        """ Add/Remove VLAN(s) actions """

        self._cli_service = cli_service
        self._logger = logger

    def create_vlan(self, vlan):
        """ Create VLAN """

        CommandTemplateExecutor(self._cli_service, add_remove_vlan.CONFIGURE_VLAN).execute_command(vlan=vlan)

    def create_vlan_range(self, start_vlan, end_vlan):
        """ Create VLAN range """

        CommandTemplateExecutor(self._cli_service,
                                add_remove_vlan.CONFIGURE_VLAN_RANGE).execute_command(start_vlan=start_vlan,
                                                                                      end_vlan=end_vlan)

    def set_vlan_to_interface(self, vlan, port_mode, qnq):
        """  """

        if qnq:
            CommandTemplateExecutor(self._cli_service, add_remove_vlan.QNQ).execute_command()
            CommandTemplateExecutor(self._cli_service, add_remove_vlan.PORT_DEFAULT_VLAN).execute_command(vlan=vlan)
        elif port_mode == "trunk":
            CommandTemplateExecutor(self._cli_service,
                                    add_remove_vlan.ALLOW_TRUNK_VLAN).execute_command(vlan=vlan)
        elif port_mode == "access":
            CommandTemplateExecutor(self._cli_service, add_remove_vlan.PORT_MODE_ACCESS).execute_command()
            CommandTemplateExecutor(self._cli_service, add_remove_vlan.PORT_DEFAULT_VLAN).execute_command(vlan=vlan)

    def set_vlan_range_to_interface(self, start_vlan, end_vlan, port_mode):
        """  """

        if port_mode == "trunk":
            CommandTemplateExecutor(self._cli_service,
                                    add_remove_vlan.ALLOW_TRUNK_VLAN_RANGE).execute_command(start_vlan=start_vlan,
                                                                                            end_vlan=end_vlan)

    def configure_interface(self, port_name):
        """ Activate interface configuration mode """

        CommandTemplateExecutor(self._cli_service,
                                add_remove_vlan.CONFIGURE_INTERFACE).execute_command(port_name=port_name)

    def activate_port(self):
        """ Activate interface configuration mode """

        CommandTemplateExecutor(self._cli_service, add_remove_vlan.UNDO_SHUTDOWN).execute_command()

    def activate_port_mode(self):
        """  """

        CommandTemplateExecutor(self._cli_service, add_remove_vlan.START_PORT_MODE).execute_command()

    def get_port_name(self, port):
        """ Get port name from port resource full address """

        if not port:
            err_msg = "Failed to determine port name. Initial port: {}".format(port)
            self._logger.error(err_msg)
            raise Exception("HuaweiConnectivityOperations: get_port_name", err_msg)

        port_name = port.split("/")[-1]
        if "port-channel" not in port_name.lower():
            port_name = port_name.replace("-", "/")

        self._logger.info("Interface name validation OK, portname = {}".format(port_name))
        return port_name
