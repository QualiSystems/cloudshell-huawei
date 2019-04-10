# !/usr/bin/python
# -*- coding: utf-8 -*-

from re import escape
from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate

COPY = CommandTemplate("copy {src} {dst}",
                       action_map=OrderedDict({
                           r"\[confirm\]": lambda session, logger: session.send_line("", logger),
                           r"\[Y/N\]": lambda session, logger: session.send_line("y", logger),
                           r"[Oo]verwrit+e": lambda session, logger: session.send_line("y", logger),
                           "\(Y/N\)": lambda session, logger: session.send_line("y", logger)}))

TFTP_GET = CommandTemplate("tftp {host} get {src} {dst}", action_map=OrderedDict({
    "\[Y/N\]": lambda session, logger: session.send_line("y", logger),
    "\(Y/N\)": lambda session, logger: session.send_line("y", logger),
    r"[Oo]verwrit+e": lambda session, logger: session.send_line("y", logger)}))

TFTP_PUT = CommandTemplate("tftp {host} put {src} {dst}", action_map=OrderedDict({
    "\[Y/N\]": lambda session, logger: session.send_line("y", logger),
    "\(Y/N\)": lambda session, logger: session.send_line("y", logger),
    r"[Oo]verwrit+e": lambda session, logger: session.send_line("y", logger)}))

SAVE_RUNNING = CommandTemplate("save {dst_file}",
                               action_map=OrderedDict({
                                   r"\[Y/N\]": lambda session, logger: session.send_line("Y", logger),
                                   r"[Oo]verwrit+e": lambda session, logger: session.send_line("y", logger),
                                   "\(Y/N\)": lambda session, logger: session.send_line("Y", logger)}))

SAVE_STARTUP = CommandTemplate("startup saved-configuration {dst}",
                               action_map=OrderedDict({
                                   r"\[confirm\]": lambda session, logger: session.send_line("", logger),
                                   r"\[Y/N\]": lambda session, logger: session.send_line("y", logger),
                                   r"[Oo]verwrit+e": lambda session, logger: session.send_line("y", logger),
                                   "\(Y/N\)": lambda session, logger: session.send_line("y", logger)}))
