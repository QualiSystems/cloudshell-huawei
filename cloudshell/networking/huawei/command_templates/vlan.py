from cloudshell.cli.command_template.command_template import CommandTemplate


from cloudshell.networking.networking_utils import validateIP, validateVlanRange


VLAN_COMMANDS_TEMPLATES = {
    'configure_interface': CommandTemplate('interface {0}',r'\w|0-9','Wrong interface name!'),
    'ip_address': CommandTemplate('ip address {0} {1}', [validateIP, validateIP],
                                  ['Wrong ip address!', 'Wrong ip mask!']),
    'configure_vlan': CommandTemplate('vlan {0}', validateVlanRange, 'Cannot create vlan - wrong vlan number(s)'),
    'quit': CommandTemplate('quit'),
    'hsrp': CommandTemplate('hsrp {0}', ['[0-9]+'],
                            ['Wrong router protocol id!']),
    'authentication': CommandTemplate('authentication {0}', [r'\w+'],
                                      ['Wrong authentication name!']),
    'undo shutdown': CommandTemplate('undo shutdown'),
    'vlan batch':CommandTemplate('vlan batch {0}',r'[0-9]+', 'Wrong vlan number!'),
    'allow_trunk_vlan': CommandTemplate('port trunk allow-pass vlan {0}', validateVlanRange,
                                        'Wrong allowed vlan id!'),
    'allow_trunk_vlan_ranges': CommandTemplate('port trunk allow-pass vlan {0}', r'[0-9]+',
                                        'Wrong allowed vlan id!'),
    'description': CommandTemplate('description'),
    'preempt': CommandTemplate('preempt'),
    'shutdown': CommandTemplate('shutdown'),
    'priority': CommandTemplate('priority {0}', ['[0-9]+'], ['Wrong priority number!']),
    'no trunk': CommandTemplate('undo port trunk allow-pass vlan {0}'),
    'track': CommandTemplate('track {0} decrement {1}', [r'[0-9]+', r'[0-9]+'],
                             ['Wrong track number!', 'Wrong track decrement number!']),
    'start_port_mode': CommandTemplate('portswitch'),
    'port_mode_trunk': CommandTemplate('port link-type trunk'),
    'port_mode_access': CommandTemplate('port link-type access'),
     'qnq': CommandTemplate('port link-type dot1q-tunnel'),
    'port_default_vlan' : CommandTemplate('port default vlan {0}',validateVlanRange, 'Cannot create vlan - wrong vlan number(s)'),
    'speed' : CommandTemplate('speed {0}', r'[0-9]+', 'Wrong speed number!')
}

