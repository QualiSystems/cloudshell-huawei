#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.flows.cli_action_flows import EnableSnmpFlow
from cloudshell.snmp.snmp_parameters import SNMPV3Parameters, SNMPV2WriteParameters

from cloudshell.networking.huawei.command_actions.system_actions import SystemActions
from cloudshell.networking.huawei.command_actions.enable_disable_snmp_actions import \
    EnableDisableSnmpV2Actions, EnableDisableSnmpV3Actions


class HuaweiEnableSnmpFlow(EnableSnmpFlow):
    DEFAULT_SNMP_ACCESS = "read"

    def execute_flow(self, snmp_parameters):
        if isinstance(snmp_parameters, SNMPV3Parameters):
            snmp_parameters.snmp_access = self.DEFAULT_SNMP_ACCESS
            Flow = HuaweiEnableSnmpV3
        else:
            Flow = HuaweiEnableSnmpV2

        Flow(self._cli_handler, self._logger, snmp_parameters).execute()


class HuaweiEnableSnmpV2(object):
    def __init__(self, cli_handler, logger, snmp_parameters):
        """ Enable SNMP v2c """

        self._cli_handler = cli_handler
        self._logger = logger
        self.snmp_parameters = snmp_parameters

    def execute(self):
        community = self.snmp_parameters.snmp_community
        if isinstance(self.snmp_parameters, SNMPV2WriteParameters):
            raise Exception("Devices doesn't support write communities")

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as conf_session:
            self._logger.info("Start creating SNMP community {}".format(community))

            snmp_actions = EnableDisableSnmpV2Actions(conf_session, self._logger)
            system_actions = SystemActions(conf_session, self._logger)
            snmp_actions.enable_snmp_service()
            snmp_actions.configure_snmp_version()
            snmp_actions.configure_snmp_comminity(community=community)
            system_actions.commit()

        self._logger.info("SNMP v2c community {} created".format(community))


class HuaweiEnableSnmpV3(object):
    ENCRYPTION = {"MD5": "md5",
                  "SHA": "sha",
                  "DES": "des56",
                  "3DES-EDE": "3des",
                  "AES-128": "aes128",
                  "AES-192": "aes192",
                  "AES-256": "aes256"}

    def __init__(self, cli_handler, logger, snmp_param):
        """ Enable SNMP v3 """

        self._cli_handler = cli_handler
        self._logger = logger
        self.snmp_param = snmp_param

    def _get_auth_type(self, user, password, priv_key):
        """ Determine authentication type based on provided snmp parameters.
        :return noauthentication or authentication or privacy or raise exception """

        if user and password and priv_key:
            return "privacy"
        elif user and password:
            return "authentication"
        elif user:
            return "noauthentication"
        else:
            raise Exception("Wrong SNMPv3 parameters")

    def execute(self):
        """  """

        auth_type = self._get_auth_type(user=self.snmp_param.snmp_user,
                                        password=self.snmp_param.snmp_password,
                                        priv_key=self.snmp_param.snmp_private_key)

        auth_protocol = self.ENCRYPTION.get(self.snmp_param.auth_protocol)
        if not auth_protocol:
            raise Exception("Wrong authentication protocol ({}) provided".format(self.snmp_param.auth_protocol))
        private_key_protocol = self.ENCRYPTION.get(self.snmp_param.private_key_protocol)

        if not private_key_protocol:
            raise Exception("Wrong privacy key protocol ({}) provided".format(self.snmp_param.private_key_protocol))

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as conf_session:
            self._logger.info("Start creating SNMPv3 configuration")
            snmp_actions = EnableDisableSnmpV3Actions(conf_session, self._logger)
            system_actions = SystemActions(conf_session, self._logger)

            snmp_actions.enable_snmp_service()
            snmp_actions.configure_snmp_version()
            snmp_actions.configure_snmp_v3(snmp_access=self.snmp_param.snmp_access,
                                           user=self.snmp_param.snmp_user,
                                           auth_type=auth_type,
                                           auth_protocol=auth_protocol,
                                           auth_password=self.snmp_param.snmp_password,
                                           priv_protocol=private_key_protocol,
                                           priv_password=self.snmp_param.snmp_private_key)

            system_actions.commit()

            self._logger.info("SNMP User {} created".format(self.snmp_param.snmp_user))
