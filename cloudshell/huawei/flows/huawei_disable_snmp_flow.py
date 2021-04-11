#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.snmp.snmp_parameters import SNMPWriteParameters

from cloudshell.huawei.command_actions.enable_disable_snmp_actions import (
    EnableDisableSnmpActions,
)
from cloudshell.huawei.command_actions.system_actions import SystemActions
from cloudshell.huawei.helpers.exceptions import HuaweiSNMPException


class HuaweiDisableSnmpFlow(object):
    def __init__(self, cli_handler, logger):
        """Disable SNMP flow."""
        self._cli_handler = cli_handler
        self._logger = logger

    def disable_flow(self, snmp_parameters):
        with self._cli_handler.get_cli_service(
            self._cli_handler.config_mode
        ) as conf_session:
            snmp_actions = EnableDisableSnmpActions(conf_session, self._logger)
            system_actions = SystemActions(conf_session, self._logger)

            if "3" in snmp_parameters.version:
                self._logger.info("Start removing SNMP v3 configuration")
                snmp_actions.remove_snmp_v3(user=snmp_parameters.snmp_user)
                system_actions.commit()
                self._logger.info("SNMP v3 configuration removed")
            else:
                community = snmp_parameters.snmp_community
                if isinstance(snmp_parameters, SNMPWriteParameters):
                    raise HuaweiSNMPException(
                        "Devices doesn't support write communities"
                    )

                self._logger.info("Start removing SNMP community {}".format(community))
                snmp_actions.remove_snmp_comminity(community=community)
                system_actions.commit()
                self._logger.info("SNMP community {} removed".format(community))
