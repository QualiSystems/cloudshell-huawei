#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.huawei.command_templates import system
from cloudshell.huawei.helpers.exceptions import HuaweiBaseException


class SystemActions(object):
    SESSION_RECONNECT_TIMEOUT = 300

    def __init__(self, cli_service, logger):
        """General System actions."""
        self._cli_service = cli_service
        self._logger = logger

    def commit(self):
        """Commit changes."""
        CommandTemplateExecutor(self._cli_service, system.COMMIT).execute_command()

    def display_os_version(self):
        """Get OS version."""
        return CommandTemplateExecutor(
            self._cli_service, system.DISPLAY_VERSION
        ).execute_command()

    def display_running_config(self, port_name=None, boot=None):
        """Get running configuration."""
        if port_name is not None:
            # display configuration for specific interface
            return CommandTemplateExecutor(
                self._cli_service, system.DISPLAY_RUNNING
            ).execute_command(port_name=port_name)
        elif boot is not None:
            # display boot configuration
            return CommandTemplateExecutor(
                self._cli_service, system.DISPLAY_RUNNING
            ).execute_command(boot=boot)
        else:
            # display full configuration
            return CommandTemplateExecutor(
                self._cli_service, system.DISPLAY_RUNNING
            ).execute_command()

    def display_startup_config(self):
        """Get startup configuration filename."""
        startup_config = CommandTemplateExecutor(
            self._cli_service, system.DISPLAY_STARTUP
        ).execute_command()
        match = re.search(
            r"Next startup saved-configuration file:(?P<startup>.*)",
            startup_config,
            re.IGNORECASE,
        )

        if not match:
            self._logger.error(
                "Can not determine startup configuration file location at : {}".format(
                    startup_config
                )
            )
            raise HuaweiBaseException(
                "Can not determine startup configuration file location"
            )
        else:
            return match.groupdict().get("startup")

    def clean_current_configuration_on_interface(
        self, configuration, action_map=None, error_map=None
    ):
        """Clean configuration on interface."""
        action_map.update(
            {
                r"[\[\(][Yy]es/[Nn]o[\)\]]|\[Continue\]|Continue?\[Y/N\]": lambda session: session.send_line(  # noqa: E501
                    "yes"
                ),
                r"[\[\(][Yy]/[Nn][\)\]]": lambda session: session.send_line("y"),
            }
        )

        for line in configuration.splitlines():
            line = line.strip()
            if re.search(
                r"^port default vlan\s+|"
                r"^port link-type\s+|"
                r"^port trunk allow-pass vlan\s+",
                line,
            ):
                if not re.search(r"^port trunk allow-pass vlan\s+", line):
                    line = re.sub(r"\s+\d+[-\d+,]*|trunk|access", "", line)

                CommandTemplateExecutor(
                    self._cli_service,
                    system.UNDO,
                    action_map=action_map,
                    error_map=error_map,
                ).execute_command(command=line)

    def reboot(self, action_map=None, error_map=None):
        """Reboot the system."""
        try:
            CommandTemplateExecutor(
                cli_service=self._cli_service,
                command_template=system.REBOOT,
                action_map=action_map,
                error_map=error_map,
                expected_string="System is rebooting, please wait",
            ).execute_command()
        except Exception:
            self._logger.info(
                "Session type is '{}', closing session...".format(
                    self._cli_service.session.session_type
                )
            )

        if self._cli_service.session.session_type.lower() != "console":
            self._cli_service.reconnect(timeout=self.SESSION_RECONNECT_TIMEOUT)
