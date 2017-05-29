#
# PySNMP MIB module HUAWEI-PORT-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/HUAWEI-PORT-MIB
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
(ImaGroupState, ImaFrameLength,) = mibBuilder.importSymbols("HUAWEI-IMA-MIB", "ImaGroupState", "ImaFrameLength")
(hwDatacomm,) = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
(InterfaceIndex,) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
(EnabledStatus,) = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks,
 Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32,) = mibBuilder.importSymbols(
    "SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType",
    "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso",
    "ObjectIdentity", "IpAddress", "Counter32")
(TruthValue, DisplayString, RowStatus, TextualConvention,) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue",
                                                                                      "DisplayString", "RowStatus",
                                                                                      "TextualConvention")

hwPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157))
hwPortMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1))
hwEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1))
hwEthernetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1), )
hwEthernetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwEthernetIfIndex"))
hwEthernetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 1), InterfaceIndex())
hwEthernetLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 11),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                        namedValues=NamedValues(("otherLoop", 1), ("stopLoopback", 2), ("local", 3),
                                                                ("remote", 4), ))).setMaxAccess("readwrite")

hwEthernetPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 12),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                        namedValues=NamedValues(("other", 1), ("copper", 2),
                                                                ("fiber", 3), ))).setMaxAccess("readwrite")

hwEthernetSpeedSet = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 13),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, )).clone(
                                        namedValues=NamedValues(("other", 1), ("speed10", 2), ("speed100", 3),
                                                                ("speed1000", 4), ("speed10000", 5), ))).setMaxAccess(
    "readwrite")

hwEthernetDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 14),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("full", 1), ("half", 2), ))).setMaxAccess("readwrite")

hwEthernetNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 15),
                                       EnabledStatus()).setMaxAccess("readwrite")
hwEthernetPortTypeOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 16),
                                           Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                               namedValues=NamedValues(("other", 1), ("copper", 2), ("fiber100", 3),
                                                                       ("fiber1000", 4), ))).setMaxAccess("readwrite")
hwEthernetClock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 20),
                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                     namedValues=NamedValues(("master", 1), ("slave", 2), ))).setMaxAccess("readwrite")

hwEthernetFlagJ0Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 21),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                          namedValues=NamedValues(("j01ByteMode", 1), ("j016ByteMode", 2),
                                                                  ("j064ByteOrNullMode", 3),
                                                                  ("peer", 4), ))).setMaxAccess("readwrite")
hwEthernetFlagJ0Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 22),
                                       Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readwrite")
hwEthernetFlagJ0Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 23),
                                       OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwEthernetFlagJ1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 24),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                          namedValues=NamedValues(("j11ByteMode", 1), ("j116ByteMode", 2),
                                                                  ("j164ByteOrNullMode", 3),
                                                                  ("peer", 4), ))).setMaxAccess("readwrite")
hwEthernetFlagJ1Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 25),
                                       Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readwrite")
hwEthernetFlagJ1Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 26),
                                       OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwEthernetFlagC2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 27),
                                       Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readwrite")
hwEthernetUpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 31),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400000))).setMaxAccess(
    "readwrite")
hwEthernetDownHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 32), Integer32().subtype(
    subtypeSpec=ValueRangeConstraint(0, 86400000))).setMaxAccess("readwrite")
hwEthernetSubinterfaceStatisticEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 33),
                                                       EnabledStatus()).setMaxAccess("readwrite")
hwEthernetFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 34),
                                       Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                           namedValues=NamedValues(("receive", 1), ("send", 2), ("both", 3),
                                                                   ("none", 4), ))).setMaxAccess("readwrite")
hwEthernetOffline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 35),
                                   Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                       namedValues=NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readwrite")
hwEthernetSetTransferMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 36),
                                           Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                               namedValues=NamedValues(("lan", 1), ("wan", 2),
                                                                       ("none", 3), ))).setMaxAccess("readwrite")
hwEthernetJumboframeMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 37),
                                               Integer32().subtype(
                                                   subtypeSpec=ValueRangeConstraint(1536, 13296))).setMaxAccess(
    "readwrite")
hwEthernetComboType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 38),
                                     Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                         namedValues=NamedValues(("auto", 1), ("copper", 2), ("fiber", 3),
                                                                 ("other", 4), ))).setMaxAccess("readwrite")
hwEthernetPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 39),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                        namedValues=NamedValues(("copper", 1), ("fiber", 2),
                                                                ("other", 3), ))).setMaxAccess("readonly")
hwEthernetNegotiationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 1, 1, 1, 40),
                                           Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                               namedValues=NamedValues(("notsupport", 1), ("auto", 2), ("master", 3),
                                                                       ("slave", 4), ))).setMaxAccess("readwrite")
hwPos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2))
hwPosTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1), )
hwPosEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPosIfIndex"))
hwPosIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 1), InterfaceIndex())
hwPosLinkProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 11),
                                   Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                       namedValues=NamedValues(("ietf", 1), ("nonstandard", 2), ("hdlc", 3),
                                                               ("ppp", 4), ))).setMaxAccess("readwrite")
hwPosFrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 12),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("sonet", 1), ("sdh", 2), ))).setMaxAccess("readwrite")
hwPosLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 13),
                               Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                   namedValues=NamedValues(("otherLoop", 1), ("stopLoopback", 2), ("local", 3),
                                                           ("remote", 4), ))).setMaxAccess("readwrite")
hwPosScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 14), EnabledStatus()).setMaxAccess(
    "readwrite")
hwPosClock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 15),
                            Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                namedValues=NamedValues(("master", 1), ("slave", 2), ))).setMaxAccess("readwrite")
hwPosCrcVerifyCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 16),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                        namedValues=NamedValues(("crc16", 1), ("crc32", 2), ))).setMaxAccess(
    "readwrite")
hwPosFlagJ0Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 21),
                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                     namedValues=NamedValues(("j01ByteMode", 1), ("j016ByteMode", 2),
                                                             ("j064ByteOrNullMode", 3), ("peer", 4), ))).setMaxAccess(
    "readwrite")
hwPosFlagJ0Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 22),
                                  Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess(
    "readwrite")
hwPosFlagJ0Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 23),
                                  OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwPosFlagJ1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 24),
                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                     namedValues=NamedValues(("j11ByteMode", 1), ("j116ByteMode", 2),
                                                             ("j164ByteOrNullMode", 3), ("peer", 4), ))).setMaxAccess(
    "readwrite")
hwPosFlagJ1Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 25),
                                  Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess(
    "readwrite")
hwPosFlagJ1Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 26),
                                  OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwPosFlagC2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 2, 1, 1, 27),
                                  Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readwrite")
hwCpos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3))
hwCposTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1), )
hwCposEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwCposIfIndex"))
hwCposIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 1), InterfaceIndex())
hwCposClock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 11),
                             Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                 namedValues=NamedValues(("master", 1), ("slave", 2), ))).setMaxAccess("readwrite")
hwCposIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 12),
                              Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                  namedValues=NamedValues(("stm1", 1), ("stm16", 2), ))).setMaxAccess("readwrite")
hwCposFrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 13),
                                   Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                       namedValues=NamedValues(("sonet", 1), ("sdh", 2), ))).setMaxAccess("readwrite")
hwCposMultiplex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 14),
                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                     namedValues=NamedValues(("au3", 1), ("au4", 2), ))).setMaxAccess("readwrite")
hwCposLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 15),
                                Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                    namedValues=NamedValues(("otherloop", 1), ("stopLoopback", 2), ("local", 3),
                                                            ("remote", 4), ))).setMaxAccess("readwrite")
hwCposFlagJ0Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 21),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                      namedValues=NamedValues(("j01ByteMode", 1), ("j016ByteMode", 2),
                                                              ("j064ByteOrNullMode", 3), ("peer", 4), ))).setMaxAccess(
    "readwrite")
hwCposFlagJ0Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 22),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess(
    "readwrite")
hwCposFlagJ0Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 23),
                                   OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwCposFlagJ1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 24),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                      namedValues=NamedValues(("j11ByteMode", 1), ("j116ByteMode", 2),
                                                              ("j164ByteOrNullMode", 3), ("peer", 4), ))).setMaxAccess(
    "readwrite")
hwCposFlagJ1Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 25),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess(
    "readwrite")
hwCposFlagJ1Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 26),
                                   OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readwrite")
hwCposFlagC2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 27),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readwrite")
hwCposB1SdAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 28),
                                          Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                              6)).setMaxAccess("readwrite")
hwCposB1ExcAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 29),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                               3)).setMaxAccess("readwrite")
hwCposB2SdAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 30),
                                          Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                              6)).setMaxAccess("readwrite")
hwCposB2ExcAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 31),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                               3)).setMaxAccess("readwrite")
hwCposB3SdAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 32),
                                          Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                              6)).setMaxAccess("readwrite")
hwCposB3ExcAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 33),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                               3)).setMaxAccess("readwrite")
hwCposLpBipSdAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 34),
                                             Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                                 6)).setMaxAccess("readwrite")
hwCposLpBipExcAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 35),
                                              Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)).clone(
                                                  3)).setMaxAccess("readwrite")
hwCposHighPathNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 36),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readonly")
hwCposLowPathNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 37),
                                     Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess(
    "readonly")
hwCposMappingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 1, 1, 38),
                                   Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                       namedValues=NamedValues(("h-mode", 1), ("l-mode", 2),
                                                               ("a-mode", 3), ))).setMaxAccess("readwrite")
hwPortPhysicalHpIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 2), Integer32()).setMaxAccess(
    "accessiblefornotify")
hwPortPhysicalLpIndex = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 3), Integer32()).setMaxAccess(
    "accessiblefornotify")
hwCposLpTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4), )
hwCposLpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwCposLpIfIndex"), (0, "HUAWEI-PORT-MIB", "hwCposLpId"))
hwCposLpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1, 1), InterfaceIndex())
hwCposLpId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1, 2), Integer32())

hwCposFlagJ2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1, 3),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("j21ByteMode", 1), ("j216ByteMode", 2), ))).setMaxAccess(
    "readwrite")

hwCposFlagJ2Value = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1, 4),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess(
    "readwrite")
hwCposFlagJ2Trace = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 3, 4, 1, 5),
                                   OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess(
    "readwrite")
hwDs0ChannelBundle = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4))
hwDs0ChannelBundleTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1), )
hwDs0ChannelBundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleParentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleDs1ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs0ChannelBundleId"))
hwDs0ChannelBundleParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 1), InterfaceIndex())
hwDs0ChannelBundleDs1ChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 2), Integer32())
hwDs0ChannelBundleId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 3),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30)))
hwDs0ChannelBundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 11),
                                           InterfaceIndex()).setMaxAccess("readcreate")
hwDs0ChannelBundleTimeSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 12),
                                             OctetString().subtype(
                                                 subtypeSpec=ValueSizeConstraint(0, 61))).setMaxAccess("readcreate")

hwDs0ChannelBundleSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 13),
                                         Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                             namedValues=NamedValues(("s56", 1), ("s64", 2), )).clone(2)).setUnits(
    'kilo bytes').setMaxAccess("readcreate")

hwDs0ChannelBundleTimeSlot0 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 14),
                                             TruthValue()).setMaxAccess("readcreate")
hwDs0ChannelBundleIsMasterPW = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 15),
                                              Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, )).clone(
                                                  namedValues=NamedValues(("notacrpw", 0), ("masterpw", 1),
                                                                          ("notmasterpw", 2), ))).setMaxAccess(
    "readonly")
hwDs0ChannelBundleMasterPWStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 16),
                                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                      namedValues=NamedValues(("unlock", 0),
                                                                              ("lock", 1), ))).setMaxAccess("readonly")
hwDs0ChannelBundlePortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 17),
                                            OctetString()).setMaxAccess("readonly")
hwDs0ChannelBundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 4, 1, 1, 51),
                                             RowStatus()).setMaxAccess("readcreate")
hwDs1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5))
hwDs1Table = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1), )
hwDs1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs1ParentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwDs1ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs1IfIndex"))
hwDs1ParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 1), InterfaceIndex())
hwDs1ChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 2),
                                Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
hwDs1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 3), InterfaceIndex())
hwDs1ChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 11),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("t1", 1), ("e1", 2), ))).setMaxAccess("readcreate")
hwDs1IfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 12),
                             Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 255, )).clone(
                                 namedValues=NamedValues(("e3", 1), ("t3", 2), ("cpos", 3), ("atm", 4),
                                                         ("none", 255), )).clone('none')).setMaxAccess("readcreate")
hwDs1Channelized = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 13),
                                  TruthValue().clone('true')).setMaxAccess("readcreate")
hwDs1CodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 14),
                               Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 255, )).clone(
                                   namedValues=NamedValues(("ami", 1), ("hdb3", 2), ("b8zs", 3),
                                                           ("none", 255), )).clone('hdb3')).setMaxAccess("readcreate")
hwDs1Clock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 15),
                            Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                namedValues=NamedValues(("master", 1), ("slave", 2), ))).setMaxAccess("readcreate")
hwDs1FrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 16),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                      namedValues=NamedValues(("esf", 1), ("sf", 2), ("noCrc4", 3),
                                                              ("crc", 4), ))).setMaxAccess("readcreate")
hwDs1Cable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 17),
                            Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 255, )).clone(
                                namedValues=NamedValues(("long", 1), ("short", 2), ("none", 255), )).clone(
                                'short')).setMaxAccess("readcreate")
hwDs1Loopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 18),
                               Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 255, )).clone(
                                   namedValues=NamedValues(("local", 1), ("remote", 2), ("payload", 3), ("cell", 4),
                                                           ("none", 255), )).clone('none')).setMaxAccess("readcreate")
hwDs1ClockRecoveryDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 19),
                                          Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess(
    "readcreate")
hwDs1PWClockDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 20),
                                    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess(
    "readcreate")
hwDs1WorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 21),
                               Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readonly")
hwDs1EsAlarmTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 22),
                                              Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900)).clone(
                                                  65)).setMaxAccess("readwrite")
hwDs1EsAlarmResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 23),
                                             Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 900)).clone(
                                                 30)).setMaxAccess("readwrite")
hwDs1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 51), RowStatus()).setMaxAccess(
    "readcreate")
hwDs1Lbo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 52),
                          Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, )).clone(
                              namedValues=NamedValues(("db75", 1), ("db155", 2), ("db225", 3), ("none", 4),
                                                      ("notsupport", 5), ))).setMaxAccess("readcreate")
hwDs1CableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 5, 1, 1, 53),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 255, )).clone(
                                      namedValues=NamedValues(("length133", 1), ("length266", 2), ("length399", 3),
                                                              ("length533", 4), ("length655", 5), ("notsupport", 6),
                                                              ("none", 255), ))).setMaxAccess("readcreate")
hwDs3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6))
hwDs3Table = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1), )
hwDs3Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDs3ParentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwDs3ChannelId"),
    (0, "HUAWEI-PORT-MIB", "hwDs3IfIndex"))
hwDs3ParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 1), InterfaceIndex())
hwDs3ChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 2),
                                Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)))
