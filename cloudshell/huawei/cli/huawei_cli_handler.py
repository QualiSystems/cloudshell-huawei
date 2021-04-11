#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.configurator import AbstractModeConfigurator
from cloudshell.cli.service.cli import CLI
from cloudshell.cli.service.cli_service_impl import CliServiceImpl
from cloudshell.cli.service.command_mode_helper import CommandModeHelper
from cloudshell.cli.service.session_pool_manager import SessionPoolManager
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.session.telnet_session import TelnetSession

from cloudshell.huawei.cli.huawei_command_modes import (
    ConfigCommandMode,
    EnableCommandMode,
)


class HuaweiCli(object):
    def __init__(self, resource_config):
        session_pool_size = int(resource_config.sessions_concurrency_limit)
        session_pool = SessionPoolManager(max_pool_size=session_pool_size)
        self.cli = CLI(session_pool=session_pool)

    def get_cli_handler(self, resource_config, logger):
        return HuaweiCliHandler(self.cli, resource_config, logger)


class HuaweiSSHSession(SSHSession):
    def _connect_actions(self, prompt, logger):
        """Open connection to device/create session."""
        action_map = {
            r"The password needs to be changed. "
            r"Change now\? \[Y\/N\]:": lambda session, logger: session.send_line(
                "N", logger
            )
        }
        cmd = None
        self.hardware_expect(
            cmd,
            expected_string=prompt,
            timeout=self._timeout,
            logger=logger,
            action_map=action_map,
        )
        self._on_session_start(logger)


class HuaweiCliHandler(AbstractModeConfigurator):
    REGISTERED_SESSIONS = (
        HuaweiSSHSession,
        TelnetSession,
    )

    def __init__(self, cli, resource_config, logger):
        super(HuaweiCliHandler, self).__init__(resource_config, logger, cli)
        self.modes = CommandModeHelper.create_command_mode(resource_config)

    @property
    def default_mode(self):
        return self.modes[EnableCommandMode]

    @property
    def enable_mode(self):
        return self.modes[EnableCommandMode]

    @property
    def config_mode(self):
        return self.modes[ConfigCommandMode]

    def _on_session_start(self, session, logger):
        """Send default commands to configure/clear session outputs."""
        cli_service = CliServiceImpl(
            session=session, requested_command_mode=self.enable_mode, logger=logger
        )
        cli_service.send_command("screen-length 0 temporary", EnableCommandMode.PROMPT)
