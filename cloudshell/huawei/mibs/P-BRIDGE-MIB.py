#
# PySNMP MIB module P-BRIDGE-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/P-BRIDGE-MIB
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
(dot1dTpPort, dot1dBridge, dot1dTp, dot1dBasePortEntry, dot1dBasePort,) = mibBuilder.importSymbols("BRIDGE-MIB",
                                                                                                   "dot1dTpPort",
                                                                                                   "dot1dBridge",
                                                                                                   "dot1dTp",
                                                                                                   "dot1dBasePortEntry",
                                                                                                   "dot1dBasePort")
(NotificationGroup, ModuleCompliance, ObjectGroup,) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup",
                                                                               "ModuleCompliance", "ObjectGroup")
(Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks,
 Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32,) = mibBuilder.importSymbols(
    "SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType",
    "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso",
    "ObjectIdentity", "Bits", "Counter32")
(TruthValue, TimeInterval, DisplayString, TextualConvention, MacAddress,) = mibBuilder.importSymbols("SNMPv2-TC",
                                                                                                     "TruthValue",
                                                                                                     "TimeInterval",
                                                                                                     "DisplayString",
                                                                                                     "TextualConvention",
                                                                                                     "MacAddress")
pBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 6)).setRevisions(("2006-01-09 00:00", "1999-08-25 00:00",))
pBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1))


class EnabledStatus(Integer32, TextualConvention):
    # print 'in huawei-p-bridge-mib EnabledStatus', '#' * 20

    subtypeSpec = Integer32.subtypeSpec + SingleValueConstraint(1, 2, )
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), )
    # print 'in huawei-p-bridge-mib EnabledStatus END', '#' * 20


dot1dExtBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 1))
dot1dPriority = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 2))
dot1dGarp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 3))
dot1dGmrp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 1, 4))
dot1dDeviceCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 1), Bits().clone(
    namedValues=NamedValues(("dot1dExtendedFilteringServices", 0), ("dot1dTrafficClasses", 1),
                            ("dot1qStaticEntryIndividualPort", 2), ("dot1qIVLCapable", 3), ("dot1qSVLCapable", 4),
                            ("dot1qHybridCapable", 5), ("dot1qConfigurablePvidTagging", 6),
                            ("dot1dLocalVlanCapable", 7), ))).setMaxAccess("readonly")
dot1dTrafficClassesEnabled = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 2), TruthValue().clone('true')).setMaxAccess(
    "readwrite")
dot1dGmrpStatus = MibScalar((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 3), EnabledStatus().clone('enabled')).setMaxAccess(
    "readwrite")
dot1dPortCapabilitiesTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4), )
dot1dPortCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1), )
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortCapabilitiesEntry"))
dot1dPortCapabilitiesEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dPortCapabilities = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 1, 4, 1, 1), Bits().clone(
    namedValues=NamedValues(("dot1qDot1qTagging", 0), ("dot1qConfigurableAcceptableFrameTypes", 1),
                            ("dot1qIngressFiltering", 2), ))).setMaxAccess("readonly")
dot1dPortPriorityTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1), )
dot1dPortPriorityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortPriorityEntry"))
dot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dPortDefaultUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 1),
                                              Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess(
    "readwrite")
dot1dPortNumTrafficClasses = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 1, 1, 2),
                                            Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess(
    "readwrite")
dot1dUserPriorityRegenTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2), )
dot1dUserPriorityRegenEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1), ).setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dUserPriority"))
dot1dUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 1),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
dot1dRegenUserPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 2, 1, 2),
                                        Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess(
    "readwrite")
dot1dTrafficClassTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3), )
dot1dTrafficClassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1), ).setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dTrafficClassPriority"))
dot1dTrafficClassPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 1),
                                           Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
dot1dTrafficClass = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 3, 1, 2),
                                   Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess(
    "readwrite")
dot1dPortOutboundAccessPriorityTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4), )
dot1dPortOutboundAccessPriorityEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1), ).setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "P-BRIDGE-MIB", "dot1dRegenUserPriority"))
dot1dPortOutboundAccessPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 2, 4, 1, 1), Integer32().subtype(
    subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
dot1dPortGarpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1), )
dot1dPortGarpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortGarpEntry"))
dot1dPortGarpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dPortGarpJoinTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 1), TimeInterval().clone(20)).setMaxAccess(
    "readwrite")
dot1dPortGarpLeaveTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 2),
                                        TimeInterval().clone(60)).setMaxAccess("readwrite")
dot1dPortGarpLeaveAllTime = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 3, 1, 1, 3),
                                           TimeInterval().clone(1000)).setMaxAccess("readwrite")
dot1dPortGmrpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1), )
dot1dPortGmrpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("P-BRIDGE-MIB", "dot1dPortGmrpEntry"))
dot1dPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dPortGmrpStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 1),
                                     EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
dot1dPortGmrpFailedRegistrations = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 2), Counter32()).setMaxAccess(
    "readonly")
dot1dPortGmrpLastPduOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 3), MacAddress()).setMaxAccess(
    "readonly")
