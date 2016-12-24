from collections import OrderedDict
from cloudshell.cli.command_template.command_template import CommandTemplate

COPY = CommandTemplate('copy {src} {dst}',
                       action_map=OrderedDict({
                           r'\[confirm\]': lambda session, logger: session.send_line('', logger),
                           r'\[Y/N\]': lambda session, logger: session.send_line('y', logger),
                           r'[Oo]verwrit+e': lambda session, logger: session.send_line('y', logger),
                           '\(Y/N\)': lambda session, logger: session.send_line('yes', logger)}))


SNMP_ENABLE = CommandTemplate("snmp-agent")
SNMP_DISABLE = CommandTemplate("undo snmp-agent")


DISPLAY_CONFIG = CommandTemplate(
    'display current-configuration [interface {port_name}] [ | include boot{boot}] [ | include snmp-server community{snmp}]')

DISPLAY_VERSION = CommandTemplate('display version')

UPDATE_FIRMWARE = CommandTemplate('startup system-software {firmware file}')
