#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

from cloudshell.huawei.flows.huawei_enable_snmp_flow import (
    HuaweiEnableSnmpFlow,
)

try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch


class TestHuaweiEnableSNMPFlow(TestCase):
    def test_import(self):
        self.assertTrue(HuaweiEnableSnmpFlow)
