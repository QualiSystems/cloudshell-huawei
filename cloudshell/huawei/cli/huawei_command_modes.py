#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.service.command_mode import CommandMode


class EnableCommandMode(CommandMode):
    PROMPT = r"<.*?>"
    ENTER_COMMAND = ""
    EXIT_COMMAND = "quit"

    def __init__(self, resource_config):
        """Initialize Enable command mode."""
        self.resource_config = resource_config

        super(EnableCommandMode, self).__init__(
            prompt=self.PROMPT,
            enter_command=self.ENTER_COMMAND,
            exit_command=self.EXIT_COMMAND,
        )


class ConfigCommandMode(CommandMode):
    PROMPT = r"\[.*?\]"
    ENTER_COMMAND = "system-view"
    EXIT_COMMAND = "quit"

    def __init__(self, resource_config):
        """Initialize Config command mode."""
        self.resource_config = resource_config

        super(ConfigCommandMode, self).__init__(
            prompt=self.PROMPT,
            enter_command=self.ENTER_COMMAND,
            exit_command=self.EXIT_COMMAND,
            enter_action_map={
                r"Error: Incomplete command found at '\^' position.": lambda session, logger: session.send_line(  # noqa: E501,E800
                    "system-view immediately", logger
                )
            },
        )


CommandMode.RELATIONS_DICT = {EnableCommandMode: {ConfigCommandMode: {}}}
