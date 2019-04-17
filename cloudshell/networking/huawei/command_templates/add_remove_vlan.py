# !/usr/bin/python
# -*- coding: utf-8 -*-

from re import escape
from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate


CONFIGURE_INTERFACE = CommandTemplate("interface {port_name}")


UNDO_SHUTDOWN = CommandTemplate("undo shutdown")
START_PORT_MODE = CommandTemplate("portswitch")

CONFIGURE_VLAN = CommandTemplate("vlan {vlan}",
                                 error_map=OrderedDict({"Error:": Exception("CONFIGURE_VLAN", "Error")}))

CONFIGURE_VLAN_RANGE = CommandTemplate("vlan batch {start_vlan} to {end_vlan}")

ALLOW_TRUNK_VLAN = CommandTemplate("port trunk allow-pass vlan {vlan}")
ALLOW_TRUNK_VLAN_RANGE = CommandTemplate("port trunk allow-pass vlan {start_vlan} to {end_vlan}")

PORT_MODE_ACCESS = CommandTemplate("port link-type access")


QNQ = CommandTemplate("port link-type dot1q-tunnel")
PORT_DEFAULT_VLAN = CommandTemplate("port default vlan {vlan}")
