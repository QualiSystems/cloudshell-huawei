#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import unittest

import mock

from cloudshell.networking.huawei.flows.huawei_add_vlan_flow import HuaweiAddVlanFlow


class TestHuaweiAddVlanFlow(unittest.TestCase):
    def setUp(self):
        cli_handler = mock.MagicMock()
        logger = mock.MagicMock()
        super(TestHuaweiAddVlanFlow, self).setUp()
        self.tested_instance = HuaweiAddVlanFlow(cli_handler=cli_handler, logger=logger)

    def tearDown(self):
        super(TestHuaweiAddVlanFlow, self).tearDown()
        del self.tested_instance

    def test_execute_flow_fail_unsupported_port_mode(self):
        """ Unsupported port mode """

        with self.assertRaisesRegexp(Exception, "Unsupported port mode"):
            self.tested_instance.execute_flow(
                "vlan_range", "port_mode", "port_name", False, "c_tag"
            )

    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_add_vlan_flow.AddRemoveVlanActions"
    )
    @mock.patch("cloudshell.networking.huawei.flows.huawei_add_vlan_flow.SystemActions")
    def test_execute_flow_success_single(self, sys_actions_class, vlan_actions_class):
        """ Successfully create single VLAN without QnQ """

        vlan = "10"
        port_mode = "trunk"
        full_port_name = "full_port_name"
        port_name = "port_name"
        qnq = False
        ctag = "c_tag"

        sys_actions = mock.MagicMock()
        sys_actions_class.return_value = sys_actions
        sys_actions.display_running_config.side_effect = [
            "Device configuration before Add VLAN Commands",
            "vlan {vlan} added successfully".format(vlan=vlan),
        ]
        vlan_actions = mock.MagicMock()
        vlan_actions_class.return_value = vlan_actions
        vlan_actions.get_port_name.return_value = port_name

        self.tested_instance.execute_flow(vlan, port_mode, full_port_name, qnq, ctag)

        vlan_actions.get_port_name.assert_called_once_with(full_port_name)
        vlan_actions.configure_interface.assert_called_once_with(port_name=port_name)
        sys_actions.clean_current_configuration_on_interface.assert_called_once()
        vlan_actions.activate_port.assert_called_once()
        vlan_actions.activate_port_mode.assert_called_once()

        vlan_actions.create_vlan_range.assert_not_called()
        vlan_actions.set_vlan_range_to_interface.assert_not_called()

        vlan_actions.create_vlan.assert_called_once_with(vlan)
        vlan_actions.set_vlan_to_interface.assert_called_once_with(vlan, port_mode, qnq)

    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_add_vlan_flow.AddRemoveVlanActions"
    )
    @mock.patch("cloudshell.networking.huawei.flows.huawei_add_vlan_flow.SystemActions")
    def test_execute_flow_success_range(self, sys_actions_class, vlan_actions_class):
        """ Successfully create VLAN range without QnQ """

        start_vlan = "10"
        end_vlan = "100"
        vlan = "{start}-{end}".format(start=start_vlan, end=end_vlan)
        port_mode = "trunk"
        full_port_name = "full_port_name"
        port_name = "port_name"
        qnq = False
        ctag = "c_tag"

        sys_actions = mock.MagicMock()
        sys_actions_class.return_value = sys_actions
        sys_actions.display_running_config.side_effect = [
            "Device configuration before Add VLAN Commands",
            "vlan {vlan} added successfully".format(vlan=vlan),
        ]
        vlan_actions = mock.MagicMock()
        vlan_actions_class.return_value = vlan_actions
        vlan_actions.get_port_name.return_value = port_name

        self.tested_instance.execute_flow(vlan, port_mode, full_port_name, qnq, ctag)

        vlan_actions.get_port_name.assert_called_once_with(full_port_name)
        vlan_actions.configure_interface.assert_called_once_with(port_name=port_name)
        sys_actions.clean_current_configuration_on_interface.assert_called_once()
        vlan_actions.activate_port.assert_called_once()
        vlan_actions.activate_port_mode.assert_called_once()

        vlan_actions.create_vlan_range.assert_called_once_with(start_vlan, end_vlan)
        vlan_actions.set_vlan_range_to_interface.assert_called_once_with(
            start_vlan, end_vlan, port_mode
        )

        vlan_actions.create_vlan.assert_not_called()
        vlan_actions.set_vlan_to_interface.assert_not_called()

    @mock.patch(
        "cloudshell.networking.huawei.flows.huawei_add_vlan_flow.AddRemoveVlanActions"
    )
    @mock.patch("cloudshell.networking.huawei.flows.huawei_add_vlan_flow.SystemActions")
    def test_execute_flow_fail(self, sys_actions_class, vlan_actions_class):
        """ Connectivity configuration failed """

        vlan = "10"
        port_mode = "trunk"
        full_port_name = "full_port_name"
        port_name = "port_name"
        qnq = False
        ctag = "c_tag"

        sys_actions = mock.MagicMock()
        sys_actions_class.return_value = sys_actions
        sys_actions.display_running_config.side_effect = [
            "Device configuration before Add VLAN Commands",
            "Connectivity configuration failed",
        ]
        vlan_actions = mock.MagicMock()
        vlan_actions_class.return_value = vlan_actions
        vlan_actions.get_port_name.return_value = port_name

        with self.assertRaisesRegexp(
            Exception, re.escape("[FAIL] VLAN(s) {} configuration failed".format(vlan))
        ):
            self.tested_instance.execute_flow(
                vlan, port_mode, full_port_name, qnq, ctag
            )
