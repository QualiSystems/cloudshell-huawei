# !/usr/bin/python
# -*- coding: utf-8 -*-

from re import escape
from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate

COMMIT = CommandTemplate("commit")

UNDO = CommandTemplate("undo {command}")

DISPLAY_VERSION = CommandTemplate("display version")

DISPLAY_RUNNING = CommandTemplate(
    "display current-configuration [interface {port_name}] [ | include boot{boot}] [ | include snmp-server community{snmp}]")

DISPLAY_STARTUP = CommandTemplate("display startup")

REBOOT = CommandTemplate("reboot fast",
                         action_map=OrderedDict({"Continue\?\[Y/N\]": lambda session, logger: session.send_line("y", logger)}))

STARTUP_SYSTEM_SOFTWARE = CommandTemplate("startup system-software {dst_file}",
                                          action_map=OrderedDict({"Continue\?\[Y/N\]": lambda session, logger: session.send_line("y", logger)}))