dot1dPortRestrictedGroupRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 1, 1, 4),
                                                      TruthValue().clone('false')).setMaxAccess("readwrite")
dot1dTpHCPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 5), )
dot1dTpHCPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 5, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpHCPortInFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 1), Counter64()).setMaxAccess("readonly")
dot1dTpHCPortOutFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 2), Counter64()).setMaxAccess("readonly")
dot1dTpHCPortInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 5, 1, 3), Counter64()).setMaxAccess("readonly")
dot1dTpPortOverflowTable = MibTable((1, 3, 6, 1, 2, 1, 17, 4, 6), )
dot1dTpPortOverflowEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 4, 6, 1), ).setIndexNames(
    (0, "BRIDGE-MIB", "dot1dTpPort"))
dot1dTpPortInOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 1), Counter32()).setMaxAccess("readonly")
dot1dTpPortOutOverflowFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 2), Counter32()).setMaxAccess("readonly")
dot1dTpPortInOverflowDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 4, 6, 1, 3), Counter32()).setMaxAccess("readonly")
pBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2))
pBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2, 1))
pBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 6, 2, 2))
pBridgeExtCapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 1)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dDeviceCapabilities"), ("P-BRIDGE-MIB", "dot1dPortCapabilities"),))
pBridgeDeviceGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 2)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dGmrpStatus"),))
pBridgeDevicePriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 3)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dTrafficClassesEnabled"),))
pBridgeDefaultPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 4)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dPortDefaultUserPriority"),))
pBridgeRegenPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 5)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dRegenUserPriority"),))
pBridgePriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 6)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dPortNumTrafficClasses"), ("P-BRIDGE-MIB", "dot1dTrafficClass"),))
pBridgeAccessPriorityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 7)).setObjects(
    *(("P-BRIDGE-MIB", "dot1dPortOutboundAccessPriority"),))
pBridgePortGarpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 8)).setObjects(*(
("P-BRIDGE-MIB", "dot1dPortGarpJoinTime"), ("P-BRIDGE-MIB", "dot1dPortGarpLeaveTime"),
("P-BRIDGE-MIB", "dot1dPortGarpLeaveAllTime"),))
pBridgePortGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 9)).setObjects(*(
("P-BRIDGE-MIB", "dot1dPortGmrpStatus"), ("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"),
("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"),))
pBridgeHCPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 10)).setObjects(*(
("P-BRIDGE-MIB", "dot1dTpHCPortInFrames"), ("P-BRIDGE-MIB", "dot1dTpHCPortOutFrames"),
("P-BRIDGE-MIB", "dot1dTpHCPortInDiscards"),))
pBridgePortOverflowGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 11)).setObjects(*(
("P-BRIDGE-MIB", "dot1dTpPortInOverflowFrames"), ("P-BRIDGE-MIB", "dot1dTpPortOutOverflowFrames"),
("P-BRIDGE-MIB", "dot1dTpPortInOverflowDiscards"),))
pBridgePortGmrpGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 6, 2, 1, 12)).setObjects(*(
("P-BRIDGE-MIB", "dot1dPortGmrpStatus"), ("P-BRIDGE-MIB", "dot1dPortGmrpFailedRegistrations"),
("P-BRIDGE-MIB", "dot1dPortGmrpLastPduOrigin"), ("P-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"),))
pBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 6, 2, 2, 1)).setObjects(*(
("P-BRIDGE-MIB", "pBridgeExtCapGroup"), ("P-BRIDGE-MIB", "pBridgeDeviceGmrpGroup"),
("P-BRIDGE-MIB", "pBridgeDevicePriorityGroup"), ("P-BRIDGE-MIB", "pBridgeDefaultPriorityGroup"),
("P-BRIDGE-MIB", "pBridgeRegenPriorityGroup"), ("P-BRIDGE-MIB", "pBridgePriorityGroup"),
("P-BRIDGE-MIB", "pBridgeAccessPriorityGroup"), ("P-BRIDGE-MIB", "pBridgePortGarpGroup"),
("P-BRIDGE-MIB", "pBridgePortGmrpGroup"), ("P-BRIDGE-MIB", "pBridgeHCPortGroup"),
("P-BRIDGE-MIB", "pBridgePortOverflowGroup"),))
pBridgeCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 6, 2, 2, 2)).setObjects(*(
("P-BRIDGE-MIB", "pBridgeExtCapGroup"), ("P-BRIDGE-MIB", "pBridgeDeviceGmrpGroup"),
("P-BRIDGE-MIB", "pBridgeDevicePriorityGroup"), ("P-BRIDGE-MIB", "pBridgeDefaultPriorityGroup"),
("P-BRIDGE-MIB", "pBridgeRegenPriorityGroup"), ("P-BRIDGE-MIB", "pBridgePriorityGroup"),
("P-BRIDGE-MIB", "pBridgeAccessPriorityGroup"), ("P-BRIDGE-MIB", "pBridgePortGarpGroup"),
("P-BRIDGE-MIB", "pBridgePortGmrpGroup2"), ("P-BRIDGE-MIB", "pBridgeHCPortGroup"),
("P-BRIDGE-MIB", "pBridgePortOverflowGroup"),))
mibBuilder.exportSymbols("P-BRIDGE-MIB", dot1dTpHCPortEntry=dot1dTpHCPortEntry,
                         dot1dPortCapabilitiesTable=dot1dPortCapabilitiesTable,
                         pBridgePortGmrpGroup=pBridgePortGmrpGroup,
                         dot1dPortGmrpFailedRegistrations=dot1dPortGmrpFailedRegistrations,
                         dot1dUserPriorityRegenEntry=dot1dUserPriorityRegenEntry,
                         dot1dDeviceCapabilities=dot1dDeviceCapabilities,
                         dot1dPortCapabilitiesEntry=dot1dPortCapabilitiesEntry, EnabledStatus=EnabledStatus,
                         dot1dPortGarpJoinTime=dot1dPortGarpJoinTime, pBridgeMIBObjects=pBridgeMIBObjects,
                         dot1dPortGarpTable=dot1dPortGarpTable,
                         dot1dPortOutboundAccessPriorityEntry=dot1dPortOutboundAccessPriorityEntry,
                         dot1dPortNumTrafficClasses=dot1dPortNumTrafficClasses,
                         dot1dTrafficClassPriority=dot1dTrafficClassPriority,
                         dot1dTpPortOverflowTable=dot1dTpPortOverflowTable,
                         dot1dPortGmrpLastPduOrigin=dot1dPortGmrpLastPduOrigin,
                         pBridgePriorityGroup=pBridgePriorityGroup, dot1dTrafficClassEntry=dot1dTrafficClassEntry,
                         dot1dTpHCPortInDiscards=dot1dTpHCPortInDiscards,
                         dot1dPortOutboundAccessPriorityTable=dot1dPortOutboundAccessPriorityTable,
                         pBridgePortOverflowGroup=pBridgePortOverflowGroup, pBridgeExtCapGroup=pBridgeExtCapGroup,
                         dot1dExtBase=dot1dExtBase, dot1dPortGarpLeaveAllTime=dot1dPortGarpLeaveAllTime,
                         pBridgeCompliances=pBridgeCompliances, dot1dTpPortOverflowEntry=dot1dTpPortOverflowEntry,
                         pBridgePortGmrpGroup2=pBridgePortGmrpGroup2, pBridgeCompliance=pBridgeCompliance,
                         dot1dTpPortOutOverflowFrames=dot1dTpPortOutOverflowFrames,
                         pBridgeDevicePriorityGroup=pBridgeDevicePriorityGroup,
                         pBridgeDefaultPriorityGroup=pBridgeDefaultPriorityGroup,
                         dot1dTpPortInOverflowFrames=dot1dTpPortInOverflowFrames, dot1dGarp=dot1dGarp,
                         pBridgeHCPortGroup=pBridgeHCPortGroup, dot1dPortGmrpEntry=dot1dPortGmrpEntry,
                         PYSNMP_MODULE_ID=pBridgeMIB,
                         dot1dPortRestrictedGroupRegistration=dot1dPortRestrictedGroupRegistration, dot1dGmrp=dot1dGmrp,
                         dot1dRegenUserPriority=dot1dRegenUserPriority, dot1dPortPriorityEntry=dot1dPortPriorityEntry,
                         pBridgeCompliance2=pBridgeCompliance2,
                         dot1dPortDefaultUserPriority=dot1dPortDefaultUserPriority,
                         dot1dTpHCPortOutFrames=dot1dTpHCPortOutFrames, dot1dUserPriority=dot1dUserPriority,
                         dot1dPortGmrpTable=dot1dPortGmrpTable, dot1dPortGarpEntry=dot1dPortGarpEntry,
                         dot1dTrafficClassTable=dot1dTrafficClassTable,
                         dot1dPortOutboundAccessPriority=dot1dPortOutboundAccessPriority,
                         dot1dTpPortInOverflowDiscards=dot1dTpPortInOverflowDiscards,
                         pBridgeConformance=pBridgeConformance, dot1dGmrpStatus=dot1dGmrpStatus,
                         dot1dTrafficClassesEnabled=dot1dTrafficClassesEnabled, pBridgeGroups=pBridgeGroups,
                         dot1dTrafficClass=dot1dTrafficClass, dot1dPortCapabilities=dot1dPortCapabilities,
                         pBridgeMIB=pBridgeMIB, dot1dUserPriorityRegenTable=dot1dUserPriorityRegenTable,
                         dot1dTpHCPortInFrames=dot1dTpHCPortInFrames, dot1dPortGarpLeaveTime=dot1dPortGarpLeaveTime,
                         pBridgeRegenPriorityGroup=pBridgeRegenPriorityGroup,
                         dot1dPortPriorityTable=dot1dPortPriorityTable, dot1dPortGmrpStatus=dot1dPortGmrpStatus,
                         pBridgeAccessPriorityGroup=pBridgeAccessPriorityGroup,
                         pBridgePortGarpGroup=pBridgePortGarpGroup, pBridgeDeviceGmrpGroup=pBridgeDeviceGmrpGroup,
                         dot1dPriority=dot1dPriority, dot1dTpHCPortTable=dot1dTpHCPortTable)
