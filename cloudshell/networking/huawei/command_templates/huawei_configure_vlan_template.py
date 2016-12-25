from collections import OrderedDict
from cloudshell.cli.command_template.command_template import CommandTemplate


CONFIGURE_INTERFACE = CommandTemplate('interface {port_name}')

CONFIGURE_VLAN = CommandTemplate('vlan {vlan_id}',
                                 error_map=OrderedDict({"Error:": Exception('CONFIGURE_VLAN', "Error")}))

SHUTDOWN = CommandTemplate('shutdown')

UNDO_SHUTDOWN = CommandTemplate('undo shutdown')

UNDO = CommandTemplate('undo {command}')

IP_ADDRESS = CommandTemplate('ip address {0}')


DISPLAY_RUNNING = CommandTemplate('display current-configuration [interface {port_name}]')

DISPLAY_VERSION = CommandTemplate('display version')

VLAN_BATCH = CommandTemplate('vlan batch {vlan_id}')

ALLOW_TRUNK_VLAN = CommandTemplate('port trunk allow-pass vlan {vlan_id}')

NO_TRUNK = CommandTemplate('undo port trunk allow-pass vlan {vlan_id}')

START_PORT_MODE = CommandTemplate('portswitch')

PORT_MODE_TRUNK = CommandTemplate('port link-type trunk')

PORT_MODE_ACCESS = CommandTemplate('port link-type access')

QNQ = CommandTemplate('port link-type dot1q-tunnel')

PORT_DEFAULT_VLAN = CommandTemplate('port default vlan {vlan_id}')

SPEED = CommandTemplate('speed')

COMMIT = CommandTemplate('commit')

