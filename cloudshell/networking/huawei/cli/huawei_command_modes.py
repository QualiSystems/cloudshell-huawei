#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_mode import CommandMode


# class DefaultCommandMode(CommandMode):
#     PROMPT = '(.*?)'
#     ENTER_COMMAND = ''
#     EXIT_COMMAND = 'quit'
#
#     def __init__(self, resource_config, api):
#         """ Initialize Default command mode, only for cases when session started not in enable mode """
#
#         self.resource_config = resource_config
#         self._api = api
#
#         super(DefaultCommandMode, self).__init__(prompt=self.PROMPT,
#                                                  enter_command=self.ENTER_COMMAND,
#                                                  exit_command=self.EXIT_COMMAND)


class EnableCommandMode(CommandMode):
    PROMPT = r'<.*?>'
    ENTER_COMMAND = ''  # system-view
    EXIT_COMMAND = 'quit'

    def __init__(self, resource_config, api):
        """ Initialize Enable command mode - super command mode for Huawei """

        self.resource_config = resource_config
        self._api = api

        super(EnableCommandMode, self).__init__(prompt=self.PROMPT,
                                                enter_command=self.ENTER_COMMAND,
                                                exit_command=self.EXIT_COMMAND)


class ConfigCommandMode(CommandMode):
    PROMPT = r'\[.*?\]'
    ENTER_COMMAND = 'sys'
    EXIT_COMMAND = 'quit'

    def __init__(self, resource_config, api):
        """ Initialize Config command mode """

        self.resource_config = resource_config
        self._api = api

        super(ConfigCommandMode, self).__init__(prompt=self.PROMPT,
                                                enter_command=self.ENTER_COMMAND,
                                                exit_command=self.EXIT_COMMAND)


CommandMode.RELATIONS_DICT = {
    # DefaultCommandMode: {
        EnableCommandMode: {
            ConfigCommandMode: {}
        }
    # }
}
