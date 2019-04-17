#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template import CommandTemplate


ACTIVATE_SNMP = CommandTemplate("snmp-agent")
DEACTIVATE_SNMP = CommandTemplate("undo snmp-agent")
CONFIGURE_SNMP_VERSION = CommandTemplate("snmp-agent sys-info version {snmp_version}")
CONFIGURE_V2C_COMMUNITY = CommandTemplate("snmp-agent community read {community}")
REMOVE_V2C_COMMUNITY = CommandTemplate("undo snmp-agent community {community}")

CONFIGURE_V3_VIEW = CommandTemplate("snmp-agent mib-view included {view_name} 1")
CONFIGURE_V3_GROUP = CommandTemplate("snmp-agent group v3 {group_name} {auth_type} {snmp_access}-view {view_name}")
CONFIGURE_V3_USER = CommandTemplate("snmp-agent usm-user v3 {user_name}")
CONFIGURE_V3_AUTH = CommandTemplate("snmp-agent usm-user v3 {user_name} authentication-mode {auth_protocol}") # md5 | sha
CONFIGURE_V3_PRIV = CommandTemplate("snmp-agent usm-user v3 {user_name} privacy-mode {priv_protocol}") # des56 | aes128 |aes192 | aes256 | 3des

REMOVE_V3_USER = CommandTemplate("undo snmp-agent usm-user v3 {user_name}")
