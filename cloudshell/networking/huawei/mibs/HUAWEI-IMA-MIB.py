#
# PySNMP MIB module HUAWEI-IMA-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/HUAWEI-IMA-MIB
# Produced by pysmi-0.0.7 at Sun Jul  3 11:25:20 2016
# On host localhost.localdomain platform Linux version 3.10.0-229.7.2.el7.x86_64 by user root
# Using Python version 2.7.5 (default, Jun 24 2015, 00:41:19) 
#
(Integer, ObjectIdentifier, OctetString,) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier",
                                                                     "OctetString")
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint,
 ValueRangeConstraint,) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint",
                                                   "ConstraintsIntersection", "ValueSizeConstraint",
                                                   "ValueRangeConstraint")
(hwDatacomm,) = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
(ifIndex, InterfaceIndexOrZero, InterfaceIndex,) = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero",
                                                                            "InterfaceIndex")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits,
 Counter32,) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow",
                                        "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks",
                                        "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso",
                                        "ObjectIdentity", "Bits", "Counter32")
(DisplayString, RowStatus, TextualConvention, DateAndTime,) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString",
                                                                                       "RowStatus", "TextualConvention",
                                                                                       "DateAndTime")
hwImaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176))
hwImaMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1))
hwImaMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2))
hwImaNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3))


class MilliSeconds(Integer32, TextualConvention):
    pass


class ImaGroupState(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, )
    namedValues = NamedValues(("notConfigured", 1), ("startUp", 2), ("startUpAck", 3), ("configAbortUnsupportedM", 4),
                              ("configAbortIncompatibleSymmetry", 5), ("configAbortOther", 6), ("insufficientLinks", 7),
                              ("blocked", 8), ("operational", 9), ("configAbortUnsupportedImaVersion", 10), )


class ImaGroupSymmetry(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, )
    namedValues = NamedValues(("symmetricOperation", 1), ("asymmetricOperation", 2), ("asymmetricConfiguration", 3), )


class ImaFrameLength(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, )
    namedValues = NamedValues(("m32", 1), ("m64", 2), ("m128", 3), ("m256", 4), )


class ImaLinkState(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, )
    namedValues = NamedValues(("notInGroup", 1), ("unusableNoGivenReason", 2), ("unusableFault", 3),
                              ("unusableMisconnected", 4), ("unusableInhibited", 5), ("unusableFailed", 6),
                              ("usable", 7), ("active", 8), )


hwImaGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1), )
hwImaGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1), ).setIndexNames(
    (0, "HUAWEI-IMA-MIB", "hwImaGroupIfIndex"))
hwImaGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess(
    "readonly")
hwImaGroupNeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 2), ImaGroupState()).setMaxAccess(
    "readonly")
hwImaGroupFeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 3), ImaGroupState()).setMaxAccess(
    "readonly")
hwImaGroupSymmetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 4), ImaGroupSymmetry()).setMaxAccess(
    "readonly")
hwImaGroupMinNumTxLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 5),
                                         Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess(
    "readcreate")
hwImaGroupMinNumRxLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 6),
                                         Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess(
    "readcreate")
hwImaGroupTxTimingRefLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 7),
                                           InterfaceIndexOrZero()).setMaxAccess("readonly")
hwImaGroupRxTimingRefLink = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 8),
                                           InterfaceIndexOrZero()).setMaxAccess("readonly")
hwImaGroupTxImaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 9),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readonly")
hwImaGroupRxImaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 10),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readonly")
hwImaGroupTxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 11),
                                         ImaFrameLength()).setMaxAccess("readcreate")
hwImaGroupRxFrameLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 12),
                                         ImaFrameLength()).setMaxAccess("readonly")
hwImaGroupDiffDelayMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 13),
                                        MilliSeconds().subtype(subtypeSpec=ValueRangeConstraint(25, 120))).setMaxAccess(
    "readcreate")
hwImaGroupAlphaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 14),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess(
    "readonly")
hwImaGroupBetaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 15),
                                     Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess(
    "readonly")
hwImaGroupGammaValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 16),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess(
    "readonly")
hwImaGroupNumTxActLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 17), Gauge32()).setMaxAccess(
    "readonly")
hwImaGroupNumRxActLinks = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 18), Gauge32()).setMaxAccess(
    "readonly")
hwImaGroupTxOamLabelValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 19),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess(
    "readonly")
hwImaGroupRxOamLabelValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 20),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readonly")
hwImaGroupFirstLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 21),
                                            InterfaceIndex()).setMaxAccess("readonly")
hwImaGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 22), OctetString()).setMaxAccess(
    "accessiblefornotify")
hwImaLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2), )
hwImaLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1), ).setIndexNames(
    (0, "HUAWEI-IMA-MIB", "hwImaLinkIfIndex"))
hwImaLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 1), InterfaceIndex())
hwImaLinkGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess(
    "readcreate")
hwImaLinkNeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 3), ImaLinkState()).setMaxAccess(
    "readonly")
hwImaLinkNeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 4), ImaLinkState()).setMaxAccess(
    "readonly")
hwImaLinkFeTxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 5), ImaLinkState()).setMaxAccess(
    "readonly")
hwImaLinkFeRxState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 6), ImaLinkState()).setMaxAccess(
    "readonly")
hwImaLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 51), RowStatus()).setMaxAccess(
    "readcreate")
hwImaLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 52), OctetString()).setMaxAccess(
    "accessiblefornotify")
hwImaAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3), )
hwImaAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1), ).setIndexNames(
    (0, "HUAWEI-IMA-MIB", "hwImaAlarmIfIndex"))
hwImaAlarmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 1), Integer32())
hwImaGroupNeDownEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 2), Integer32()).setMaxAccess(
    "readwrite")
hwImaGroupFeDownEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 3), Integer32()).setMaxAccess(
    "readwrite")
hwImaGroupTxClkMismatchEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 4), Integer32()).setMaxAccess(
    "readwrite")
hwImaLinkLifEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
hwImaLinkLodsEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 6), Integer32()).setMaxAccess(
    "readwrite")
hwImaLinkRfiEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
hwImaLinkFeTxUnusableEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 8), Integer32()).setMaxAccess(
    "readwrite")
hwImaLinkFeRxUnusableEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 9), Integer32()).setMaxAccess(
    "readwrite")
hwIMAAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 3, 1, 10), Integer32()).setMaxAccess("readwrite")
hwImaMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1))
hwImaMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2))
hwImaMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2, 1)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupGroup"), ("HUAWEI-IMA-MIB", "hwImaLinkGroup"),))
hwImaGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 1)).setObjects(*(
("HUAWEI-IMA-MIB", "hwImaGroupIfIndex"), ("HUAWEI-IMA-MIB", "hwImaGroupNeState"),
("HUAWEI-IMA-MIB", "hwImaGroupFeState"), ("HUAWEI-IMA-MIB", "hwImaGroupSymmetry"),
("HUAWEI-IMA-MIB", "hwImaGroupMinNumTxLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupMinNumRxLinks"),
("HUAWEI-IMA-MIB", "hwImaGroupTxTimingRefLink"), ("HUAWEI-IMA-MIB", "hwImaGroupRxTimingRefLink"),
("HUAWEI-IMA-MIB", "hwImaGroupTxImaId"), ("HUAWEI-IMA-MIB", "hwImaGroupRxImaId"),
("HUAWEI-IMA-MIB", "hwImaGroupTxFrameLength"), ("HUAWEI-IMA-MIB", "hwImaGroupRxFrameLength"),
("HUAWEI-IMA-MIB", "hwImaGroupDiffDelayMax"), ("HUAWEI-IMA-MIB", "hwImaGroupAlphaValue"),
("HUAWEI-IMA-MIB", "hwImaGroupBetaValue"), ("HUAWEI-IMA-MIB", "hwImaGroupGammaValue"),
("HUAWEI-IMA-MIB", "hwImaGroupNumTxActLinks"), ("HUAWEI-IMA-MIB", "hwImaGroupNumRxActLinks"),
("HUAWEI-IMA-MIB", "hwImaGroupTxOamLabelValue"), ("HUAWEI-IMA-MIB", "hwImaGroupRxOamLabelValue"),
("HUAWEI-IMA-MIB", "hwImaGroupFirstLinkIfIndex"),))
hwImaLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 2)).setObjects(*(
("HUAWEI-IMA-MIB", "hwImaLinkGroupIfIndex"), ("HUAWEI-IMA-MIB", "hwImaLinkNeTxState"),
("HUAWEI-IMA-MIB", "hwImaLinkNeRxState"), ("HUAWEI-IMA-MIB", "hwImaLinkFeTxState"),
("HUAWEI-IMA-MIB", "hwImaLinkFeRxState"), ("HUAWEI-IMA-MIB", "hwImaLinkRowStatus"),))
hwImaGroupNeDownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 1)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaGroupNeDownAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 2)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaGroupFeDownAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 3)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaGroupFeDownAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 4)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaGroupTxClkMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 5)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaGroupTxClkMismatchResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 6)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaGroupName"),))
hwImaLinkLifAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 7)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkLifAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 8)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkLodsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 9)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkLodsAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 10)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkRfiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 11)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkRfiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 12)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkFeTxUnusableAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 13)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkFeTxUnusableAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 14)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkFeRxUnusableAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 15)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
hwImaLinkFeRxUnusableAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 3, 16)).setObjects(
    *(("HUAWEI-IMA-MIB", "hwImaLinkName"),))
