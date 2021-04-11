#!/usr/bin/python
# -*- coding: utf-8 -*-


class HuaweiBaseException(Exception):
    """Base Huawei exception."""


class HuaweiSNMPException(HuaweiBaseException):
    """Huawei enable/disable SNMP configuration exception."""


class HuaweiSaveRestoreException(HuaweiBaseException):
    """Huawei save/restore configuration exception."""


class HuaweiConnectivityException(HuaweiBaseException):
    """Huawei connectivity exception."""


class HuaweiFirmwareException(HuaweiBaseException):
    """Huawei load firmware exception."""