hwDs3IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 3), InterfaceIndex())
hwDs3ChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 11),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("t3", 1), ("e3", 2), ))).setMaxAccess("readcreate")
hwDs3IfType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 12),
                             Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 255, )).clone(
                                 namedValues=NamedValues(("cpos", 1), ("none", 255), )).clone('none')).setMaxAccess(
    "readcreate")
hwDs3Channelized = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 13),
                                  TruthValue().clone('true')).setMaxAccess("readcreate")
hwDs3Clock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 14),
                            Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                namedValues=NamedValues(("master", 1), ("slave", 2), ))).setMaxAccess("readcreate")
hwDs3FrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 15),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, )).clone(
                                      namedValues=NamedValues(("g832Adm", 1), ("g751Adm", 2), ("g751Plcp", 3),
                                                              ("cbitAdm", 4), ("cbitPlcp", 5), ("m23Adm", 6),
                                                              ("m23Plcp", 7), ))).setMaxAccess("readcreate")
hwDs3Scramble = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 16),
                               TruthValue().clone('false')).setMaxAccess("readcreate")
hwDs3Cable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 17),
                            Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                namedValues=NamedValues(("long", 1), ("short", 2), )).clone('short')).setMaxAccess(
    "readcreate")
hwDs3NationalBit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 18),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                      namedValues=NamedValues(("n0", 1), ("n1", 2), )).clone('n0')).setMaxAccess(
    "readcreate")
hwDs3Loopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 19),
                               Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 255, )).clone(
                                   namedValues=NamedValues(("local", 1), ("remote", 2), ("payload", 3), ("cell", 4),
                                                           ("none", 255), )).clone('none')).setMaxAccess("readcreate")
hwDs3CreateSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 20),
                                   TruthValue().clone('false')).setMaxAccess("readcreate")
hwDs3RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 6, 1, 1, 51), RowStatus()).setMaxAccess(
    "readcreate")
hwBundleSerial = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7))
hwBundleSerialTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1), )
hwBundleSerialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwBundleSerialIfIndex"))
hwBundleSerialIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 1), InterfaceIndex())
hwBundleSerialLinkProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 11), Integer32().subtype(
    subtypeSpec=SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 255, )).clone(
    namedValues=NamedValues(("ietf", 1), ("nonstandard", 2), ("hdlc", 3), ("ppp", 4), ("lapb", 5), ("atm", 6),
                            ("tdm", 7), ("none", 255), ))).setMaxAccess("readwrite")
hwBundleSerialTimerHold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 12),
                                         Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess(
    "readwrite")
hwBundleSerialLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 13),
                                        TruthValue().clone('false')).setMaxAccess("readwrite")
hwBundleSerialCrcVerifyCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 7, 1, 1, 14),
                                             Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                                 namedValues=NamedValues(("crc16", 1), ("crc32", 2), ))).setMaxAccess(
    "readwrite")
hwPhysicalPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8))
hwPhysicalPortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1), )
hwPhysicalPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"))
hwPhysicalPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 1), InterfaceIndex())
hwPhysicalPortDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 2), Unsigned32().subtype(
    subtypeSpec=ValueRangeConstraint(0, 86400000))).setMaxAccess("readwrite")
hwPhysicalPortDelayRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 3),
                                               Unsigned32().subtype(
                                                   subtypeSpec=ValueRangeConstraint(0, 86400000))).setMaxAccess(
    "readonly")
hwPhysicalPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 4), OctetString()).setMaxAccess(
    "readonly")
hwPhysicalPortInChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwPhysicalPortInSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 6), Integer32()).setMaxAccess(
    "readonly")
hwPhysicalPortInCard = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 7), Integer32()).setMaxAccess(
    "readonly")
hwPhysicalPortInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 8), Integer32()).setMaxAccess(
    "readonly")
hwPhysicalAutoShutLaserEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 9), Integer32().subtype(
    subtypeSpec=SingleValueConstraint(1, 2, 255, )).clone(
    namedValues=NamedValues(("enable", 1), ("disable", 2), ("not-support", 255), ))).setMaxAccess("readwrite")
hwPhysicalAutoShutLaserOpenInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 10),
                                                     Integer32().subtype(
                                                         subtypeSpec=ConstraintsUnion(ValueRangeConstraint(100, 300),
                                                                                      ValueRangeConstraint(2147483647,
                                                                                                           2147483647), ))).setMaxAccess(
    "readwrite")
hwPhysicalAutoShutLaserCloseInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 11),
                                                      Integer32().subtype(
                                                          subtypeSpec=ConstraintsUnion(ValueRangeConstraint(200, 30000),
                                                                                       ValueRangeConstraint(2147483647,
                                                                                                            2147483647), ))).setMaxAccess(
    "readwrite")
hwPhysicalAutoShutLaserLongOpenInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 12),
                                                         Integer32().subtype(subtypeSpec=ConstraintsUnion(
                                                             ValueRangeConstraint(200, 30000),
                                                             ValueRangeConstraint(2147483647,
                                                                                  2147483647), ))).setMaxAccess(
    "readwrite")
hwPhysicalLoopbackType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 13),
                                        Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 4, )).clone(
                                            namedValues=NamedValues(("otherLoop", 1), ("stopLoopback", 2), ("local", 3),
                                                                    ("remote", 4), ))).setMaxAccess("readonly")
hwPhysicalShutLaser = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 14),
                                     Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 255, )).clone(
                                         namedValues=NamedValues(("off", 1), ("on", 2),
                                                                 ("not-support", 255), ))).setMaxAccess("readwrite")
hwPhysicalLaserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 15),
                                       Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, 255, )).clone(
                                           namedValues=NamedValues(("off", 1), ("on", 2), ("offline", 3),
                                                                   ("not-support", 255), ))).setMaxAccess("readonly")
hwPhysicalPortHoldUp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 16),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                          namedValues=NamedValues(("disable", 0), ("enable", 1), ))).setMaxAccess(
    "readwrite")
hwPhysicalPortAlarmInverseEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 1, 1, 17),
                                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                                      namedValues=NamedValues(("enable", 1),
                                                                              ("disable", 2), ))).setMaxAccess(
    "readwrite")
hwSDHRsMsPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2), )
hwSDHRsMsPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwSDHRsMsPerfCurrentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwSDHRsMsPerfCurrentDataIndex"))
hwSDHRsMsPerfCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 1), InterfaceIndex())
hwSDHRsMsPerfCurrentDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 2),
                                               Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
hwSDHRsPerfCurrentBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 3), Integer32()).setMaxAccess(
    "readonly")
hwSDHRsPerfCurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 4), Integer32()).setMaxAccess(
    "readonly")
hwSDHRsPerfCurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwSDHRsPerfCurrentUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 6), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 7), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 8), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 9), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 10), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentFEBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 11),
                                         Integer32()).setMaxAccess("readonly")
hwSDHMsPerfCurrentFEES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 12), Integer32()).setMaxAccess(
    "readonly")
hwSDHMsPerfCurrentFESES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 13),
                                         Integer32()).setMaxAccess("readonly")
hwSDHMsPerfCurrentFEUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 2, 1, 14),
                                         Integer32()).setMaxAccess("readonly")
hwSDHHpPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3), )
hwSDHHpPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwSDHHpPerfCurrentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwSDHHpPerfCurrentHpIndex"),
    (0, "HUAWEI-PORT-MIB", "hwSDHHpPerfCurrentDataIndex"))
hwSDHHpPerfCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 1), InterfaceIndex())
hwSDHHpPerfCurrentHpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 2), Integer32())
hwSDHHpPerfCurrentDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 3),
                                             Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
hwSDHHpPerfCurrentBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 4), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 6), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 7), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentFEBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 8), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentFEES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 9), Integer32()).setMaxAccess(
    "readonly")
hwSDHHpPerfCurrentFESES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 10),
                                         Integer32()).setMaxAccess("readonly")
hwSDHHpPerfCurrentFEUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 3, 1, 11),
                                         Integer32()).setMaxAccess("readonly")
hwSDHLpPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4), )
hwSDHLpPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentHpIndex"),
    (0, "HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentLpIndex"), (0, "HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentDataIndex"))
hwSDHLpPerfCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 1), InterfaceIndex())
hwSDHLpPerfCurrentHpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 2), Integer32())
hwSDHLpPerfCurrentLpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 3), Integer32())
hwSDHLpPerfCurrentDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 4),
                                             Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
hwSDHLpPerfCurrentBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 6), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 7), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 8), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentFEBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 9), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentFEES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 10), Integer32()).setMaxAccess(
    "readonly")
hwSDHLpPerfCurrentFESES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 11),
                                         Integer32()).setMaxAccess("readonly")
hwSDHLpPerfCurrentFEUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 4, 1, 12),
                                         Integer32()).setMaxAccess("readonly")
hwPDHPerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5), )
hwPDHPerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPDHPerfCurrentIfIndex"), (0, "HUAWEI-PORT-MIB", "hwPDHPerfCurrentDataIndex"))
hwPDHPerfCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 1), InterfaceIndex())
hwPDHPerfCurrentDataIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 2),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1)))
hwPDHPerfCurrentBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 3), Integer32()).setMaxAccess(
    "readonly")
hwPDHPerfCurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 4), Integer32()).setMaxAccess(
    "readonly")
hwPDHPerfCurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwPDHPerfCurrentUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 5, 1, 6), Integer32()).setMaxAccess(
    "readonly")
hwEthPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 6), )
hwEthPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 6, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwEthPortStatIfIndex"))
hwEthPortStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 6, 1, 1), InterfaceIndex())
hwEthPortStatBadBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 6, 1, 2), Counter64()).setMaxAccess(
    "readonly")
hwPhysicalPortGlobleCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 7))
hwLoopBackAutoClearEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 7, 1),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                          namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess(
    "readwrite")
hwLoopBackAutoClearPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 7, 2),
                                      Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2880))).setUnits(
    'minute').setMaxAccess("readwrite")
hwPortAlarmInverseEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 8, 7, 3),
                                     Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                         namedValues=NamedValues(("enable", 1), ("disable", 2), ))).setMaxAccess(
    "readwrite")
hwDslGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9))
hwDslGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1), )
hwDslGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDslGroupIfIndex"))
hwDslGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 1), InterfaceIndex()).setMaxAccess(
    "readonly")
hwDslGroupWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 2),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                        namedValues=NamedValues(("atm", 1), ("efm", 2), ))).setMaxAccess("readwrite")
hwDslGroupBisState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 3),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                        namedValues=NamedValues(("disable", 1), ("enable", 2),
                                                                ("notSupport", 3), ))).setMaxAccess("readwrite")
hwDslGroupEncapeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 4),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                          namedValues=NamedValues(("eoaLlc", 1), ("eoaVcmux", 2),
                                                                  ("notSupport", 3), ))).setMaxAccess("readwrite")
hwDslGroupEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 5),
                                  Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3, )).clone(
                                      namedValues=NamedValues(("disable", 1), ("enable", 2),
                                                              ("notSupport", 3), ))).setMaxAccess("readwrite")
hwDslGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 1, 1, 60), RowStatus()).setMaxAccess(
    "readwrite")
hwDslGroupBoundVeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2), )
hwDslGroupBoundVeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDslGroupIfIndexOfBound"), (0, "HUAWEI-PORT-MIB", "hwDslGroupPvcId"))
hwDslGroupIfIndexOfBound = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 1),
                                          InterfaceIndex()).setMaxAccess("readonly")
hwVirtualEthernetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 2),
                                          InterfaceIndex()).setMaxAccess("readonly")
hwDslGroupVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 3),
                               Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
hwDslGroupVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 4),
                               Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess(
    "readwrite")
hwDslGroupPvcId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 5),
                                 Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
hwBoundVeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 2, 1, 50), RowStatus()).setMaxAccess(
    "readwrite")
hwDslGroupBindVeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 3), )
hwDslGroupBindVeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 3, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDslGroupInterfaceIndex"), (0, "HUAWEI-PORT-MIB", "hwVirtualEthernetInterfaceIndex"))
hwDslGroupInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 3, 1, 1),
                                          InterfaceIndex()).setMaxAccess("readonly")
hwVirtualEthernetInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 3, 1, 2),
                                                 InterfaceIndex()).setMaxAccess("readonly")
hwBindVeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 9, 3, 1, 50), RowStatus()).setMaxAccess(
    "readwrite")
hwDslGroupIma = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10))
hwDslGroupImaTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1), )
hwDslGroupImaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"))
hwDslGroupImaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 1),
                                      InterfaceIndex()).setMaxAccess("readonly")
hwDslGroupImaVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 2),
                                      Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                          namedValues=NamedValues(("v0", 1), ("v1", 2), ))).setMaxAccess("readwrite")
hwDslGroupImaFrameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 3),
                                       ImaFrameLength()).setMaxAccess("readwrite")
hwDslGroupImaReset = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 4),
                                    Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, )).clone(
                                        namedValues=NamedValues(("disable", 1), ("enable", 2), ))).setMaxAccess(
    "readwrite")
hwDslGroupImaTxMinLinkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 5),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess(
    "readwrite")
hwDslGroupImaRxMinLinkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 6),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess(
    "readwrite")
hwDslGroupImaNeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 7),
                                      ImaGroupState()).setMaxAccess("readonly")
hwDslGroupImaFeState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 8),
                                      ImaGroupState()).setMaxAccess("readonly")
hwDslGroupImaTxCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 9),
                                         Integer32()).setMaxAccess("readonly")
hwDslGroupImaRxCellRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 10),
                                         Integer32()).setMaxAccess("readonly")
hwDslGroupImaTxActLinkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 11),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess(
    "readonly")
hwDslGroupImaRxActLinkNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 12),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess(
    "readonly")
hwDslGroupImaIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 10, 1, 1, 13), OctetString()).setMaxAccess(
    "readonly")
hwDslLink = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11))
hwDslLinkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1), )
hwDslLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), (0, "HUAWEI-PORT-MIB", "hwDslLinkIfIndex"))
hwBoundDslGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1, 1),
                                        InterfaceIndex()).setMaxAccess("readonly")
hwDslLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1, 2), InterfaceIndex()).setMaxAccess(
    "readwrite")
hwDslLinkIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1, 4), OctetString()).setMaxAccess(
    "readonly")
hwBoundDslGroupIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1, 5),
                                       OctetString()).setMaxAccess("readonly")
hwDslLinkBoundRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 11, 1, 1, 50),
                                         RowStatus()).setMaxAccess("readwrite")
hwPWAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12))
hwPWAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1), )
hwPWAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPWAlarmIfIndex"))
hwPWAlarmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 1), InterfaceIndex())
hwPWCesVcID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
hwPWCesVcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 3), Integer32()).setMaxAccess(
    "readonly")
hwPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 4), IpAddress()).setMaxAccess(
    "readonly")
hwAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 5), Integer32()).setMaxAccess(
    "readonly")
hwPWAlarmRMLEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 6),
                                          EnabledStatus()).setMaxAccess("readwrite")
hwLosAlarmTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 7),
                                            Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 65535)).clone(
                                                100)).setMaxAccess("readwrite")
hwLosAlarmResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 8),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535)).clone(
                                               100)).setMaxAccess("readwrite")
hwPWPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 9), OctetString()).setMaxAccess(
    "readonly")
hwLosPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 10),
                                             Integer32()).setMaxAccess("readwrite")
hwLosPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 11),
                                            Integer32()).setMaxAccess("readwrite")
hwMisorderPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 12),
                                                  Integer32()).setMaxAccess("readwrite")
hwMisorderPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 13),
                                                 Integer32()).setMaxAccess("readwrite")
hwStrayPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 14),
                                               Integer32()).setMaxAccess("readwrite")
hwStrayPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 15),
                                              Integer32()).setMaxAccess("readwrite")
hwMalPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 16),
                                             Integer32()).setMaxAccess("readwrite")
hwMalPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 17),
                                            Integer32()).setMaxAccess("readwrite")
hwJtrUdrExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 18),
                                             Integer32()).setMaxAccess("readwrite")
hwJtrUdrExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 19),
                                            Integer32()).setMaxAccess("readwrite")
hwJtrOvrExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 20),
                                             Integer32()).setMaxAccess("readwrite")
hwJtrOvrExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 1, 1, 21),
                                            Integer32()).setMaxAccess("readwrite")
hwAtmPWAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2), )
hwAtmPWAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwAtmPWAlarmIfIndex"))
hwAtmPWAlarmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 1),
                                     InterfaceIndex()).setMaxAccess("readonly")
hwAtmVcID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 2), Integer32()).setMaxAccess("readonly")
hwAtmVcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 3), Integer32()).setMaxAccess("readonly")
hwAtmPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 4), IpAddress()).setMaxAccess(
    "readonly")
hwAtmPWPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 5), OctetString()).setMaxAccess(
    "readonly")
hwAtmLosPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 6),
                                                Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                    100)).setMaxAccess("readwrite")
hwAtmLosPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 7),
                                               Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                   1)).setMaxAccess("readwrite")
hwAtmMisorderPktExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 8),
                                                     Integer32().subtype(
                                                         subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                         100)).setMaxAccess("readwrite")
hwAtmMisorderPktExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 9),
                                                    Integer32().subtype(
                                                        subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                        1)).setMaxAccess("readwrite")
hwAtmUnknownCellExcTriggerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 10),
                                                     Integer32().subtype(
                                                         subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                         100)).setMaxAccess("readwrite")
hwAtmUnknownCellExcResumeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 12, 2, 1, 11),
                                                    Integer32().subtype(
                                                        subtypeSpec=ValueRangeConstraint(1, 1000)).clone(
                                                        1)).setMaxAccess("readwrite")
hwSNMPTrapEn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13))
hwSNMPTrapEnTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1), )
hwSNMPTrapEnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwSNMPTrapEnIfIndex"))
hwSNMPTrapEnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 1), InterfaceIndex())
hwCesPWLopsEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 2), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWRemoteLosPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 3), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWOppositeRAIEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 4), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWOppositeAcfaultEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 5),
                                          Integer32()).setMaxAccess("readwrite")
hwCesPWLosPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 6), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWMisorderPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 7), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWStrayPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 8), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWMalPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 9), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWJtrUnrEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 10), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWJtrOvrEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 11), Integer32()).setMaxAccess(
    "readwrite")
hwCesPWAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 12), Integer32()).setMaxAccess(
    "readwrite")
hwPhysicalPortLosAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 13),
                                          Integer32()).setMaxAccess("readwrite")
hwPhysicalPortLofAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 14),
                                          Integer32()).setMaxAccess("readwrite")
hwRsOofAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 15), Integer32()).setMaxAccess(
    "readwrite")
hwRsB1ExcAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 16), Integer32()).setMaxAccess(
    "readwrite")
hwRsB1SdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 17), Integer32()).setMaxAccess(
    "readwrite")
hwRsJ0TimAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 18), Integer32()).setMaxAccess(
    "readwrite")
hwMsRdiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 19), Integer32()).setMaxAccess(
    "readwrite")
hwMsB2ExcAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 20), Integer32()).setMaxAccess(
    "readwrite")
hwMsAuLopAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 21), Integer32()).setMaxAccess(
    "readwrite")
hwMsAisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 22), Integer32()).setMaxAccess(
    "readwrite")
hwMsB2SdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 23), Integer32()).setMaxAccess(
    "readwrite")
hwHpJ1TimAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 24), Integer32()).setMaxAccess(
    "readwrite")
hwHpUneqAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 25), Integer32()).setMaxAccess(
    "readwrite")
hwHpRdiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 26), Integer32()).setMaxAccess(
    "readwrite")
hwHpB3ExcAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 27), Integer32()).setMaxAccess(
    "readwrite")
hwHpPlmAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 28), Integer32()).setMaxAccess(
    "readwrite")
hwHpB3SdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 29), Integer32()).setMaxAccess(
    "readwrite")
hwHpAuAisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 30), Integer32()).setMaxAccess(
    "readwrite")
hwLpTuLopAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 31), Integer32()).setMaxAccess(
    "readwrite")
hwHpTuLomAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 32), Integer32()).setMaxAccess(
    "readwrite")
hwLpTimAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 33), Integer32()).setMaxAccess(
    "readwrite")
hwLpUneqAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 34), Integer32()).setMaxAccess(
    "readwrite")
hwLpRdiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 35), Integer32()).setMaxAccess(
    "readwrite")
hwLpBipExcAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 36), Integer32()).setMaxAccess(
    "readwrite")
hwLpBipSdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 37), Integer32()).setMaxAccess(
    "readwrite")
hwLpPlmAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 38), Integer32()).setMaxAccess(
    "readwrite")
hwLpTuAisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 39), Integer32()).setMaxAccess(
    "readwrite")
hwDs1EsExcAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 40), Integer32()).setMaxAccess(
    "readwrite")
hwDs1RmfaAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 41), Integer32()).setMaxAccess(
    "readwrite")
hwDs1LmfaAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 42), Integer32()).setMaxAccess(
    "readwrite")
hwDs1AisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 43), Integer32()).setMaxAccess(
    "readwrite")
hwDs1RdiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 44), Integer32()).setMaxAccess(
    "readwrite")
hwRsLocAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 45), Integer32()).setMaxAccess(
    "readwrite")
hwLpRfiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 46), Integer32()).setMaxAccess(
    "readwrite")
hwLpV5VcaisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 47), Integer32()).setMaxAccess(
    "readwrite")
hwVc12oofAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 48), Integer32()).setMaxAccess(
    "readwrite")
hwVc12AlmE1RaiAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 49), Integer32()).setMaxAccess(
    "readwrite")
hwVc12LfaAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 50), Integer32()).setMaxAccess(
    "readwrite")
hwVc12UpE1AisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 51), Integer32()).setMaxAccess(
    "readwrite")
hwVc12DownE1AisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 52),
                                        Integer32()).setMaxAccess("readwrite")
hwDs1DownE1AisAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 53), Integer32()).setMaxAccess(
    "readwrite")
hwMsLpsUniBiMAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 54), Integer32()).setMaxAccess(
    "readwrite")
hwMsK1K2MAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 55), Integer32()).setMaxAccess(
    "readwrite")
hwMsK2MAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 56), Integer32()).setMaxAccess(
    "readwrite")
hwVc12LmfaAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 57), Integer32()).setMaxAccess(
    "readwrite")
hwSDHAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 58), Integer32()).setMaxAccess(
    "readwrite")
hwLaserShutAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 59), Integer32()).setMaxAccess(
    "readwrite")
hwLaserAutoShutAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 60),
                                        Integer32()).setMaxAccess("readwrite")
hwLaserAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 61), Integer32()).setMaxAccess(
    "readwrite")
hwLoopbackAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 62), Integer32()).setMaxAccess(
    "readwrite")
hwChannelLoopbackAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 63),
                                          Integer32()).setMaxAccess("readwrite")
hwLoopbackAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 64), Integer32()).setMaxAccess(
    "readwrite")
hwAtmOcdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 65), Integer32()).setMaxAccess(
    "readwrite")
hwAtmLcdAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 66), Integer32()).setMaxAccess(
    "readwrite")
hwAtmUhcsAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 67), Integer32()).setMaxAccess(
    "readwrite")
hwAtmChcsAlarmEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 68), Integer32()).setMaxAccess(
    "readwrite")
hwAtmPWLosPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 69), Integer32()).setMaxAccess(
    "readwrite")
hwAtmPWMisorderPktEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 70), Integer32()).setMaxAccess(
    "readwrite")
hwAtmPWUnknownCellEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 71), Integer32()).setMaxAccess(
    "readwrite")
hwAtmAllEn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 13, 1, 1, 72), Integer32()).setMaxAccess(
    "readwrite")
hwPortAlarmThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14))
hwPortAlarmThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1), )
hwPortAlarmThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"))
hwPhysicalPortThrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 1), InterfaceIndex())
hwPhysicalPortThrName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 2),
                                       OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readonly")
hwPhysicalPortCrcErrorStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 3),
                                                  Counter64()).setMaxAccess("readonly")
hwPhysicalPortCrcErrorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 4),
                                                     Unsigned32().subtype(
                                                         subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortCrcErrorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 5),
                                                    Unsigned32().subtype(
                                                        subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortCrcErrorInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 6),
                                                Unsigned32().subtype(
                                                    subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess(
    "readwrite")
hwPhysicalPortSymbolErrorStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 7),
                                                     Counter64()).setMaxAccess("readonly")
hwPhysicalPortSymbolErrorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 8),
                                                        Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                              4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortSymbolErrorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 9),
                                                       Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                             4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortSymbolErrorInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 10),
                                                   Unsigned32().subtype(
                                                       subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess(
    "readwrite")
hwPhysicalPortInputErrorStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 11),
                                                    Counter64()).setMaxAccess("readonly")
hwPhysicalPortInputErrorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 12),
                                                       Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                             4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortInputErrorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 13),
                                                      Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                            4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortInputErrorInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 14),
                                                  Unsigned32().subtype(
                                                      subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess(
    "readwrite")
hwPhysicalPortOutputErrorStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 15),
                                                     Counter64()).setMaxAccess("readonly")
hwPhysicalPortOutputErrorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 16),
                                                        Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                              4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortOutputErrorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 17),
                                                       Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1,
                                                                                                             4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortOutputErrorInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 18),
                                                   Unsigned32().subtype(
                                                       subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess(
    "readwrite")
hwPhysicalPortSdhErrorStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 19),
                                                  Counter64()).setMaxAccess("readonly")
hwPhysicalPortSdhErrorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 20),
                                                     Unsigned32().subtype(
                                                         subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortSdhErrorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 21),
                                                    Unsigned32().subtype(
                                                        subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess(
    "readwrite")
hwPhysicalPortSdhErrorInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 22),
                                                Unsigned32().subtype(
                                                    subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess(
    "readwrite")
hwPhysicalPortBIP8SDErrorThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 23),
                                                    Unsigned32().subtype(
                                                        subtypeSpec=ValueRangeConstraint(6, 9))).setMaxAccess(
    "readwrite")
hwPhysicalPortCrcPerAlarmThresholdCoefficient = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 24),
                                                               Unsigned32()).setMaxAccess("readwrite")
hwPhysicalPortCrcPerAlarmThresholdPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 25),
                                                         Unsigned32()).setMaxAccess("readwrite")
hwPhysicalPortCrcPerResumeThresholdCoefficient = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 26),
                                                                Unsigned32()).setMaxAccess("readwrite")
hwPhysicalPortCrcPerResumeThresholdPower = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 27),
                                                          Unsigned32()).setMaxAccess("readwrite")
hwPhysicalPortCrcPerTriggerLsp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 28),
                                                Unsigned32()).setMaxAccess("readwrite")
hwPhysicalPortCrcPerCurrentValueString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 29),
                                                        OctetString()).setMaxAccess("accessiblefornotify")
hwPhysicalPortCrcPerAlarmThresholdString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 30),
                                                          OctetString()).setMaxAccess("accessiblefornotify")
hwPhysicalPortCrcPerResumeThresholdString = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 14, 1, 1, 31),
                                                           OctetString()).setMaxAccess("accessiblefornotify")
hwPortAlarmDownEnable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15))
hwPortAlarmDownEnableTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1), )
hwPortAlarmDownEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1), ).setIndexNames(
    (0, "HUAWEI-PORT-MIB", "hwPhysicalPortDownIfIndex"))
hwPhysicalPortDownIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 1), InterfaceIndex())
hwPhysicalPortDownName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 2),
                                        OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess(
    "readonly")
hwPhysicalPortCrcEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 3),
                                              Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                  namedValues=NamedValues(("disable", 0),
                                                                          ("enable", 1), ))).setMaxAccess("readwrite")
hwPhysicalPortSymbolEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 4),
                                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                     namedValues=NamedValues(("disable", 0),
                                                                             ("enable", 1), ))).setMaxAccess(
    "readwrite")
hwPhysicalPortInputEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 5),
                                                Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                    namedValues=NamedValues(("disable", 0),
                                                                            ("enable", 1), ))).setMaxAccess("readwrite")
hwPhysicalPortOutputEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 6),
                                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                     namedValues=NamedValues(("disable", 0),
                                                                             ("enable", 1), ))).setMaxAccess(
    "readwrite")
hwPhysicalPortSdhEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 7),
                                              Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                  namedValues=NamedValues(("disable", 0),
                                                                          ("enable", 1), ))).setMaxAccess("readwrite")
hwPhysicalPortBip8SdEnabledDown = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 1, 15, 1, 1, 8),
                                                 Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, )).clone(
                                                     namedValues=NamedValues(("disable", 0),
                                                                             ("enable", 1), ))).setMaxAccess(
    "readwrite")
hwPortNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2))
hwPortACRMasterPWChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleParentIfIndex"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleDs1ChannelId"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleId"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundlePortName"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleIsMasterPW"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleMasterPWStatus"),))
hwDslImaGroupTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 2))
hwDslImaGroupLEDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 2, 1)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"),))
hwDslImaGroupLEUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 2, 2)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"),))
hwDslImaGroupREDown = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 2, 3)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"),))
hwDslImaGroupREUp = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 2, 4)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"),))
hwDslImaLinkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3))
hwDslImaLinkLif = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkLifResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 2)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkLods = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 3)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkLodsResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 4)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkRfi = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 5)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkRfiResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 6)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkReTxUnusable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 7)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkReTxUsable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 8)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkReRxUnusable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 9)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslImaLinkReRxUsable = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 3, 10)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslLinkTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 4))
hwDslLinkFrameLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 4, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslLinkFrameResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 4, 2)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslLinkSignalLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 4, 3)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwDslLinkSignalResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 4, 4)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfName"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),))
hwCesPwRemoteLosPktAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 5)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesPwRemoteLosPktAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 6)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesPwOppositeRai = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 7)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesPwOppositeRaiResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 8)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwLosAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 9)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLosAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 10)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLofAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 11)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLofAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 12)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwOofAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 13)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwOofAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 14)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwB1TcaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 15)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwB1TcaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 16)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwB2TcaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 17)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwB2TcaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 18)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwJ0TimAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 19)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwJ0TimAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 20)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLrdiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 21)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLrdiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 22)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwSfbereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 23)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwSfbereAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 24)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwAuLopAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 25)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwAuLopAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 26)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLaisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 27)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLaisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 28)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwSdbereAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 29)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwSdbereAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 30)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwPtimAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 31)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPtimAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 32)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPuneqAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 33)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPuneqAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 34)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPrdiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 35)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPrdiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 36)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwB3TcaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 37)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwB3TcaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 38)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPplmAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 39)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPplmAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 40)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPaisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 41)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwPaisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 42)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwAuAisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 43)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwAuAisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 44)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwVlopAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 45)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwVlopAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 46)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLomAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 47)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwLomAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 48)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),))
hwLpTimVc12Alarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 49)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLpTimVc12AlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 50)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLpUneqVc12Alarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 51)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLpUneqVc12AlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 52)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwVrdiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 53)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwVrdiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 54)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwBip2TcaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 57)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwBip2TcaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 58)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLpSlmVc12Alarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 59)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLpSlmVc12AlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 60)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwTuAisVc12Alarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 61)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwTuAisVc12AlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 62)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwE1EsTcaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 63)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1EsTcaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 64)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1LmfaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 67)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1LmfaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 68)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1UpE1AisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 69)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1UpE1AisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 70)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1AlmE1RaiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 71)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1AlmE1RaiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 72)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwCesPwOppositeAcFault = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 73)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesPwOppositeAcFaultResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 74)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesLosPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 75)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesLosPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 76)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesMisorderPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 77)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesMisorderPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 78)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesStrayPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 79)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesStrayPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 80)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesMalPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 81)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesMalPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 82)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesJtrUdrExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 83)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesJtrUdrExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 84)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesJtrOvrExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 85)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesJtrOvrExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 86)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwRroolAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 87)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwRroolAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 88)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwVrfiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 89)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwVrfiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 90)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwV5VcaisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 91)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwV5VcaisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 92)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1AlmE1RaiAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 95)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1AlmE1RaiAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 96)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1LfaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 97)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1LfaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 98)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1UpE1AisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 99)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1UpE1AisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 100)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1DownE1AisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 101)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1DownE1AisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 102)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwE1DownE1AisAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 103)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwE1DownE1AisAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 104)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwCposE1LmfaAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 111)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwCposE1LmfaAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 112)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPortPhysicalLpIndex"),))
hwLaserShutAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 113)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLaserShutAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 114)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLaserAutoShutAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 115)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLaserAutoShutAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 116)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLoopbackAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 117)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),
("HUAWEI-PORT-MIB", "hwPhysicalLoopbackType"),))
hwLoopbackAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 118)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),
("HUAWEI-PORT-MIB", "hwPhysicalLoopbackType"),))
hwOcdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 119)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwOcdAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 120)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLcdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 121)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwLcdAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 122)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwUhcsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 123)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwUhcsAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 124)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwChcsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 125)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwChcsAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 126)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwChannelLoopbackAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 127)).setObjects(*(
("HUAWEI-PORT-MIB", "hwSDHHpPerfCurrentIfIndex"), ("HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentIfIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalLoopbackType"), ("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwChannelLoopbackAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 128)).setObjects(*(
("HUAWEI-PORT-MIB", "hwSDHHpPerfCurrentIfIndex"), ("HUAWEI-PORT-MIB", "hwSDHLpPerfCurrentIfIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalLoopbackType"), ("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwCesLopsAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 129)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwCesLopsAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 130)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPWCesVcID"), ("HUAWEI-PORT-MIB", "hwPWCesVcType"), ("HUAWEI-PORT-MIB", "hwPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwPWPortName"),))
hwAtmPwLosPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 131)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwAtmPwLosPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 132)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwAtmPwMisorderPktExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 133)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwAtmPwMisorderPktExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 134)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwAtmPwUnknownCellExcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 135)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwAtmPwUnknownCellExcAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 136)).setObjects(*(
("HUAWEI-PORT-MIB", "hwAtmVcID"), ("HUAWEI-PORT-MIB", "hwAtmVcType"), ("HUAWEI-PORT-MIB", "hwAtmPeerIpAddr"),
("HUAWEI-PORT-MIB", "hwAtmPWPortName"),))
hwInputErrorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 153)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwInputErrorAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 154)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwOutputErrorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 155)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwOutputErrorAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 156)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwPortAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157))
hwPhysicalPortCrcError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorInterval"),))
hwPhysicalPortCrcErrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 2)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorInterval"),))
hwPhysicalPortSymbolError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 3)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorStatistics"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorLowThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorInterval"),))
hwPhysicalPortSymbolErrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 4)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorStatistics"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorLowThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorInterval"),))
hwPhysicalPortSdhError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 5)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorInterval"),))
hwPhysicalPortSdhErrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 6)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorInterval"),))
hwPhysicalPortBip8SdError = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 7)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortBIP8SDErrorThreshold"),))
hwPhysicalPortBip8SdErrorResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 8)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortBIP8SDErrorThreshold"),))
hwPhysicalPortCrcPacketErrorRatio = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 9)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerCurrentValueString"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerAlarmThresholdString"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerResumeThresholdString"),))
hwPhysicalPortCrcPacketErrorRatioResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 157, 10)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwPhysicalPortThrIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortThrName"),
      ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerCurrentValueString"),
      ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerAlarmThresholdString"),
      ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcPerResumeThresholdString"),))
hwLoopBackAutoClearNotice = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 160)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwChannelLoopBackAutoClearNotice = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 161)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortIfIndex"), ("HUAWEI-PORT-MIB", "hwPhysicalPortName"),
("HUAWEI-PORT-MIB", "hwDs1ChannelId"),))
hwHpJ1TiuAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 162)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwHpJ1TiuAlarmResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 163)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortInSlot"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInCard"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInPort"), ("HUAWEI-PORT-MIB", "hwPortPhysicalHpIndex"),
("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwPortAlarmInverseAutoRecover = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 2, 164)).setObjects(
    *(("HUAWEI-PORT-MIB", "hwPhysicalPortName"),))
hwPortConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11))
hwPortCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 1))
hwPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 1, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwEthernetObjectGroup"), ("HUAWEI-PORT-MIB", "hwPosObjectGroup"),
("HUAWEI-PORT-MIB", "hwCposObjectGroup"), ("HUAWEI-PORT-MIB", "hwBundleSerialObjectGroup"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleObjectGroup"), ("HUAWEI-PORT-MIB", "hwDs1ObjectGroup"),
("HUAWEI-PORT-MIB", "hwDs3ObjectGroup"), ("HUAWEI-PORT-MIB", "hwPortNotificationsGroup"),
("HUAWEI-PORT-MIB", "hwPortAlarmThresholdObjectGroup"), ("HUAWEI-PORT-MIB", "hwPortAlarmDownEnableObjectGroup"),))
hwPortGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2))
hwEthernetObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 1)).setObjects(*(
("HUAWEI-PORT-MIB", "hwEthernetLoopback"), ("HUAWEI-PORT-MIB", "hwEthernetPortType"),
("HUAWEI-PORT-MIB", "hwEthernetSpeedSet"), ("HUAWEI-PORT-MIB", "hwEthernetDuplex"),
("HUAWEI-PORT-MIB", "hwEthernetNegotiation"), ("HUAWEI-PORT-MIB", "hwEthernetPortTypeOperate"),
("HUAWEI-PORT-MIB", "hwEthernetClock"), ("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Mode"),
("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Value"), ("HUAWEI-PORT-MIB", "hwEthernetFlagJ0Trace"),
("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Mode"), ("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Value"),
("HUAWEI-PORT-MIB", "hwEthernetFlagJ1Trace"), ("HUAWEI-PORT-MIB", "hwEthernetFlagC2Value"),
("HUAWEI-PORT-MIB", "hwEthernetUpHoldTime"), ("HUAWEI-PORT-MIB", "hwEthernetDownHoldTime"),
("HUAWEI-PORT-MIB", "hwEthernetSubinterfaceStatisticEnable"), ("HUAWEI-PORT-MIB", "hwEthernetJumboframeMaxLength"),
("HUAWEI-PORT-MIB", "hwEthernetComboType"), ("HUAWEI-PORT-MIB", "hwEthernetPortMode"),))
hwPosObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 2)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPosLinkProtocol"), ("HUAWEI-PORT-MIB", "hwPosFrameFormat"), ("HUAWEI-PORT-MIB", "hwPosLoopback"),
("HUAWEI-PORT-MIB", "hwPosScramble"), ("HUAWEI-PORT-MIB", "hwPosClock"), ("HUAWEI-PORT-MIB", "hwPosCrcVerifyCode"),
("HUAWEI-PORT-MIB", "hwPosFlagJ0Mode"), ("HUAWEI-PORT-MIB", "hwPosFlagJ0Value"),
("HUAWEI-PORT-MIB", "hwPosFlagJ0Trace"), ("HUAWEI-PORT-MIB", "hwPosFlagJ1Mode"),
("HUAWEI-PORT-MIB", "hwPosFlagJ1Value"), ("HUAWEI-PORT-MIB", "hwPosFlagJ1Trace"),
("HUAWEI-PORT-MIB", "hwPosFlagC2Value"),))
hwCposObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 3)).setObjects(*(
("HUAWEI-PORT-MIB", "hwCposFrameFormat"), ("HUAWEI-PORT-MIB", "hwCposMultiplex"), ("HUAWEI-PORT-MIB", "hwCposClock"),
("HUAWEI-PORT-MIB", "hwCposIfType"), ("HUAWEI-PORT-MIB", "hwCposLoopback"), ("HUAWEI-PORT-MIB", "hwCposFlagJ0Mode"),
("HUAWEI-PORT-MIB", "hwCposFlagJ0Value"), ("HUAWEI-PORT-MIB", "hwCposFlagJ0Trace"),
("HUAWEI-PORT-MIB", "hwCposFlagJ1Mode"), ("HUAWEI-PORT-MIB", "hwCposFlagJ1Value"),
("HUAWEI-PORT-MIB", "hwCposFlagJ1Trace"), ("HUAWEI-PORT-MIB", "hwCposFlagC2Value"),
("HUAWEI-PORT-MIB", "hwCposB1SdAlarmThreshold"), ("HUAWEI-PORT-MIB", "hwCposB1ExcAlarmThreshold"),
("HUAWEI-PORT-MIB", "hwCposB2SdAlarmThreshold"), ("HUAWEI-PORT-MIB", "hwCposB2ExcAlarmThreshold"),
("HUAWEI-PORT-MIB", "hwCposB3SdAlarmThreshold"), ("HUAWEI-PORT-MIB", "hwCposB3ExcAlarmThreshold"),
("HUAWEI-PORT-MIB", "hwCposLpBipSdAlarmThreshold"), ("HUAWEI-PORT-MIB", "hwCposLpBipExcAlarmThreshold"),
("HUAWEI-PORT-MIB", "hwCposHighPathNumber"), ("HUAWEI-PORT-MIB", "hwCposLowPathNumber"),
("HUAWEI-PORT-MIB", "hwCposMappingMode"),))
hwDs0ChannelBundleObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 4)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleIfIndex"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleTimeSlots"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleSpeed"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundleIsMasterPW"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleMasterPWStatus"), ("HUAWEI-PORT-MIB", "hwDs0ChannelBundlePortName"),
("HUAWEI-PORT-MIB", "hwDs0ChannelBundleRowStatus"),))
hwDs1ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 5)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDs1ChannelType"), ("HUAWEI-PORT-MIB", "hwDs1IfType"), ("HUAWEI-PORT-MIB", "hwDs1Channelized"),
("HUAWEI-PORT-MIB", "hwDs1CodeType"), ("HUAWEI-PORT-MIB", "hwDs1Clock"), ("HUAWEI-PORT-MIB", "hwDs1FrameFormat"),
("HUAWEI-PORT-MIB", "hwDs1Cable"), ("HUAWEI-PORT-MIB", "hwDs1Loopback"),
("HUAWEI-PORT-MIB", "hwDs1ClockRecoveryDomain"), ("HUAWEI-PORT-MIB", "hwDs1PWClockDomain"),
("HUAWEI-PORT-MIB", "hwDs1WorkMode"), ("HUAWEI-PORT-MIB", "hwDs1RowStatus"),))
hwDs3ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 6)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDs3ChannelType"), ("HUAWEI-PORT-MIB", "hwDs3IfType"), ("HUAWEI-PORT-MIB", "hwDs3Channelized"),
("HUAWEI-PORT-MIB", "hwDs3Clock"), ("HUAWEI-PORT-MIB", "hwDs3FrameFormat"), ("HUAWEI-PORT-MIB", "hwDs3Scramble"),
("HUAWEI-PORT-MIB", "hwDs3Cable"), ("HUAWEI-PORT-MIB", "hwDs3NationalBit"), ("HUAWEI-PORT-MIB", "hwDs3Loopback"),
("HUAWEI-PORT-MIB", "hwDs3CreateSerial"), ("HUAWEI-PORT-MIB", "hwDs3RowStatus"),))
hwBundleSerialObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 7)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBundleSerialLinkProtocol"), ("HUAWEI-PORT-MIB", "hwBundleSerialTimerHold"),
("HUAWEI-PORT-MIB", "hwBundleSerialCrcVerifyCode"), ("HUAWEI-PORT-MIB", "hwBundleSerialLoopback"),))
hwPortNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 8)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPortACRMasterPWChange"), ("HUAWEI-PORT-MIB", "hwHpJ1TiuAlarm"),
("HUAWEI-PORT-MIB", "hwHpJ1TiuAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesPwOppositeAcFault"),
("HUAWEI-PORT-MIB", "hwCesPwOppositeAcFaultResume"), ("HUAWEI-PORT-MIB", "hwCesLosPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesLosPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesMisorderPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesMisorderPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesStrayPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesStrayPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesMalPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesMalPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesJtrUdrExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesJtrUdrExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesJtrOvrExcAlarm"),
("HUAWEI-PORT-MIB", "hwCesJtrOvrExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwLaserShutAlarm"),
("HUAWEI-PORT-MIB", "hwLaserShutAlarmResume"), ("HUAWEI-PORT-MIB", "hwLaserAutoShutAlarm"),
("HUAWEI-PORT-MIB", "hwLaserAutoShutAlarmResume"), ("HUAWEI-PORT-MIB", "hwLoopbackAlarm"),
("HUAWEI-PORT-MIB", "hwLoopbackAlarmResume"), ("HUAWEI-PORT-MIB", "hwChannelLoopbackAlarm"),
("HUAWEI-PORT-MIB", "hwChannelLoopbackAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesPwOppositeRaiResume"),
("HUAWEI-PORT-MIB", "hwCesPwOppositeRai"), ("HUAWEI-PORT-MIB", "hwB1TcaAlarm"),
("HUAWEI-PORT-MIB", "hwB1TcaAlarmResume"), ("HUAWEI-PORT-MIB", "hwB2TcaAlarm"),
("HUAWEI-PORT-MIB", "hwB2TcaAlarmResume"), ("HUAWEI-PORT-MIB", "hwOofAlarm"), ("HUAWEI-PORT-MIB", "hwOofAlarmResume"),
("HUAWEI-PORT-MIB", "hwLosAlarm"), ("HUAWEI-PORT-MIB", "hwLosAlarmResume"), ("HUAWEI-PORT-MIB", "hwJ0TimAlarm"),
("HUAWEI-PORT-MIB", "hwJ0TimAlarmResume"), ("HUAWEI-PORT-MIB", "hwLrdiAlarm"), ("HUAWEI-PORT-MIB", "hwLrdiAlarmResume"),
("HUAWEI-PORT-MIB", "hwSfbereAlarm"), ("HUAWEI-PORT-MIB", "hwSfbereAlarmResume"), ("HUAWEI-PORT-MIB", "hwAuLopAlarm"),
("HUAWEI-PORT-MIB", "hwAuLopAlarmResume"), ("HUAWEI-PORT-MIB", "hwLaisAlarm"), ("HUAWEI-PORT-MIB", "hwLaisAlarmResume"),
("HUAWEI-PORT-MIB", "hwSdbereAlarm"), ("HUAWEI-PORT-MIB", "hwSdbereAlarmResume"), ("HUAWEI-PORT-MIB", "hwPtimAlarm"),
("HUAWEI-PORT-MIB", "hwPtimAlarmResume"), ("HUAWEI-PORT-MIB", "hwPuneqAlarm"),
("HUAWEI-PORT-MIB", "hwPuneqAlarmResume"), ("HUAWEI-PORT-MIB", "hwPrdiAlarm"), ("HUAWEI-PORT-MIB", "hwPrdiAlarmResume"),
("HUAWEI-PORT-MIB", "hwB3TcaAlarm"), ("HUAWEI-PORT-MIB", "hwB3TcaAlarmResume"), ("HUAWEI-PORT-MIB", "hwPplmAlarm"),
("HUAWEI-PORT-MIB", "hwPplmAlarmResume"), ("HUAWEI-PORT-MIB", "hwPaisAlarm"), ("HUAWEI-PORT-MIB", "hwPaisAlarmResume"),
("HUAWEI-PORT-MIB", "hwAuAisAlarm"), ("HUAWEI-PORT-MIB", "hwAuAisAlarmResume"), ("HUAWEI-PORT-MIB", "hwVlopAlarm"),
("HUAWEI-PORT-MIB", "hwVlopAlarmResume"), ("HUAWEI-PORT-MIB", "hwLomAlarm"), ("HUAWEI-PORT-MIB", "hwLomAlarmResume"),
("HUAWEI-PORT-MIB", "hwLpTimVc12Alarm"), ("HUAWEI-PORT-MIB", "hwLpTimVc12AlarmResume"),
("HUAWEI-PORT-MIB", "hwLofAlarm"), ("HUAWEI-PORT-MIB", "hwLofAlarmResume"),
("HUAWEI-PORT-MIB", "hwCesPwRemoteLosPktAlarm"), ("HUAWEI-PORT-MIB", "hwCesPwRemoteLosPktAlarmResume"),
("HUAWEI-PORT-MIB", "hwLpUneqVc12Alarm"), ("HUAWEI-PORT-MIB", "hwLpUneqVc12AlarmResume"),
("HUAWEI-PORT-MIB", "hwVrdiAlarm"), ("HUAWEI-PORT-MIB", "hwVrdiAlarmResume"), ("HUAWEI-PORT-MIB", "hwBip2TcaAlarm"),
("HUAWEI-PORT-MIB", "hwBip2TcaAlarmResume"), ("HUAWEI-PORT-MIB", "hwLpSlmVc12Alarm"),
("HUAWEI-PORT-MIB", "hwLpSlmVc12AlarmResume"), ("HUAWEI-PORT-MIB", "hwTuAisVc12Alarm"),
("HUAWEI-PORT-MIB", "hwTuAisVc12AlarmResume"), ("HUAWEI-PORT-MIB", "hwE1EsTcaAlarm"),
("HUAWEI-PORT-MIB", "hwE1EsTcaAlarmResume"), ("HUAWEI-PORT-MIB", "hwE1LmfaAlarm"),
("HUAWEI-PORT-MIB", "hwE1LmfaAlarmResume"), ("HUAWEI-PORT-MIB", "hwE1UpE1AisAlarm"),
("HUAWEI-PORT-MIB", "hwE1UpE1AisAlarmResume"), ("HUAWEI-PORT-MIB", "hwE1AlmE1RaiAlarm"),
("HUAWEI-PORT-MIB", "hwE1AlmE1RaiAlarmResume"), ("HUAWEI-PORT-MIB", "hwRroolAlarm"),
("HUAWEI-PORT-MIB", "hwRroolAlarmResume"), ("HUAWEI-PORT-MIB", "hwVrfiAlarm"), ("HUAWEI-PORT-MIB", "hwVrfiAlarmResume"),
("HUAWEI-PORT-MIB", "hwV5VcaisAlarm"), ("HUAWEI-PORT-MIB", "hwV5VcaisAlarmResume"),
("HUAWEI-PORT-MIB", "hwCposE1AlmE1RaiAlarm"), ("HUAWEI-PORT-MIB", "hwCposE1AlmE1RaiAlarmResume"),
("HUAWEI-PORT-MIB", "hwCposE1LfaAlarm"), ("HUAWEI-PORT-MIB", "hwCposE1LfaAlarmResume"),
("HUAWEI-PORT-MIB", "hwCposE1UpE1AisAlarm"), ("HUAWEI-PORT-MIB", "hwCposE1UpE1AisAlarmResume"),
("HUAWEI-PORT-MIB", "hwCposE1DownE1AisAlarm"), ("HUAWEI-PORT-MIB", "hwCposE1DownE1AisAlarmResume"),
("HUAWEI-PORT-MIB", "hwE1DownE1AisAlarm"), ("HUAWEI-PORT-MIB", "hwE1DownE1AisAlarmResume"),
("HUAWEI-PORT-MIB", "hwCposE1LmfaAlarm"), ("HUAWEI-PORT-MIB", "hwCposE1LmfaAlarmResume"),
("HUAWEI-PORT-MIB", "hwOcdAlarm"), ("HUAWEI-PORT-MIB", "hwOcdAlarmResume"), ("HUAWEI-PORT-MIB", "hwLcdAlarm"),
("HUAWEI-PORT-MIB", "hwLcdAlarmResume"), ("HUAWEI-PORT-MIB", "hwUhcsAlarm"), ("HUAWEI-PORT-MIB", "hwUhcsAlarmResume"),
("HUAWEI-PORT-MIB", "hwChcsAlarm"), ("HUAWEI-PORT-MIB", "hwChcsAlarmResume"), ("HUAWEI-PORT-MIB", "hwCesLopsAlarm"),
("HUAWEI-PORT-MIB", "hwCesLopsAlarmResume"), ("HUAWEI-PORT-MIB", "hwAtmPwLosPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwAtmPwLosPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwAtmPwMisorderPktExcAlarm"),
("HUAWEI-PORT-MIB", "hwAtmPwMisorderPktExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwAtmPwUnknownCellExcAlarm"),
("HUAWEI-PORT-MIB", "hwAtmPwUnknownCellExcAlarmResume"), ("HUAWEI-PORT-MIB", "hwPortAlarmInverseAutoRecover"),))
hwDslGroupObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 9)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupWorkMode"),
("HUAWEI-PORT-MIB", "hwDslGroupBisState"), ("HUAWEI-PORT-MIB", "hwDslGroupEncapeMode"),
("HUAWEI-PORT-MIB", "hwDslGroupEnable"), ("HUAWEI-PORT-MIB", "hwDslGroupRowStatus"),
("HUAWEI-PORT-MIB", "hwDslGroupIfIndexOfBound"), ("HUAWEI-PORT-MIB", "hwVirtualEthernetIfIndex"),
("HUAWEI-PORT-MIB", "hwBoundVeRowStatus"), ("HUAWEI-PORT-MIB", "hwDslGroupVci"), ("HUAWEI-PORT-MIB", "hwDslGroupVpi"),
("HUAWEI-PORT-MIB", "hwDslGroupPvcId"),))
hwDslGroupImaObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 10)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslGroupImaVersion"), ("HUAWEI-PORT-MIB", "hwDslGroupImaFrameLen"),
("HUAWEI-PORT-MIB", "hwDslGroupImaReset"), ("HUAWEI-PORT-MIB", "hwDslGroupImaRxMinLinkNum"),
("HUAWEI-PORT-MIB", "hwDslGroupImaNeState"), ("HUAWEI-PORT-MIB", "hwDslGroupImaRxActLinkNum"),
("HUAWEI-PORT-MIB", "hwDslGroupImaRxCellRate"), ("HUAWEI-PORT-MIB", "hwDslGroupImaTxActLinkNum"),
("HUAWEI-PORT-MIB", "hwDslGroupImaTxCellRate"), ("HUAWEI-PORT-MIB", "hwDslGroupImaFeState"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfIndex"), ("HUAWEI-PORT-MIB", "hwDslGroupImaTxMinLinkNum"),
("HUAWEI-PORT-MIB", "hwDslGroupImaIfName"),))
hwDslLinkObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 11)).setObjects(*(
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfIndex"), ("HUAWEI-PORT-MIB", "hwDslLinkIfIndex"),
("HUAWEI-PORT-MIB", "hwDslLinkBoundRowStatus"), ("HUAWEI-PORT-MIB", "hwDslLinkIfName"),
("HUAWEI-PORT-MIB", "hwBoundDslGroupIfName"),))
hwDslImaTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 20)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslImaGroupLEDown"), ("HUAWEI-PORT-MIB", "hwDslImaGroupLEUp"),
("HUAWEI-PORT-MIB", "hwDslImaGroupREDown"), ("HUAWEI-PORT-MIB", "hwDslImaGroupREUp"),
("HUAWEI-PORT-MIB", "hwDslImaLinkLif"), ("HUAWEI-PORT-MIB", "hwDslImaLinkLifResume"),
("HUAWEI-PORT-MIB", "hwDslImaLinkLods"), ("HUAWEI-PORT-MIB", "hwDslImaLinkLodsResume"),
("HUAWEI-PORT-MIB", "hwDslImaLinkRfi"), ("HUAWEI-PORT-MIB", "hwDslImaLinkRfiResume"),
("HUAWEI-PORT-MIB", "hwDslImaLinkReTxUnusable"), ("HUAWEI-PORT-MIB", "hwDslImaLinkReTxUsable"),
("HUAWEI-PORT-MIB", "hwDslImaLinkReRxUnusable"), ("HUAWEI-PORT-MIB", "hwDslImaLinkReRxUsable"),))
hwDslLinkTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 21)).setObjects(*(
("HUAWEI-PORT-MIB", "hwDslLinkFrameLost"), ("HUAWEI-PORT-MIB", "hwDslLinkFrameResume"),
("HUAWEI-PORT-MIB", "hwDslLinkSignalLost"), ("HUAWEI-PORT-MIB", "hwDslLinkSignalResume"),))
hwPortAlarmThresholdObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 22)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorInterval"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorStatistics"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorInterval"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInputErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInputErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInputErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInputErrorInterval"),
("HUAWEI-PORT-MIB", "hwPhysicalPortOutputErrorStatistics"),
("HUAWEI-PORT-MIB", "hwPhysicalPortOutputErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortOutputErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortOutputErrorInterval"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorStatistics"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorHighThreshold"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorLowThreshold"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorInterval"),
("HUAWEI-PORT-MIB", "hwPhysicalPortBIP8SDErrorThreshold"),))
hwPortAlarmDownEnableObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 23)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcEnabledDown"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolEnabledDown"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInputEnabledDown"), ("HUAWEI-PORT-MIB", "hwPhysicalPortOutputEnabledDown"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhEnabledDown"), ("HUAWEI-PORT-MIB", "hwPhysicalPortBip8SdEnabledDown"),))
hwPortAlarmTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 157, 11, 2, 25)).setObjects(*(
("HUAWEI-PORT-MIB", "hwPhysicalPortCrcError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortCrcErrorResume"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSymbolErrorResume"),
("HUAWEI-PORT-MIB", "hwPhysicalPortInputError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortInputErrorResume"),
("HUAWEI-PORT-MIB", "hwPhysicalPortOutputError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortOutputErrorResume"),
("HUAWEI-PORT-MIB", "hwPhysicalPortSdhError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortSdhErrorResume"),
("HUAWEI-PORT-MIB", "hwPhysicalPortBip8SdError"), ("HUAWEI-PORT-MIB", "hwPhysicalPortBip8SdErrorResume"),))
mibBuilder.exportSymbols("HUAWEI-PORT-MIB", hwEthernetFlagJ0Trace=hwEthernetFlagJ0Trace,
                         hwSDHLpPerfCurrentSES=hwSDHLpPerfCurrentSES, hwPosCrcVerifyCode=hwPosCrcVerifyCode,
                         hwCposFlagJ0Value=hwCposFlagJ0Value, hwAtmVcID=hwAtmVcID,
                         hwDslImaLinkReRxUsable=hwDslImaLinkReRxUsable, hwSDHLpPerfCurrentEntry=hwSDHLpPerfCurrentEntry,
                         hwVc12LfaAlarmEn=hwVc12LfaAlarmEn, hwRroolAlarm=hwRroolAlarm, hwBundleSerial=hwBundleSerial,
                         hwCposE1LfaAlarm=hwCposE1LfaAlarm, hwLoopbackAlarm=hwLoopbackAlarm,
                         hwCposFlagJ0Trace=hwCposFlagJ0Trace, hwLcdAlarm=hwLcdAlarm,
                         hwLpUneqVc12Alarm=hwLpUneqVc12Alarm, hwE1LmfaAlarm=hwE1LmfaAlarm,
                         hwCposE1LfaAlarmResume=hwCposE1LfaAlarmResume, hwPosFlagJ1Trace=hwPosFlagJ1Trace,
                         hwDslImaGroupREDown=hwDslImaGroupREDown, hwTuAisVc12AlarmResume=hwTuAisVc12AlarmResume,
                         hwDslImaLinkRfiResume=hwDslImaLinkRfiResume, hwAuLopAlarmResume=hwAuLopAlarmResume,
                         hwPortAlarmTraps=hwPortAlarmTraps, hwDslGroupObjectGroup=hwDslGroupObjectGroup,
                         hwEthernetFlagJ1Mode=hwEthernetFlagJ1Mode, hwAtmPWAlarmIfIndex=hwAtmPWAlarmIfIndex,
                         hwPhysicalPortInChassis=hwPhysicalPortInChassis, hwTuAisVc12Alarm=hwTuAisVc12Alarm,
                         hwEthernetFlagC2Value=hwEthernetFlagC2Value,
                         hwPhysicalPortCrcPerAlarmThresholdCoefficient=hwPhysicalPortCrcPerAlarmThresholdCoefficient,
                         hwPhysicalPortDownName=hwPhysicalPortDownName, hwPortAlarmThreshold=hwPortAlarmThreshold,
                         hwRsJ0TimAlarmEn=hwRsJ0TimAlarmEn, hwDs0ChannelBundleRowStatus=hwDs0ChannelBundleRowStatus,
                         hwPtimAlarmResume=hwPtimAlarmResume, hwCposB1ExcAlarmThreshold=hwCposB1ExcAlarmThreshold,
                         hwAtmOcdAlarmEn=hwAtmOcdAlarmEn, hwPWCesVcID=hwPWCesVcID, hwLoopbackAllEn=hwLoopbackAllEn,
                         hwPrdiAlarmResume=hwPrdiAlarmResume, hwDslLinkSignalResume=hwDslLinkSignalResume,
                         hwDslGroupBindVeEntry=hwDslGroupBindVeEntry,
                         hwDs0ChannelBundleTimeSlot0=hwDs0ChannelBundleTimeSlot0,
                         hwSDHHpPerfCurrentFEBBE=hwSDHHpPerfCurrentFEBBE, hwDs1AisAlarmEn=hwDs1AisAlarmEn,
                         hwDs0ChannelBundleTimeSlots=hwDs0ChannelBundleTimeSlots, hwLpPlmAlarmEn=hwLpPlmAlarmEn,
                         hwBundleSerialIfIndex=hwBundleSerialIfIndex, hwSNMPTrapEnTable=hwSNMPTrapEnTable,
                         hwHpJ1TimAlarmEn=hwHpJ1TimAlarmEn, hwSDHLpPerfCurrentFESES=hwSDHLpPerfCurrentFESES,
                         hwDs0ChannelBundlePortName=hwDs0ChannelBundlePortName, hwCposClock=hwCposClock,
                         hwLpV5VcaisAlarmEn=hwLpV5VcaisAlarmEn, hwAtmPeerIpAddr=hwAtmPeerIpAddr,
                         hwAtmMisorderPktExcTriggerThreshold=hwAtmMisorderPktExcTriggerThreshold,
                         hwDslLinkTraps=hwDslLinkTraps, hwDs3CreateSerial=hwDs3CreateSerial,
                         hwSDHMsPerfCurrentFEUAS=hwSDHMsPerfCurrentFEUAS, hwCposE1AlmE1RaiAlarm=hwCposE1AlmE1RaiAlarm,
                         hwDs1CodeType=hwDs1CodeType, hwPortAlarmInverseEnable=hwPortAlarmInverseEnable,
                         hwDs0ChannelBundle=hwDs0ChannelBundle, hwLaserShutAlarmEn=hwLaserShutAlarmEn,
                         hwCposIfType=hwCposIfType, hwBundleSerialTable=hwBundleSerialTable,
                         hwCesJtrUdrExcAlarmResume=hwCesJtrUdrExcAlarmResume, hwDs3ParentIfIndex=hwDs3ParentIfIndex,
                         hwEthernetOffline=hwEthernetOffline, hwPortAlarmDownEnableEntry=hwPortAlarmDownEnableEntry,
                         hwSDHLpPerfCurrentFEES=hwSDHLpPerfCurrentFEES, hwDslGroupEncapeMode=hwDslGroupEncapeMode,
                         hwHpB3SdAlarmEn=hwHpB3SdAlarmEn, hwDslGroupPvcId=hwDslGroupPvcId,
                         hwDslGroupImaTxMinLinkNum=hwDslGroupImaTxMinLinkNum,
                         hwDslGroupImaFrameLen=hwDslGroupImaFrameLen, hwBindVeRowStatus=hwBindVeRowStatus,
                         hwDslLinkTable=hwDslLinkTable, hwVrdiAlarmResume=hwVrdiAlarmResume,
                         hwSDHHpPerfCurrentFEES=hwSDHHpPerfCurrentFEES,
                         hwVirtualEthernetIfIndex=hwVirtualEthernetIfIndex, hwJ0TimAlarm=hwJ0TimAlarm,
                         hwDs1CableLength=hwDs1CableLength, hwDslGroupWorkMode=hwDslGroupWorkMode,
                         hwDslImaLinkReRxUnusable=hwDslImaLinkReRxUnusable, hwDs3Loopback=hwDs3Loopback,
                         hwCesMisorderPktExcAlarmResume=hwCesMisorderPktExcAlarmResume,
                         hwPaisAlarmResume=hwPaisAlarmResume, hwDs1IfIndex=hwDs1IfIndex,
                         hwCesPWOppositeAcfaultEn=hwCesPWOppositeAcfaultEn, hwPhysicalPortEntry=hwPhysicalPortEntry,
                         hwCesLopsAlarm=hwCesLopsAlarm, hwEthPortStatIfIndex=hwEthPortStatIfIndex,
                         hwLaserShutAlarm=hwLaserShutAlarm, hwPosFlagJ0Value=hwPosFlagJ0Value,
                         hwMalPktExcResumeThreshold=hwMalPktExcResumeThreshold,
                         hwPhysicalPortBIP8SDErrorThreshold=hwPhysicalPortBIP8SDErrorThreshold,
                         hwAtmUhcsAlarmEn=hwAtmUhcsAlarmEn,
                         hwPortAlarmDownEnableObjectGroup=hwPortAlarmDownEnableObjectGroup,
                         hwPhysicalPortBip8SdError=hwPhysicalPortBip8SdError, hwSNMPTrapEnEntry=hwSNMPTrapEnEntry,
                         hwLaserAllEn=hwLaserAllEn, hwDslLinkFrameLost=hwDslLinkFrameLost,
                         hwMsB2ExcAlarmEn=hwMsB2ExcAlarmEn, hwDslGroupTable=hwDslGroupTable,
                         hwSdbereAlarmResume=hwSdbereAlarmResume, hwDslGroupVpi=hwDslGroupVpi,
                         hwPhysicalPort=hwPhysicalPort, hwRsB1SdAlarmEn=hwRsB1SdAlarmEn,
                         hwMsAuLopAlarmEn=hwMsAuLopAlarmEn, hwStrayPktExcTriggerThreshold=hwStrayPktExcTriggerThreshold,
                         hwAuAisAlarm=hwAuAisAlarm, hwDs1Loopback=hwDs1Loopback, hwPplmAlarm=hwPplmAlarm,
                         hwPhysicalPortSymbolErrorHighThreshold=hwPhysicalPortSymbolErrorHighThreshold,
                         hwPhysicalPortCrcPerCurrentValueString=hwPhysicalPortCrcPerCurrentValueString,
                         hwCesPwOppositeRaiResume=hwCesPwOppositeRaiResume,
                         hwDslGroupImaRxMinLinkNum=hwDslGroupImaRxMinLinkNum,
                         hwDs0ChannelBundleMasterPWStatus=hwDs0ChannelBundleMasterPWStatus,
                         hwMalPktExcTriggerThreshold=hwMalPktExcTriggerThreshold,
                         hwLoopBackAutoClearPeriod=hwLoopBackAutoClearPeriod, hwDs1Cable=hwDs1Cable,
                         hwLpTimVc12AlarmResume=hwLpTimVc12AlarmResume, hwChannelLoopbackAlarm=hwChannelLoopbackAlarm,
                         hwPosLinkProtocol=hwPosLinkProtocol, hwB3TcaAlarm=hwB3TcaAlarm,
                         hwDs3Channelized=hwDs3Channelized, hwLosPktExcResumeThreshold=hwLosPktExcResumeThreshold,
                         hwLosAlarmResume=hwLosAlarmResume, hwPWAlarmIfIndex=hwPWAlarmIfIndex,
                         hwAtmUnknownCellExcResumeThreshold=hwAtmUnknownCellExcResumeThreshold,
                         hwSNMPTrapEnIfIndex=hwSNMPTrapEnIfIndex,
                         hwPhysicalPortSdhErrorHighThreshold=hwPhysicalPortSdhErrorHighThreshold,
                         hwLpSlmVc12Alarm=hwLpSlmVc12Alarm, hwDslImaLinkLifResume=hwDslImaLinkLifResume,
                         hwPDHPerfCurrentIfIndex=hwPDHPerfCurrentIfIndex,
                         hwAtmPwMisorderPktExcAlarm=hwAtmPwMisorderPktExcAlarm,
                         hwPhysicalPortSdhErrorInterval=hwPhysicalPortSdhErrorInterval,
                         hwPortAlarmDownEnableTable=hwPortAlarmDownEnableTable,
                         hwCesPwRemoteLosPktAlarmResume=hwCesPwRemoteLosPktAlarmResume,
                         hwOcdAlarmResume=hwOcdAlarmResume, hwPosFlagC2Value=hwPosFlagC2Value,
                         hwCesPWJtrOvrEn=hwCesPWJtrOvrEn, hwDs1DownE1AisAlarmEn=hwDs1DownE1AisAlarmEn,
                         hwCposLoopback=hwCposLoopback, hwDslGroupImaTxCellRate=hwDslGroupImaTxCellRate,
                         hwCposLpBipExcAlarmThreshold=hwCposLpBipExcAlarmThreshold,
                         hwSDHRsPerfCurrentBBE=hwSDHRsPerfCurrentBBE, hwDslGroupBisState=hwDslGroupBisState,
                         hwPortAlarmThresholdTable=hwPortAlarmThresholdTable, hwDs3ObjectGroup=hwDs3ObjectGroup,
                         hwDs3Scramble=hwDs3Scramble, hwLomAlarmResume=hwLomAlarmResume,
                         hwDslGroupIfIndexOfBound=hwDslGroupIfIndexOfBound,
                         hwDs0ChannelBundleIsMasterPW=hwDs0ChannelBundleIsMasterPW,
                         hwLaserAutoShutAlarmResume=hwLaserAutoShutAlarmResume, hwOcdAlarm=hwOcdAlarm,
                         hwOutputErrorAlarm=hwOutputErrorAlarm,
                         hwAtmPwUnknownCellExcAlarmResume=hwAtmPwUnknownCellExcAlarmResume,
                         hwPhysicalPortThrIfIndex=hwPhysicalPortThrIfIndex, hwDslGroupIfIndex=hwDslGroupIfIndex,
                         hwPhysicalPortName=hwPhysicalPortName, hwLpTimVc12Alarm=hwLpTimVc12Alarm,
                         hwDslGroupImaEntry=hwDslGroupImaEntry, hwSDHLpPerfCurrentTable=hwSDHLpPerfCurrentTable,
                         hwLpRdiAlarmEn=hwLpRdiAlarmEn, hwDs1ObjectGroup=hwDs1ObjectGroup,
                         hwCposLpBipSdAlarmThreshold=hwCposLpBipSdAlarmThreshold,
                         hwBundleSerialTimerHold=hwBundleSerialTimerHold, hwDslLinkEntry=hwDslLinkEntry,
                         hwSDHLpPerfCurrentLpIndex=hwSDHLpPerfCurrentLpIndex, hwDslLinkIfIndex=hwDslLinkIfIndex,
                         hwEthernetJumboframeMaxLength=hwEthernetJumboframeMaxLength, hwDs3ChannelId=hwDs3ChannelId,
                         hwDslGroupImaIfName=hwDslGroupImaIfName, hwDslGroupImaReset=hwDslGroupImaReset,
                         hwPDHPerfCurrentTable=hwPDHPerfCurrentTable, hwPhysicalPortLosAlarmEn=hwPhysicalPortLosAlarmEn,
                         hwSDHHpPerfCurrentUAS=hwSDHHpPerfCurrentUAS, hwPDHPerfCurrentUAS=hwPDHPerfCurrentUAS,
                         hwPhysicalPortLofAlarmEn=hwPhysicalPortLofAlarmEn,
                         hwEthernetSetTransferMode=hwEthernetSetTransferMode, hwEthernetPortType=hwEthernetPortType,
                         hwEthernetTable=hwEthernetTable, PYSNMP_MODULE_ID=hwPortMIB,
                         hwDs0ChannelBundleTable=hwDs0ChannelBundleTable,
                         hwPhysicalPortCrcPacketErrorRatio=hwPhysicalPortCrcPacketErrorRatio,
                         hwSDHHpPerfCurrentSES=hwSDHHpPerfCurrentSES, hwPortMIBObjects=hwPortMIBObjects, hwDs1=hwDs1,
                         hwChcsAlarm=hwChcsAlarm,
                         hwPhysicalPortCrcPerResumeThresholdCoefficient=hwPhysicalPortCrcPerResumeThresholdCoefficient,
                         hwCposHighPathNumber=hwCposHighPathNumber, hwAuLopAlarm=hwAuLopAlarm,
                         hwDs1RdiAlarmEn=hwDs1RdiAlarmEn,
                         hwPhysicalPortInputErrorLowThreshold=hwPhysicalPortInputErrorLowThreshold,
                         hwBip2TcaAlarmResume=hwBip2TcaAlarmResume, hwB2TcaAlarmResume=hwB2TcaAlarmResume,
                         hwSDHMsPerfCurrentES=hwSDHMsPerfCurrentES, hwPortNotificationsGroup=hwPortNotificationsGroup,
                         hwCesPWRemoteLosPktEn=hwCesPWRemoteLosPktEn, hwLaisAlarm=hwLaisAlarm,
                         hwLoopBackAutoClearNotice=hwLoopBackAutoClearNotice,
                         hwInputErrorAlarmResume=hwInputErrorAlarmResume,
                         hwCesStrayPktExcAlarmResume=hwCesStrayPktExcAlarmResume, hwPosScramble=hwPosScramble,
                         hwSDHLpPerfCurrentBBE=hwSDHLpPerfCurrentBBE, hwAtmPWAlarmTable=hwAtmPWAlarmTable,
                         hwCesPWLosPktEn=hwCesPWLosPktEn, hwCposB3SdAlarmThreshold=hwCposB3SdAlarmThreshold,
                         hwB1TcaAlarm=hwB1TcaAlarm, hwDslLinkIfName=hwDslLinkIfName,
                         hwLosAlarmResumeThreshold=hwLosAlarmResumeThreshold,
                         hwDslGroupBindVeTable=hwDslGroupBindVeTable, hwPrdiAlarm=hwPrdiAlarm,
                         hwPDHPerfCurrentDataIndex=hwPDHPerfCurrentDataIndex, hwMsK1K2MAlarmEn=hwMsK1K2MAlarmEn,
                         hwLoopbackAlarmResume=hwLoopbackAlarmResume, hwAtmPWLosPktEn=hwAtmPWLosPktEn,
                         hwPhysicalPortAlarmInverseEnable=hwPhysicalPortAlarmInverseEnable, hwB2TcaAlarm=hwB2TcaAlarm,
                         hwDs1Entry=hwDs1Entry, hwVrdiAlarm=hwVrdiAlarm,
                         hwAtmUnknownCellExcTriggerThreshold=hwAtmUnknownCellExcTriggerThreshold,
                         hwInputErrorAlarm=hwInputErrorAlarm, hwSDHMsPerfCurrentUAS=hwSDHMsPerfCurrentUAS,
                         hwVc12UpE1AisAlarmEn=hwVc12UpE1AisAlarmEn,
                         hwSDHLpPerfCurrentDataIndex=hwSDHLpPerfCurrentDataIndex, hwVlopAlarmResume=hwVlopAlarmResume,
                         hwPhysicalPortInPort=hwPhysicalPortInPort, hwDs1ParentIfIndex=hwDs1ParentIfIndex,
                         hwDslGroupImaTable=hwDslGroupImaTable, hwDs1ChannelId=hwDs1ChannelId,
                         hwSDHLpPerfCurrentUAS=hwSDHLpPerfCurrentUAS,
                         hwJtrOvrExcTriggerThreshold=hwJtrOvrExcTriggerThreshold,
                         hwBundleSerialLinkProtocol=hwBundleSerialLinkProtocol,
                         hwDslGroupImaObjectGroup=hwDslGroupImaObjectGroup, hwPosFlagJ0Trace=hwPosFlagJ0Trace,
                         hwPhysicalPortCrcPerTriggerLsp=hwPhysicalPortCrcPerTriggerLsp,
                         hwDslGroupImaVersion=hwDslGroupImaVersion, hwSDHLpPerfCurrentHpIndex=hwSDHLpPerfCurrentHpIndex,
                         hwPortAlarmTrapGroup=hwPortAlarmTrapGroup,
                         hwPhysicalPortCrcErrorStatistics=hwPhysicalPortCrcErrorStatistics,
                         hwDs1RmfaAlarmEn=hwDs1RmfaAlarmEn, hwSDHRsPerfCurrentSES=hwSDHRsPerfCurrentSES,
                         hwCesPWStrayPktEn=hwCesPWStrayPktEn, hwCesPWMisorderPktEn=hwCesPWMisorderPktEn,
                         hwPhysicalAutoShutLaserLongOpenInterval=hwPhysicalAutoShutLaserLongOpenInterval,
                         hwPhysicalLoopbackType=hwPhysicalLoopbackType, hwCesPwOppositeAcFault=hwCesPwOppositeAcFault,
                         hwCesJtrUdrExcAlarm=hwCesJtrUdrExcAlarm,
                         hwMisorderPktExcTriggerThreshold=hwMisorderPktExcTriggerThreshold,
                         hwV5VcaisAlarmResume=hwV5VcaisAlarmResume, hwDslImaLinkLods=hwDslImaLinkLods)
mibBuilder.exportSymbols("HUAWEI-PORT-MIB", hwDs1WorkMode=hwDs1WorkMode, hwAtmLcdAlarmEn=hwAtmLcdAlarmEn,
                         hwPortPhysicalLpIndex=hwPortPhysicalLpIndex, hwPortPhysicalHpIndex=hwPortPhysicalHpIndex,
                         hwRsB1ExcAlarmEn=hwRsB1ExcAlarmEn, hwPWAlarm=hwPWAlarm, hwCposFlagJ1Trace=hwCposFlagJ1Trace,
                         hwPhysicalPortSdhErrorStatistics=hwPhysicalPortSdhErrorStatistics,
                         hwLosPktExcTriggerThreshold=hwLosPktExcTriggerThreshold, hwVrfiAlarm=hwVrfiAlarm,
                         hwSDHRsMsPerfCurrentIfIndex=hwSDHRsMsPerfCurrentIfIndex, hwSNMPTrapEn=hwSNMPTrapEn,
                         hwJtrUdrExcTriggerThreshold=hwJtrUdrExcTriggerThreshold,
                         hwPhysicalPortCrcError=hwPhysicalPortCrcError, hwMsAisAlarmEn=hwMsAisAlarmEn,
                         hwChannelLoopbackAlarmEn=hwChannelLoopbackAlarmEn, hwEthPortStatEntry=hwEthPortStatEntry,
                         hwPhysicalPortCrcErrorLowThreshold=hwPhysicalPortCrcErrorLowThreshold,
                         hwEthernetUpHoldTime=hwEthernetUpHoldTime, hwSDHHpPerfCurrentIfIndex=hwSDHHpPerfCurrentIfIndex,
                         hwLoopbackAlarmEn=hwLoopbackAlarmEn, hwPhysicalPortHoldUp=hwPhysicalPortHoldUp,
                         hwAtmVcType=hwAtmVcType, hwDs3Table=hwDs3Table,
                         hwLpUneqVc12AlarmResume=hwLpUneqVc12AlarmResume, hwPosLoopback=hwPosLoopback,
                         hwCposLpIfIndex=hwCposLpIfIndex, hwEthernetLoopback=hwEthernetLoopback,
                         hwDslLinkSignalLost=hwDslLinkSignalLost, hwHpJ1TiuAlarm=hwHpJ1TiuAlarm,
                         hwVc12oofAlarmEn=hwVc12oofAlarmEn, hwDslGroupBoundVeEntry=hwDslGroupBoundVeEntry,
                         hwDs3RowStatus=hwDs3RowStatus, hwPosIfIndex=hwPosIfIndex,
                         hwEthPortStatTable=hwEthPortStatTable, hwPhysicalShutLaser=hwPhysicalShutLaser, hwDs3=hwDs3,
                         hwCesStrayPktExcAlarm=hwCesStrayPktExcAlarm, hwCposFlagJ0Mode=hwCposFlagJ0Mode,
                         hwCesJtrOvrExcAlarmResume=hwCesJtrOvrExcAlarmResume, hwPortNotifications=hwPortNotifications,
                         hwPhysicalPortCrcPerAlarmThresholdString=hwPhysicalPortCrcPerAlarmThresholdString,
                         hwDs0ChannelBundleSpeed=hwDs0ChannelBundleSpeed,
                         hwPhysicalPortBip8SdErrorResume=hwPhysicalPortBip8SdErrorResume,
                         hwDs0ChannelBundleId=hwDs0ChannelBundleId, hwCposMultiplex=hwCposMultiplex,
                         hwLaisAlarmResume=hwLaisAlarmResume, hwLaserAutoShutAlarm=hwLaserAutoShutAlarm,
                         hwPhysicalPortTable=hwPhysicalPortTable,
                         hwDs1EsAlarmResumeThreshold=hwDs1EsAlarmResumeThreshold, hwAtmAllEn=hwAtmAllEn,
                         hwPhysicalPortBip8SdEnabledDown=hwPhysicalPortBip8SdEnabledDown,
                         hwDslGroupInterfaceIndex=hwDslGroupInterfaceIndex, hwDslGroupImaIfIndex=hwDslGroupImaIfIndex,
                         hwPhysicalPortIfIndex=hwPhysicalPortIfIndex, hwPhysicalLaserStatus=hwPhysicalLaserStatus,
                         hwCposLowPathNumber=hwCposLowPathNumber, hwDs3IfIndex=hwDs3IfIndex,
                         hwHpUneqAlarmEn=hwHpUneqAlarmEn, hwCesPwOppositeRai=hwCesPwOppositeRai,
                         hwPhysicalPortInputErrorInterval=hwPhysicalPortInputErrorInterval,
                         hwPDHPerfCurrentEntry=hwPDHPerfCurrentEntry, hwPosFrameFormat=hwPosFrameFormat,
                         hwCposEntry=hwCposEntry, hwEthernetDownHoldTime=hwEthernetDownHoldTime, hwPosEntry=hwPosEntry,
                         hwB1TcaAlarmResume=hwB1TcaAlarmResume, hwCposLpTable=hwCposLpTable,
                         hwDs3NationalBit=hwDs3NationalBit, hwEthernetEntry=hwEthernetEntry,
                         hwPhysicalPortSymbolError=hwPhysicalPortSymbolError, hwDslGroupImaNeState=hwDslGroupImaNeState,
                         hwDs1RowStatus=hwDs1RowStatus, hwAlarmStatus=hwAlarmStatus, hwUhcsAlarm=hwUhcsAlarm,
                         hwCposFlagJ1Mode=hwCposFlagJ1Mode,
                         hwDs0ChannelBundleParentIfIndex=hwDs0ChannelBundleParentIfIndex, hwLofAlarm=hwLofAlarm,
                         hwDslImaLinkReTxUnusable=hwDslImaLinkReTxUnusable, hwPDHPerfCurrentES=hwPDHPerfCurrentES,
                         hwPhysicalPortCrcPerAlarmThresholdPower=hwPhysicalPortCrcPerAlarmThresholdPower,
                         hwCposB1SdAlarmThreshold=hwCposB1SdAlarmThreshold, hwMsK2MAlarmEn=hwMsK2MAlarmEn,
                         hwEthernetFlowControl=hwEthernetFlowControl, hwSdbereAlarm=hwSdbereAlarm,
                         hwRsLocAlarmEn=hwRsLocAlarmEn, hwDslImaLinkTraps=hwDslImaLinkTraps,
                         hwAtmLosPktExcTriggerThreshold=hwAtmLosPktExcTriggerThreshold,
                         hwSDHMsPerfCurrentFEES=hwSDHMsPerfCurrentFEES, hwDslGroupBoundVeTable=hwDslGroupBoundVeTable,
                         hwLpUneqAlarmEn=hwLpUneqAlarmEn,
                         hwChannelLoopBackAutoClearNotice=hwChannelLoopBackAutoClearNotice,
                         hwPhysicalPortCrcErrorHighThreshold=hwPhysicalPortCrcErrorHighThreshold,
                         hwJ0TimAlarmResume=hwJ0TimAlarmResume, hwDs1ChannelType=hwDs1ChannelType,
                         hwHpRdiAlarmEn=hwHpRdiAlarmEn, hwCposObjectGroup=hwCposObjectGroup,
                         hwE1AlmE1RaiAlarm=hwE1AlmE1RaiAlarm, hwAtmPwLosPktExcAlarmResume=hwAtmPwLosPktExcAlarmResume,
                         hwAtmPWAlarmEntry=hwAtmPWAlarmEntry, hwEthernetPortTypeOperate=hwEthernetPortTypeOperate,
                         hwDs3Entry=hwDs3Entry, hwPortAlarmThresholdEntry=hwPortAlarmThresholdEntry,
                         hwSDHMsPerfCurrentBBE=hwSDHMsPerfCurrentBBE, hwDslImaGroupLEDown=hwDslImaGroupLEDown,
                         hwDs1Clock=hwDs1Clock, hwLpRfiAlarmEn=hwLpRfiAlarmEn,
                         hwPhysicalPortThrName=hwPhysicalPortThrName, hwSDHHpPerfCurrentFESES=hwSDHHpPerfCurrentFESES,
                         hwPosFlagJ1Value=hwPosFlagJ1Value,
                         hwPhysicalPortSymbolErrorInterval=hwPhysicalPortSymbolErrorInterval,
                         hwCposLpEntry=hwCposLpEntry, hwDslImaGroupREUp=hwDslImaGroupREUp,
                         hwPhysicalPortCrcPacketErrorRatioResume=hwPhysicalPortCrcPacketErrorRatioResume,
                         hwDslImaGroupTraps=hwDslImaGroupTraps,
                         hwSDHRsMsPerfCurrentDataIndex=hwSDHRsMsPerfCurrentDataIndex, hwCesPWAllEn=hwCesPWAllEn,
                         hwPtimAlarm=hwPtimAlarm, hwDs1FrameFormat=hwDs1FrameFormat,
                         hwMsLpsUniBiMAlarmEn=hwMsLpsUniBiMAlarmEn, hwPortCompliances=hwPortCompliances,
                         hwPosTable=hwPosTable, hwPhysicalPortSymbolErrorResume=hwPhysicalPortSymbolErrorResume,
                         hwDslImaLinkLodsResume=hwDslImaLinkLodsResume, hwSDHRsPerfCurrentES=hwSDHRsPerfCurrentES,
                         hwPhysicalPortSdhEnabledDown=hwPhysicalPortSdhEnabledDown,
                         hwB3TcaAlarmResume=hwB3TcaAlarmResume, hwPhysicalPortDownIfIndex=hwPhysicalPortDownIfIndex,
                         hwEthPortStatBadBytes=hwEthPortStatBadBytes,
                         hwPhysicalPortInputErrorHighThreshold=hwPhysicalPortInputErrorHighThreshold,
                         hwLomAlarm=hwLomAlarm, hwLpBipSdAlarmEn=hwLpBipSdAlarmEn,
                         hwDslGroupImaFeState=hwDslGroupImaFeState, hwEthernetNegotiationMode=hwEthernetNegotiationMode,
                         hwPuneqAlarm=hwPuneqAlarm, hwDs1Lbo=hwDs1Lbo, hwDs1LmfaAlarmEn=hwDs1LmfaAlarmEn,
                         hwCesPwOppositeAcFaultResume=hwCesPwOppositeAcFaultResume,
                         hwPhysicalPortCrcEnabledDown=hwPhysicalPortCrcEnabledDown,
                         hwCposE1AlmE1RaiAlarmResume=hwCposE1AlmE1RaiAlarmResume,
                         hwSDHHpPerfCurrentDataIndex=hwSDHHpPerfCurrentDataIndex,
                         hwE1LmfaAlarmResume=hwE1LmfaAlarmResume, hwCposTable=hwCposTable,
                         hwSDHHpPerfCurrentBBE=hwSDHHpPerfCurrentBBE, hwRsOofAlarmEn=hwRsOofAlarmEn,
                         hwDs0ChannelBundleDs1ChannelId=hwDs0ChannelBundleDs1ChannelId,
                         hwPhysicalAutoShutLaserCloseInterval=hwPhysicalAutoShutLaserCloseInterval,
                         hwEthernetFlagJ1Value=hwEthernetFlagJ1Value,
                         hwCposB2ExcAlarmThreshold=hwCposB2ExcAlarmThreshold,
                         hwSDHLpPerfCurrentFEBBE=hwSDHLpPerfCurrentFEBBE,
                         hwPortACRMasterPWChange=hwPortACRMasterPWChange, hwBoundDslGroupIfName=hwBoundDslGroupIfName,
                         hwDslGroupImaRxCellRate=hwDslGroupImaRxCellRate, hwHpAuAisAlarmEn=hwHpAuAisAlarmEn,
                         hwLaserShutAlarmResume=hwLaserShutAlarmResume, hwCposE1LmfaAlarmResume=hwCposE1LmfaAlarmResume,
                         hwPhysicalPortInputErrorStatistics=hwPhysicalPortInputErrorStatistics,
                         hwBundleSerialObjectGroup=hwBundleSerialObjectGroup, hwCposLpId=hwCposLpId,
                         hwDs3Clock=hwDs3Clock, hwDslImaGroupLEUp=hwDslImaGroupLEUp, hwDs3IfType=hwDs3IfType,
                         hwHpTuLomAlarmEn=hwHpTuLomAlarmEn, hwPortCompliance=hwPortCompliance,
                         hwCposE1UpE1AisAlarm=hwCposE1UpE1AisAlarm, hwPDHPerfCurrentSES=hwPDHPerfCurrentSES,
                         hwCposFrameFormat=hwCposFrameFormat, hwE1UpE1AisAlarmResume=hwE1UpE1AisAlarmResume,
                         hwEthernetFlagJ1Trace=hwEthernetFlagJ1Trace,
                         hwAtmLosPktExcResumeThreshold=hwAtmLosPktExcResumeThreshold, hwCesPWJtrUnrEn=hwCesPWJtrUnrEn,
                         hwDslImaTrapGroup=hwDslImaTrapGroup,
                         hwPhysicalPortOutputErrorInterval=hwPhysicalPortOutputErrorInterval,
                         hwChcsAlarmResume=hwChcsAlarmResume, hwEthernetComboType=hwEthernetComboType,
                         hwCesMisorderPktExcAlarm=hwCesMisorderPktExcAlarm, hwVlopAlarm=hwVlopAlarm,
                         hwLoopBackAutoClearEnable=hwLoopBackAutoClearEnable,
                         hwDs1EsAlarmTriggerThreshold=hwDs1EsAlarmTriggerThreshold,
                         hwDslGroupImaRxActLinkNum=hwDslGroupImaRxActLinkNum, hwPeerIpAddr=hwPeerIpAddr,
                         hwLofAlarmResume=hwLofAlarmResume, hwPhysicalPortSdhErrorResume=hwPhysicalPortSdhErrorResume,
                         hwDslGroupEntry=hwDslGroupEntry,
                         hwPhysicalPortCrcPerResumeThresholdString=hwPhysicalPortCrcPerResumeThresholdString,
                         hwDslGroupImaTxActLinkNum=hwDslGroupImaTxActLinkNum, hwEthernetIfIndex=hwEthernetIfIndex,
                         hwCposIfIndex=hwCposIfIndex, hwHpPlmAlarmEn=hwHpPlmAlarmEn, hwDs1Table=hwDs1Table,
                         hwCesPwRemoteLosPktAlarm=hwCesPwRemoteLosPktAlarm,
                         hwLpSlmVc12AlarmResume=hwLpSlmVc12AlarmResume, hwCposE1DownE1AisAlarm=hwCposE1DownE1AisAlarm,
                         hwPhysicalPortInputEnabledDown=hwPhysicalPortInputEnabledDown,
                         hwSDHLpPerfCurrentES=hwSDHLpPerfCurrentES, hwPhysicalPortInCard=hwPhysicalPortInCard,
                         hwLpTuLopAlarmEn=hwLpTuLopAlarmEn, hwDs1IfType=hwDs1IfType,
                         hwPortAlarmThresholdObjectGroup=hwPortAlarmThresholdObjectGroup,
                         hwMisorderPktExcResumeThreshold=hwMisorderPktExcResumeThreshold,
                         hwEthernetSpeedSet=hwEthernetSpeedSet, hwOofAlarmResume=hwOofAlarmResume,
                         hwCposE1UpE1AisAlarmResume=hwCposE1UpE1AisAlarmResume, hwBip2TcaAlarm=hwBip2TcaAlarm,
                         hwDslLinkTrapGroup=hwDslLinkTrapGroup, hwDslImaLinkRfi=hwDslImaLinkRfi,
                         hwCposFlagJ2Mode=hwCposFlagJ2Mode, hwSDHMsPerfCurrentFESES=hwSDHMsPerfCurrentFESES,
                         hwPhysicalPortSymbolErrorLowThreshold=hwPhysicalPortSymbolErrorLowThreshold,
                         hwBoundDslGroupIfIndex=hwBoundDslGroupIfIndex,
                         hwAtmMisorderPktExcResumeThreshold=hwAtmMisorderPktExcResumeThreshold,
                         hwAtmPWPortName=hwAtmPWPortName, hwDslImaLinkLif=hwDslImaLinkLif,
                         hwSDHRsMsPerfCurrentEntry=hwSDHRsMsPerfCurrentEntry, hwAuAisAlarmResume=hwAuAisAlarmResume,
                         hwPaisAlarm=hwPaisAlarm, hwBoundVeRowStatus=hwBoundVeRowStatus, hwDslLink=hwDslLink,
                         hwPortMIB=hwPortMIB, hwSDHLpPerfCurrentIfIndex=hwSDHLpPerfCurrentIfIndex,
                         hwPhysicalPortCrcErrorInterval=hwPhysicalPortCrcErrorInterval,
                         hwSDHMsPerfCurrentFEBBE=hwSDHMsPerfCurrentFEBBE,
                         hwDs1ClockRecoveryDomain=hwDs1ClockRecoveryDomain,
                         hwPWAlarmRMLEnableStatus=hwPWAlarmRMLEnableStatus, hwCesPWMalPktEn=hwCesPWMalPktEn,
                         hwPhysicalPortOutputErrorLowThreshold=hwPhysicalPortOutputErrorLowThreshold,
                         hwPhysicalPortOutputErrorStatistics=hwPhysicalPortOutputErrorStatistics,
                         hwLosAlarmTriggerThreshold=hwLosAlarmTriggerThreshold, hwPuneqAlarmResume=hwPuneqAlarmResume,
                         hwChannelLoopbackAlarmResume=hwChannelLoopbackAlarmResume,
                         hwAtmPwLosPktExcAlarm=hwAtmPwLosPktExcAlarm, hwEthernetObjectGroup=hwEthernetObjectGroup,
                         hwEthernetNegotiation=hwEthernetNegotiation, hwLosAlarm=hwLosAlarm,
                         hwDs1EsExcAlarmEn=hwDs1EsExcAlarmEn, hwE1UpE1AisAlarm=hwE1UpE1AisAlarm,
                         hwPosObjectGroup=hwPosObjectGroup, hwSDHHpPerfCurrentES=hwSDHHpPerfCurrentES,
                         hwDslLinkObjectGroup=hwDslLinkObjectGroup, hwSDHMsPerfCurrentSES=hwSDHMsPerfCurrentSES,
                         hwCposMappingMode=hwCposMappingMode, hwDslLinkBoundRowStatus=hwDslLinkBoundRowStatus,
                         hwPhysicalPortGlobleCfg=hwPhysicalPortGlobleCfg, hwVc12AlmE1RaiAlarmEn=hwVc12AlmE1RaiAlarmEn,
                         hwRroolAlarmResume=hwRroolAlarmResume,
                         hwDs0ChannelBundleObjectGroup=hwDs0ChannelBundleObjectGroup,
                         hwCposB2SdAlarmThreshold=hwCposB2SdAlarmThreshold, hwHpJ1TiuAlarmResume=hwHpJ1TiuAlarmResume,
                         hwPWPortName=hwPWPortName, hwCposE1LmfaAlarm=hwCposE1LmfaAlarm,
                         hwSDHHpPerfCurrentHpIndex=hwSDHHpPerfCurrentHpIndex,
                         hwSDHHpPerfCurrentEntry=hwSDHHpPerfCurrentEntry, hwCposFlagJ1Value=hwCposFlagJ1Value,
                         hwPortConformance=hwPortConformance)
mibBuilder.exportSymbols("HUAWEI-PORT-MIB",
                         hwPhysicalPortCrcPerResumeThresholdPower=hwPhysicalPortCrcPerResumeThresholdPower,
                         hwPhysicalPortOutputErrorHighThreshold=hwPhysicalPortOutputErrorHighThreshold,
                         hwDslGroupIma=hwDslGroupIma, hwPWCesVcType=hwPWCesVcType,
                         hwCesJtrOvrExcAlarm=hwCesJtrOvrExcAlarm, hwVc12LmfaAlarmEn=hwVc12LmfaAlarmEn,
                         hwPhysicalPortSdhError=hwPhysicalPortSdhError,
                         hwEthernetSubinterfaceStatisticEnable=hwEthernetSubinterfaceStatisticEnable,
                         hwPhysicalPortSymbolEnabledDown=hwPhysicalPortSymbolEnabledDown,
                         hwPhysicalAutoShutLaserEnable=hwPhysicalAutoShutLaserEnable,
                         hwCposB3ExcAlarmThreshold=hwCposB3ExcAlarmThreshold,
                         hwVirtualEthernetInterfaceIndex=hwVirtualEthernetInterfaceIndex,
                         hwCesMalPktExcAlarm=hwCesMalPktExcAlarm, hwEthernetClock=hwEthernetClock,
                         hwBundleSerialEntry=hwBundleSerialEntry,
                         hwPhysicalPortDelayRemainTime=hwPhysicalPortDelayRemainTime,
                         hwE1AlmE1RaiAlarmResume=hwE1AlmE1RaiAlarmResume, hwPWAlarmEntry=hwPWAlarmEntry,
                         hwDs1Channelized=hwDs1Channelized, hwSDHLpPerfCurrentFEUAS=hwSDHLpPerfCurrentFEUAS,
                         hwCesLosPktExcAlarm=hwCesLosPktExcAlarm, hwDs0ChannelBundleIfIndex=hwDs0ChannelBundleIfIndex,
                         hwPplmAlarmResume=hwPplmAlarmResume, hwLrdiAlarm=hwLrdiAlarm, hwCesPWLopsEn=hwCesPWLopsEn,
                         hwLpBipExcAlarmEn=hwLpBipExcAlarmEn, hwPos=hwPos, hwPosFlagJ0Mode=hwPosFlagJ0Mode,
                         hwEthernetDuplex=hwEthernetDuplex, hwEthernetFlagJ0Mode=hwEthernetFlagJ0Mode,
                         hwSDHAllEn=hwSDHAllEn, hwDslImaLinkReTxUsable=hwDslImaLinkReTxUsable,
                         hwPhysicalPortSdhErrorLowThreshold=hwPhysicalPortSdhErrorLowThreshold,
                         hwSfbereAlarm=hwSfbereAlarm, hwPhysicalPortOutputEnabledDown=hwPhysicalPortOutputEnabledDown,
                         hwHpB3ExcAlarmEn=hwHpB3ExcAlarmEn, hwLcdAlarmResume=hwLcdAlarmResume,
                         hwVc12DownE1AisAlarmEn=hwVc12DownE1AisAlarmEn,
                         hwJtrUdrExcResumeThreshold=hwJtrUdrExcResumeThreshold,
                         hwAtmPwMisorderPktExcAlarmResume=hwAtmPwMisorderPktExcAlarmResume,
                         hwLrdiAlarmResume=hwLrdiAlarmResume, hwSDHHpPerfCurrentFEUAS=hwSDHHpPerfCurrentFEUAS,
                         hwLaserAutoShutAlarmEn=hwLaserAutoShutAlarmEn,
                         hwPhysicalAutoShutLaserOpenInterval=hwPhysicalAutoShutLaserOpenInterval,
                         hwDs1PWClockDomain=hwDs1PWClockDomain, hwEthernetPortMode=hwEthernetPortMode,
                         hwPhysicalPortInSlot=hwPhysicalPortInSlot, hwPosFlagJ1Mode=hwPosFlagJ1Mode,
                         hwCposE1DownE1AisAlarmResume=hwCposE1DownE1AisAlarmResume,
                         hwBundleSerialCrcVerifyCode=hwBundleSerialCrcVerifyCode, hwCposFlagJ2Value=hwCposFlagJ2Value,
                         hwPortAlarmDownEnable=hwPortAlarmDownEnable, hwCposFlagJ2Trace=hwCposFlagJ2Trace,
                         hwAtmChcsAlarmEn=hwAtmChcsAlarmEn, hwE1DownE1AisAlarm=hwE1DownE1AisAlarm, hwCpos=hwCpos,
                         hwPhysicalPortSymbolErrorStatistics=hwPhysicalPortSymbolErrorStatistics,
                         hwDslLinkFrameResume=hwDslLinkFrameResume, hwSDHRsPerfCurrentUAS=hwSDHRsPerfCurrentUAS,
                         hwOutputErrorAlarmResume=hwOutputErrorAlarmResume, hwDs3Cable=hwDs3Cable,
                         hwPosClock=hwPosClock, hwSDHHpPerfCurrentTable=hwSDHHpPerfCurrentTable,
                         hwAtmPwUnknownCellExcAlarm=hwAtmPwUnknownCellExcAlarm, hwMsB2SdAlarmEn=hwMsB2SdAlarmEn,
                         hwDslGroup=hwDslGroup, hwSDHRsMsPerfCurrentTable=hwSDHRsMsPerfCurrentTable,
                         hwV5VcaisAlarm=hwV5VcaisAlarm, hwE1EsTcaAlarmResume=hwE1EsTcaAlarmResume,
                         hwPortAlarmInverseAutoRecover=hwPortAlarmInverseAutoRecover, hwLpTuAisAlarmEn=hwLpTuAisAlarmEn,
                         hwLpTimAlarmEn=hwLpTimAlarmEn, hwE1EsTcaAlarm=hwE1EsTcaAlarm,
                         hwEthernetFlagJ0Value=hwEthernetFlagJ0Value, hwDs3FrameFormat=hwDs3FrameFormat,
                         hwCesMalPktExcAlarmResume=hwCesMalPktExcAlarmResume,
                         hwJtrOvrExcResumeThreshold=hwJtrOvrExcResumeThreshold,
                         hwCesLopsAlarmResume=hwCesLopsAlarmResume, hwDslGroupEnable=hwDslGroupEnable,
                         hwSfbereAlarmResume=hwSfbereAlarmResume, hwAtmPWUnknownCellEn=hwAtmPWUnknownCellEn,
                         hwStrayPktExcResumeThreshold=hwStrayPktExcResumeThreshold, hwEthernet=hwEthernet,
                         hwPDHPerfCurrentBBE=hwPDHPerfCurrentBBE, hwDs0ChannelBundleEntry=hwDs0ChannelBundleEntry,
                         hwVrfiAlarmResume=hwVrfiAlarmResume, hwCesPWOppositeRAIEn=hwCesPWOppositeRAIEn,
                         hwUhcsAlarmResume=hwUhcsAlarmResume, hwPhysicalPortCrcErrorResume=hwPhysicalPortCrcErrorResume,
                         hwE1DownE1AisAlarmResume=hwE1DownE1AisAlarmResume, hwDslGroupRowStatus=hwDslGroupRowStatus,
                         hwDs3ChannelType=hwDs3ChannelType, hwCesLosPktExcAlarmResume=hwCesLosPktExcAlarmResume,
                         hwCposFlagC2Value=hwCposFlagC2Value, hwPWAlarmTable=hwPWAlarmTable, hwOofAlarm=hwOofAlarm,
                         hwDslGroupVci=hwDslGroupVci, hwAtmPWMisorderPktEn=hwAtmPWMisorderPktEn,
                         hwPhysicalPortDelayTime=hwPhysicalPortDelayTime, hwMsRdiAlarmEn=hwMsRdiAlarmEn,
                         hwPortGroups=hwPortGroups, hwBundleSerialLoopback=hwBundleSerialLoopback)
