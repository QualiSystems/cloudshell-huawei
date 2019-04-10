#!/usr/bin/python
# -*- coding: utf-8 -*-


class SnmpIfEntity(object):
    IF_MIB = "IF-MIB"
    IF_NAME = "ifDescr"
    IF_ALIAS = "ifAlias"

    def __init__(self, snmp_handler, logger, index, port_attributes_snmp_tables):
        self.if_index = int(index)
        self._snmp = snmp_handler
        self._port_attributes_snmp_tables = port_attributes_snmp_tables
        self._logger = logger
        self._ipv4 = ""
        self._ipv6 = ""
        self._if_alias = ""
        self._if_name = ""

    @property
    def if_name(self):
        if not self._if_name:
            self._if_name = self._snmp.get_property(self.IF_MIB, self.IF_NAME, self.if_index)
        return self._if_name

    @property
    def if_port_description(self):
        if not self._if_alias:
            self._if_alias = self._snmp.get_property(self.IF_MIB, self.IF_ALIAS, self.if_index)
        return self._if_alias

    @property
    def ipv4_address(self):
        if not self._ipv4:
            self._ipv4 = self._get_ipv4()
        return self._ipv4

    @property
    def ipv6_address(self):
        if not self._ipv6:
            self._ipv6 = self._get_ipv6()
        return self._ipv6

    def _get_ipv4(self):
        """Get IPv4 address details for provided port

        :return str IPv4 Address
        """

        if self._port_attributes_snmp_tables.ip_v4_table:
            for key, value in self._port_attributes_snmp_tables.ip_v4_table.iteritems():
                if 'ipAdEntIfIndex' in value and int(value['ipAdEntIfIndex']) == self.if_index:
                    return key

    def _get_ipv6(self):
        """Get IPv6 address details for provided port

        :return str IPv6 Address
        """

        if self._port_attributes_snmp_tables.ip_v6_table:
            for key, value in self._port_attributes_snmp_tables.ip_v6_table.iteritems():
                if 'ipAdEntIfIndex' in value and int(value['ipAdEntIfIndex']) == self.if_index:
                    return key
