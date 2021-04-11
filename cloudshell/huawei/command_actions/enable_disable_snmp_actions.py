#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.cli.command_template.command_template_executor import (
    CommandTemplateExecutor,
)

from cloudshell.huawei.command_templates import enable_disable_snmp
from cloudshell.huawei.helpers.exceptions import HuaweiSNMPException


class EnableDisableSnmpActions(object):
    VIEW = "quali_view"
    GROUP = "quali_group"

    def __init__(self, cli_service, logger):
        """Enable Disable Snmp actions."""
        self._cli_service = cli_service
        self._logger = logger

    def enable_snmp_service(self):
        """Enable SNMP agent and configure SNMP version."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.ACTIVATE_SNMP
        ).execute_command()

    def configure_snmp_version(self, snmp_version):
        """Configure SNMP Version."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_SNMP_VERSION
        ).execute_command(snmp_version=snmp_version)

    def configure_snmp_community(self, community):
        """Configure SNMP v2c community."""
        # Error: Wrong parameter found at '^' position.
        # Error: The password must consist of at least 2 types of characters,
        #        including lowercase letters, uppercase letters,
        #        digits and special characters.
        output = CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V2C_COMMUNITY
        ).execute_command(community=community)
        if "Error:" in output:
            self._logger.error(
                "Configuration SNMP v2c community failed. {}".format(output)
            )
            raise HuaweiSNMPException("Configuration SNMP v2c community failed")

    def remove_snmp_comminity(self, community):
        """Remove SNMP v2c community."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.REMOVE_V2C_COMMUNITY
        ).execute_command(community=community)

    def configure_snmp_v3(
        self,
        snmp_access,
        user,
        auth_type,
        auth_protocol,
        auth_password,
        priv_protocol,
        priv_password,
    ):
        """Configure SNMP v3."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V3_VIEW
        ).execute_command(view_name=self.VIEW)
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V3_GROUP
        ).execute_command(
            group_name=self.GROUP,
            auth_type=auth_type,
            snmp_access=snmp_access,
            view_name=self.VIEW,
        )

        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V3_USER
        ).execute_command(user_name=user, group_name=self.GROUP)

        command = CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V3_AUTH
        )
        command.update_action_map(
            {
                r"Password:": lambda session, logger: session.send_line(
                    auth_password, logger
                )
            }
        )
        command.execute_command(user_name=user, auth_protocol=auth_protocol)

        # Enter Password:
        # Confirm Password:
        command = CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.CONFIGURE_V3_PRIV
        )
        command.update_action_map(
            {
                r"Password:": lambda session, logger: session.send_line(
                    priv_password, logger
                )
            }
        )
        command.execute_command(user_name=user, priv_protocol=priv_protocol)

    def remove_snmp_v3(self, user):
        """Remove SNMP v3 configuration."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.REMOVE_V3_USER
        ).execute_command(user_name=user)

    def disable_snmp_service(self):
        """Disable SNMP service on the device."""
        CommandTemplateExecutor(
            self._cli_service, enable_disable_snmp.DEACTIVATE_SNMP
        ).execute_command()
