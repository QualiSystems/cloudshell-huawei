from collections import OrderedDict
from cloudshell.cli.command_template.command_template import CommandTemplate

# <editor-fold desc="Interface configuration templates">

CONFIGURE_INTERFACE = CommandTemplate('interface {port_name}')

SWITCHPORT_MODE = CommandTemplate('switchport[ mode {port_mode}]',
                                  action_map=OrderedDict(
                                      {'[\[\(][Yy]es/[Nn]o[\)\]]|\[confirm\]': lambda session: session.send_line('yes'),
                                       '[\[\(][Yy]/[Nn][\)\]]': lambda session: session.send_line('y')}),
                                  error_map=OrderedDict({
                                      "[Ii]nvalid\s*([Ii]nput|[Cc]ommand)|[Cc]ommand rejected":
                                          Exception('SWITCHPORT_MODE', 'Failed to switch port mode'),
                                  }))

SWITCHPORT_ALLOW_VLAN = CommandTemplate(
    'switchport [trunk allowed{port_mode_trunk}] [access{port_mode_access}] vlan {vlan_range}',
    action_map=OrderedDict(
        {'[\[\(][Yy]es/[Nn]o[\)\]]|\[confirm\]': lambda session: session.send_line('yes'),
         '[\[\(][Yy]/[Nn][\)\]]': lambda session: session.send_line('y')}),
    error_map=OrderedDict({
        "[Ii]nvalid\s*([Ii]nput|[Cc]ommand)|[Cc]ommand rejected": Exception('SWITCHPORT_MODE',
                                                                            'Failed to switch port mode')}))

# </editor-fold>

# <editor-fold desc="Vlan configuration templates">

CONFIGURE_VLAN = CommandTemplate('vlan {vlan_id}',
                                 error_map=OrderedDict({"%.*\.": Exception('CONFIGURE_VLAN', "Error")}))
STATE_ACTIVE = CommandTemplate('state active')

# </editor-fold>

SHUTDOWN = CommandTemplate('shutdown')

NO_SHUTDOWN = CommandTemplate('no shutdown')

NO = CommandTemplate('no {command}')

IP = CommandTemplate('ip {0}')

# <editor-fold desc="Show templates">

SHOW_RUNNING = CommandTemplate(
    'show running-config [interface {port_name}] [ | include boot{boot}] [ | include snmp-server community{snmp}]')

SHOW_VERSION = CommandTemplate('show version')

# </editor-fold>
