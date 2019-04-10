#!/usr/bin/python
# -*- coding: utf-8 -*-


from cloudshell.cli.cli_service_impl import CliServiceImpl
from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.session.telnet_session import TelnetSession
from cloudshell.devices.cli_handler_impl import CliHandlerImpl

from cloudshell.networking.huawei.cli.huawei_command_modes import EnableCommandMode, ConfigCommandMode


class HuaweiCliHandler(CliHandlerImpl):
    def __init__(self, cli, resource_config, logger, api):
        super(HuaweiCliHandler, self).__init__(cli, resource_config, logger, api)
        self.modes = CommandModeHelper.create_command_mode(resource_config, api)

    @property
    def default_mode(self):
        return self.modes[EnableCommandMode]

    @property
    def enable_mode(self):
        return self.modes[EnableCommandMode]

    @property
    def config_mode(self):
        return self.modes[ConfigCommandMode]

    def _new_sessions(self):
        if self.cli_type.lower() == SSHSession.SESSION_TYPE.lower():
            new_sessions = self._ssh_session()
        elif self.cli_type.lower() == TelnetSession.SESSION_TYPE.lower():
            new_sessions = self._telnet_session()
        else:
            new_sessions = [self._ssh_session(), self._telnet_session()]

        return new_sessions

    def on_session_start(self, session, logger):
        """Send default commands to configure/clear session outputs
        :param SSHSession|TelnetSession session:
        :param Logger logger:
        """

        cli_service = CliServiceImpl(session, self.enable_mode, logger)
        # cli_service.send_command("set cli config-output-format set")
        # cli_service.send_command("set cli pager off")
        # cli_service.send_command("set cli terminal width 300")
        cli_service.send_command("screen-length 0 temporary")
        # cli_service.send_command("screen-width 300")
