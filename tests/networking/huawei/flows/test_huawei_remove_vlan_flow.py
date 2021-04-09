#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import unittest

import mock

from cloudshell.networking.huawei.flows.huawei_remove_vlan_flow import (
    HuaweiRemoveVlanFlow,
)


class TestHuaweiRemoveVlanFlow(unittest.TestCase):
    def setUp(self):
        cli_handler = mock.MagicMock()
        logger = mock.MagicMock()
        super(TestHuaweiRemoveVlanFlow, self).setUp()
        self.tested_instance = HuaweiRemoveVlanFlow(
            cli_handler=cli_handler, logger=logger
        )

    def tearDown(self):
        super(TestHuaweiRemoveVlanFlow, self).tearDown()
        del self.tested_instance

    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_remove_vlan_flow.AddRemoveVlanActions"
    )
    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_remove_vlan_flow.SystemActions"
    )
    def test_execute_flow_success(self, sys_actions_class, vlan_actions_class):
        """ Successfully remove VLAN configuration """

        vlan = "10"
        port_mode = "trunk"
        full_port_name = "full_port_name"
        port_name = "port_name"
        qnq = False
        ctag = "c_tag"

        sys_actions = mock.MagicMock()
        sys_actions_class.return_value = sys_actions
        sys_actions.display_running_config.side_effect = [
            "Device configuration before Removing VLAN Commands",
            "Connectivity configuration removed",
        ]
        vlan_actions = mock.MagicMock()
        vlan_actions_class.return_value = vlan_actions
        vlan_actions.get_port_name.return_value = port_name

        self.tested_instance.execute_flow(vlan, port_mode, full_port_name, qnq, ctag)

        vlan_actions.get_port_name.assert_called_once_with(full_port_name)

        vlan_actions.configure_interface.assert_called_once_with(port_name=port_name)
        sys_actions.clean_current_configuration_on_interface.assert_called_once_with(
            configuration="Device configuration before Removing VLAN Commands"
        )
        sys_actions.commit.assert_called_once()

    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_remove_vlan_flow.AddRemoveVlanActions"
    )
    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_remove_vlan_flow.SystemActions"
    )
    def test_execute_flow_failed(self, sys_actions_class, vlan_actions_class):
        """ Successfully remove VLAN configuration """

        vlan = "10"
        port_mode = "trunk"
        full_port_name = "full_port_name"
        port_name = "port_name"
        qnq = False
        ctag = "c_tag"

        sys_actions = mock.MagicMock()
        sys_actions_class.return_value = sys_actions
        sys_actions.display_running_config.side_effect = [
            "Device configuration before Removing VLAN Commands",
            "vlan {vlan} still in configuration".format(vlan=vlan),
        ]
        vlan_actions = mock.MagicMock()
        vlan_actions_class.return_value = vlan_actions
        vlan_actions.get_port_name.return_value = port_name

        with self.assertRaisesRegexp(
            Exception, re.escape("[FAIL] VLAN(s) {} removing failed".format(vlan))
        ):
            self.tested_instance.execute_flow(
                vlan, port_mode, full_port_name, qnq, ctag
            )

        vlan_actions.get_port_name.assert_called_once_with(full_port_name)

        vlan_actions.configure_interface.assert_called_once_with(port_name=port_name)
        sys_actions.clean_current_configuration_on_interface.assert_called_once_with(
            configuration="Device configuration before Removing VLAN Commands"
        )
        sys_actions.commit.assert_called_once()