mibBuilder.exportSymbols("HUAWEI-IMA-MIB", hwImaGroupFirstLinkIfIndex=hwImaGroupFirstLinkIfIndex,
                         hwImaLinkFeRxState=hwImaLinkFeRxState, PYSNMP_MODULE_ID=hwImaMIB,
                         hwImaLinkRfiEn=hwImaLinkRfiEn, hwImaGroupNumRxActLinks=hwImaGroupNumRxActLinks,
                         hwImaLinkRfiAlarmResume=hwImaLinkRfiAlarmResume, hwImaLinkLifAlarm=hwImaLinkLifAlarm,
                         hwImaGroupTxClkMismatch=hwImaGroupTxClkMismatch,
                         hwImaGroupRxOamLabelValue=hwImaGroupRxOamLabelValue, hwImaLinkLifEn=hwImaLinkLifEn,
                         hwImaGroupFeDownAlarmResume=hwImaGroupFeDownAlarmResume, hwImaLinkNeRxState=hwImaLinkNeRxState,
                         hwImaGroupFeDownAlarm=hwImaGroupFeDownAlarm, ImaGroupState=ImaGroupState,
                         hwImaAlarmIfIndex=hwImaAlarmIfIndex, hwImaGroupNeDownEn=hwImaGroupNeDownEn,
                         hwImaLinkEntry=hwImaLinkEntry, hwImaGroupRxTimingRefLink=hwImaGroupRxTimingRefLink,
                         hwImaGroupNeDownAlarm=hwImaGroupNeDownAlarm, hwImaGroupTable=hwImaGroupTable,
                         hwImaLinkFeTxState=hwImaLinkFeTxState, ImaGroupSymmetry=ImaGroupSymmetry,
                         hwImaLinkName=hwImaLinkName, hwImaLinkLodsEn=hwImaLinkLodsEn,
                         hwImaGroupFeState=hwImaGroupFeState, hwImaLinkIfIndex=hwImaLinkIfIndex,
                         hwImaGroupMinNumRxLinks=hwImaGroupMinNumRxLinks, hwImaMIB=hwImaMIB,
                         hwImaGroupGroup=hwImaGroupGroup, hwImaLinkFeTxUnusableEn=hwImaLinkFeTxUnusableEn,
                         hwImaNotifications=hwImaNotifications, hwImaGroupFeDownEn=hwImaGroupFeDownEn,
                         hwImaGroupTxImaId=hwImaGroupTxImaId, hwImaGroupTxFrameLength=hwImaGroupTxFrameLength,
                         hwIMAAllEn=hwIMAAllEn, ImaLinkState=ImaLinkState,
                         hwImaLinkFeRxUnusableAlarm=hwImaLinkFeRxUnusableAlarm,
                         hwImaLinkFeRxUnusableAlarmResume=hwImaLinkFeRxUnusableAlarmResume,
                         hwImaLinkLifAlarmResume=hwImaLinkLifAlarmResume,
                         hwImaGroupNeDownAlarmResume=hwImaGroupNeDownAlarmResume, hwImaGroupEntry=hwImaGroupEntry,
                         hwImaMibCompliances=hwImaMibCompliances, hwImaAlarmEntry=hwImaAlarmEntry,
                         hwImaLinkRowStatus=hwImaLinkRowStatus, hwImaLinkLodsAlarm=hwImaLinkLodsAlarm,
                         hwImaGroupNeState=hwImaGroupNeState, hwImaMibCompliance=hwImaMibCompliance,
                         hwImaLinkFeTxUnusableAlarm=hwImaLinkFeTxUnusableAlarm, hwImaGroupIfIndex=hwImaGroupIfIndex,
                         hwImaGroupTxClkMismatchEn=hwImaGroupTxClkMismatchEn,
                         hwImaGroupDiffDelayMax=hwImaGroupDiffDelayMax, hwImaGroupRxFrameLength=hwImaGroupRxFrameLength,
                         hwImaGroupTxClkMismatchResume=hwImaGroupTxClkMismatchResume,
                         hwImaGroupTxOamLabelValue=hwImaGroupTxOamLabelValue,
                         hwImaGroupTxTimingRefLink=hwImaGroupTxTimingRefLink, hwImaGroupBetaValue=hwImaGroupBetaValue,
                         hwImaGroupName=hwImaGroupName, hwImaMibGroups=hwImaMibGroups,
                         hwImaGroupRxImaId=hwImaGroupRxImaId, hwImaLinkFeRxUnusableEn=hwImaLinkFeRxUnusableEn,
                         hwImaAlarmTable=hwImaAlarmTable, hwImaLinkNeTxState=hwImaLinkNeTxState,
                         hwImaGroupSymmetry=hwImaGroupSymmetry, hwImaMibConformance=hwImaMibConformance,
                         hwImaMibObjects=hwImaMibObjects, MilliSeconds=MilliSeconds,
                         hwImaGroupMinNumTxLinks=hwImaGroupMinNumTxLinks, hwImaLinkTable=hwImaLinkTable,
                         hwImaLinkGroup=hwImaLinkGroup, hwImaLinkRfiAlarm=hwImaLinkRfiAlarm,
                         ImaFrameLength=ImaFrameLength, hwImaGroupGammaValue=hwImaGroupGammaValue,
                         hwImaGroupAlphaValue=hwImaGroupAlphaValue, hwImaLinkLodsAlarmResume=hwImaLinkLodsAlarmResume,
                         hwImaGroupNumTxActLinks=hwImaGroupNumTxActLinks,
                         hwImaLinkFeTxUnusableAlarmResume=hwImaLinkFeTxUnusableAlarmResume,
                         hwImaLinkGroupIfIndex=hwImaLinkGroupIfIndex)
