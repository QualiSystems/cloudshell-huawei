#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict


class SnmpPortAttrTables(object):
    def __init__(self, snmp_handler, logger):
        self._snmp = snmp_handler
        self._logger = logger
        self._lldp_remote_table = None
        self._lldp_local_table = None
        self._cdp_table = None
        self._duplex_table = None
        # self._cisco_duplex_state_table = None
        self._ip_v4_table = None
        self._ip_v6_table = None
        self._port_channel_ports = None

    @property
    def lldp_remote_table(self):
        if self._lldp_remote_table is None:
            self._lldp_remote_table = self._snmp.get_table('LLDP-MIB', 'lldpRemSysName')
            self._logger.info('lldpRemSysName table loaded')
        return self._lldp_remote_table

    @property
    def lldp_local_table(self):
        if self._lldp_local_table is None:
            lldp_local_table = self._snmp.get_table('LLDP-MIB', 'lldpLocPortDesc')
            if lldp_local_table:
                self._lldp_local_table = dict(
                    [(v['lldpLocPortDesc'].lower(), k) for k, v in lldp_local_table.iteritems()])
            else:
                self._lldp_local_table = defaultdict()
            self._logger.info('lldpLocPortDesc table loaded')
        return self._lldp_local_table

    # @property
    # def cdp_table(self):
    #     if self._cdp_table is None:
    #         self._cdp_table = self._snmp.get_table('CISCO-CDP-MIB', 'cdpCacheDeviceId')
    #         self._logger.info('cdpCacheDeviceId table loaded')
    #     return self._cdp_table

    @property
    def duplex_table(self):
        if self._duplex_table is None:
            self._duplex_table = self._snmp.get_table('EtherLike-MIB', 'dot3StatsIndex')
            self._logger.info('dot3StatsIndex table loaded')
        return self._duplex_table

    # @property
    # def cisco_duplex_state_table(self):
    #     if self._cisco_duplex_state_table is None:
    #         self._cisco_duplex_state_table = dict()
    #         cisco_duplex_state_table = self._snmp.get_table('CISCO-STACK-MIB', 'portIfIndex')
    #         if cisco_duplex_state_table:
    #             self._cisco_duplex_state_table = dict(
    #                 [(v.get('portIfIndex', "").lower(), k) for k, v in cisco_duplex_state_table.iteritems()])
    #         self._logger.info('Duplex portIfIndex table loaded')
    #     return self._cisco_duplex_state_table

    @property
    def ip_v4_table(self):
        if self._ip_v4_table is None:
            self._ip_v4_table = self._snmp.get_table('IP-MIB', 'ipAddrTable')
            self._logger.info('ipAddrTable table loaded')
        return self._ip_v4_table

    @property
    def ip_v6_table(self):
        if self._ip_v6_table is None:
            self._ip_v6_table = self._snmp.get_table('IPV6-MIB', 'ipv6AddrEntry')
            self._logger.info('ipv6AddrEntry table loaded')
        return self._ip_v6_table

    @property
    def port_channel_ports(self):
        if self._port_channel_ports is None:
            self._port_channel_ports = self._snmp.get_table('IEEE8023-LAG-MIB',
                                                            'dot3adAggPortAttachedAggID')
            self._logger.info('dot3adAggPortAttachedAggID table loaded')
        return self._port_channel_ports
