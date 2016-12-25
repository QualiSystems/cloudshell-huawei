from collections import OrderedDict
from cloudshell.cli.command_template.command_template import CommandTemplate

COPY = CommandTemplate('copy {src} {dst}',
                       action_map=OrderedDict({
                           r'\[confirm\]': lambda session, logger: session.send_line('', logger),
                           r'\[Y/N\]': lambda session, logger: session.send_line('y', logger),
                           r'[Oo]verwrit+e': lambda session, logger: session.send_line('y', logger),
                           '\(Y/N\)': lambda session, logger: session.send_line('y', logger)}))

TFTP_PUT = CommandTemplate('tftp {host} put {src} {dst}',action_map=OrderedDict({
                           '\[Y/N\]': lambda session, logger: session.send_line('y', logger),
                           '\(Y/N\)': lambda session, logger: session.send_line('y', logger),
                           r'[Oo]verwrit+e': lambda session, logger: session.send_line('y', logger)}))

TFTP_GET = CommandTemplate('tftp {host} get {src} {dst}',action_map=OrderedDict({
                           '\[Y/N\]': lambda session, logger: session.send_line('y', logger),
                           '\(Y/N\)': lambda session, logger: session.send_line('y', logger),
                           r'[Oo]verwrit+e': lambda session, logger: session.send_line('y', logger)}))

SNMP_ENABLE = CommandTemplate("snmp-agent")
SNMP_DISABLE = CommandTemplate("undo snmp-agent")


DISPLAY_CONFIG = CommandTemplate(
    'display current-configuration [interface {port_name}] [ | include boot{boot}] [ | include snmp-server community{snmp}]')

DISPLAY_VERSION = CommandTemplate('display version')

DISPLAY_STARTUP = CommandTemplate('display startup')

UPDATE_FIRMWARE = CommandTemplate('startup system-software {firmware file}')

PWD = CommandTemplate('pwd')

REBOOT = CommandTemplate('reboot fast',action_map=OrderedDict({'Continue\?\[Y/N\]': lambda session,logger:
    session.send_line('y', logger)}))

STARTUP_SYSTEM_SOFTWARE = CommandTemplate('startup system-software {dst_file}',
                                          action_map=OrderedDict({'Continue\?\[Y/N\]':lambda session,logger: session.send_line('y',logger)}))
