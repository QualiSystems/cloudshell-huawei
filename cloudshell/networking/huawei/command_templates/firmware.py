# !/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict
from cloudshell.cli.command_template.command_template import CommandTemplate

STARTUP_SYSTEM_SOFTWARE = CommandTemplate("startup system-software {dst_file}",
                                          action_map=OrderedDict({"Continue\?\[Y/N\]": lambda session, logger: session.send_line("y", logger)}))

