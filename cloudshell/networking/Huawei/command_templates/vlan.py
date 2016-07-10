from cloudshell.cli.command_template.command_template import CommandTemplate


from cloudshell.networking.networking_utils import validateIP, validateVlanRange


VLAN_COMMANDS_TEMPLATES = {
    'configure_interface': CommandTemplate('interface {0} {1]', [r'[\w-]+\s*[0-9/]+',r'[\w-]+\s*[0-9/]+'],
                                           ['Interface name is incorrect!','Interface value is incorrect!']),
    'ip_address': CommandTemplate('ip address {0} {1}', [validateIP, validateIP],
                                  ['Wrong ip address!', 'Wrong ip mask!']),
    'configure_vlan': CommandTemplate('vlan {0}', validateVlanRange, 'Cannot create vlan - wrong vlan number(s)'),
    'quit': CommandTemplate('quit'),
    'hsrp': CommandTemplate('hsrp {0}', ['[0-9]+'],
                            ['Wrong router protocol id!']),
    'authentication': CommandTemplate('authentication {0}', [r'\w+'],
                                      ['Wrong authentication name!']),
    'undo_shutdown': CommandTemplate('undo shutdown'),
    'allow_trunk_vlan': CommandTemplate('port trunk allow-pass vlan {0}', validateVlanRange,
                                        'Wrong allowed vlan id!'),
    'description': CommandTemplate('description'),
    'mode trunk': CommandTemplate('port link-type trunk'),
    'preempt': CommandTemplate('preempt'),
    'access vlan': CommandTemplate('port link-type access'),
    'shutdown': CommandTemplate('shutdown'),
    'priority': CommandTemplate('priority {0}', ['[0-9]+'], ['Wrong priority number!']),
    'no trunk': CommandTemplate('undo port trunk allow-pass vlan {0}'),
    'track': CommandTemplate('track {0} decrement {1}', [r'[0-9]+', r'[0-9]+'],
                             ['Wrong track number!', 'Wrong track decrement number!'])
}

