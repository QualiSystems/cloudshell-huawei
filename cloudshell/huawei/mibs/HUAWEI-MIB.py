#
# PySNMP MIB module HUAWEI-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/HUAWEI-MIB
# Produced by pysmi-0.2.2 at Tue Apr 30 13:26:34 2019
# On host ? platform ? version ? by user ?
# Using Python version 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols(
    "ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint",
    "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols(
    "SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType",
    "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32",
    "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
huawei = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011))
if mibBuilder.loadTexts: huawei.setLastUpdated('200601250000Z')
if mibBuilder.loadTexts: huawei.setOrganization('Fix-Net Dept, Huawei Technologies Co.,Ltd.')
hwLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1))
quidway = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 1))
hwTrans = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 2))
hwInternetProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3))
rmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 4))
performance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4))
hwNovellProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 1, 4))
hwProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 1))
atmAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 1, 1))
atmBone = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 1, 2))
r8750 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 1, 2, 1))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2))
routerGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 1))
ne08 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 7508))
ne16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 7516))
attr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 1, 1))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 2))
flash = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 3))
mixinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 4))
huaweiMemoryPool = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 5))
configFile = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 6))
netEngine = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 2, 8070))
access_server = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 3)).setLabel("access-server")
as8010 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 3, 1))
lan_switch = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4)).setLabel("lan-switch")
switch2403 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 1))
switch2403F = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 1, 0))
switch3008 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 2))
switch3016 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 3))
switch2024_M = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 4)).setLabel("switch2024-M")
switch3025_M = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 4, 5)).setLabel("switch3025-M")
xdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 5))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 5, 1))
musa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6))
hwMusaV100R001Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 1))
hwMA5200Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 2))
hwMusaV100R002Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 3))
hwMd5500Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 4))
hwMa5100Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 5))
hwMa5300Mib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 6))
ias = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 6, 7))
mpeg_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 7)).setLabel("mpeg-2")
gprs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 8))
honet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 9))
cc08 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 10))
sbs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 11))
ip_phone = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 12)).setLabel("ip-phone")
ups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 13))
viewpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 14))
netManager = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15))
iNet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 16))
ne80 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 17))
wireIn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18))
wireInScp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18, 1))
wireInSdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18, 2))
wireInSmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18, 3))
wireInSsp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18, 4))
wireInIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 18, 5))
mobileIn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19))
mobileInScp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19, 1))
mobileInSdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19, 2))
mobileInSmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19, 3))
mobileInSsp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19, 4))
mobileInIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 19, 5))
cdmaIn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20))
cdmaInScp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20, 1))
cdmaInSdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20, 2))
cdmaInSmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20, 3))
cdmaInSsp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20, 4))
cdmaInIP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 20, 5))
acdIn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 21))
esr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22))
radium8750 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 2))
isn8850 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 3))
esr8825 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 5))
esrV5R3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 6))
esrV5R58850 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 7))
esrV5R58825 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 22, 8))
lanSw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23))
lswCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1))
s8016 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 11))
s8016Common = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 1))
s8016A = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 2))
s8016B = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 11, 3))
s3526 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 12))
s3026 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 13))
s3026V = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 14))
s2008 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 15))
s2016 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 16))
s3526F = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 17))
s5516 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 18))
s6506 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 19))
s3026F = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 20))
s3526E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 21))
s2026 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 22))
s2403H = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 23))
s3026E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 24))
s3050C = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 29))
s6503 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 30))
s8512 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 31))
s8505 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 32))
s6506R = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 33))
s3026c = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 34))
s3026g = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 35))
s3026t = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 36))
s3552G = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 37))
s3552P = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 38))
s3528G = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 39))
s3528P = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 40))
s3526c = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 41))
s3026c_24_12fs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 42)).setLabel("s3026c-24-12fs")
s3026c_24_12fm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 43)).setLabel("s3026c-24-12fm")
s3526c_24_12fs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 44)).setLabel("s3526c-24-12fs")
s3526c_24_12fm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 45)).setLabel("s3526c-24-12fm")
s5012G = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 46))
s5012G_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 47)).setLabel("s5012G-DC")
s5012T_12_10GBC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 48)).setLabel("s5012T-12-10GBC")
s5012T_12_10GBC_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 49)).setLabel("s5012T-12-10GBC-DC")
s5024G_24_20TP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 50)).setLabel("s5024G-24-20TP")
s5024G_24_20TP_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 51)).setLabel("s5024G-24-20TP-DC")
s2026Z = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 52))
s2026C = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 53))
s3026G_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 54)).setLabel("s3026G-SI")
s3026C_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 55)).setLabel("s3026C-SI")
s3026S_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 56)).setLabel("s3026S-SI")
s8505e = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 57))
s3552F_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 67)).setLabel("s3552F-SI")
s3552F_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 68)).setLabel("s3552F-EI")
e026 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 69))
e026_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 70)).setLabel("e026-SI")
e050 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 71))
s2326P_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 72)).setLabel("s2326P-SI")
s2326P_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 73)).setLabel("s2326P-EI")
s2318P_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 74)).setLabel("s2318P-SI")
s2318P_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 75)).setLabel("s2318P-EI")
s2309P_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 76)).setLabel("s2309P-SI")
s2309P_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 77)).setLabel("s2309P-EI")
s3352P_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 78)).setLabel("s3352P-SI")
s3352P_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 79)).setLabel("s3352P-EI")
s3328TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 80)).setLabel("s3328TP-SI")
s3328TP_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 81)).setLabel("s3328TP-EI")
s3328TP_EI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 82)).setLabel("s3328TP-EI-24S")
s3328TP_SI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 83)).setLabel("s3328TP-SI-24S")
s3352P_EI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 84)).setLabel("s3352P-EI-24S")
s3352P_EI_48S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 85)).setLabel("s3352P-EI-48S")
s3352P_SI_48S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 86)).setLabel("s3352P-SI-48S")
s2309TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 87)).setLabel("s2309TP-SI")
s2309TP_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 88)).setLabel("s2309TP-EI")
s2318TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 89)).setLabel("s2318TP-SI")
s2318TP_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 90)).setLabel("s2318TP-EI")
s2326TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 91)).setLabel("s2326TP-SI")
s2326TP_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 92)).setLabel("s2326TP-EI")
s2352P_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 93)).setLabel("s2352P-SI")
s2352P_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 94)).setLabel("s2352P-EI")
s5328C_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 95)).setLabel("s5328C-EI")
s5328C_EI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 96)).setLabel("s5328C-EI-24S")
s5352C_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 97)).setLabel("s5352C-EI")
s5324TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 98)).setLabel("s5324TP-SI")
s5348TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 99)).setLabel("s5348TP-SI")
s5324TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 100)).setLabel("s5324TP-PWR-SI")
s5348TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 101)).setLabel("s5348TP-PWR-SI")
s5328C_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 102)).setLabel("s5328C-SI")
s5352C_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 103)).setLabel("s5352C-SI")
s5328C_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 104)).setLabel("s5328C-PWR-SI")
s5352C_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 105)).setLabel("s5352C-PWR-SI")
s5328C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 106)).setLabel("s5328C-PWR-EI")
s5352C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 107)).setLabel("s5352C-PWR-EI")
s2309TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 108)).setLabel("s2309TP-PWR-EI")
s2326TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 109)).setLabel("s2326TP-PWR-EI")
s3328TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 110)).setLabel("s3328TP-PWR-EI")
s3352P_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 111)).setLabel("s3352P-PWR-EI")
s3328TP_EI_MC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 112)).setLabel("s3328TP-EI-MC")
s3318TP_EI_MC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 113)).setLabel("s3318TP-EI-MC")
s2700_9TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 114)).setLabel("s2700-9TP-EI-AC")
s2700_9TP_EI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 115)).setLabel("s2700-9TP-EI-DC")
s2700_18TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 116)).setLabel("s2700-18TP-EI-AC")
s2700_26TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 117)).setLabel("s2700-26TP-EI-AC")
s2700_26TP_EI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 118)).setLabel("s2700-26TP-EI-DC")
s2700_52TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 119)).setLabel("s2700-52TP-EI-AC")
s2700_9TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 120)).setLabel("s2700-9TP-SI-AC")
s2700_18TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 121)).setLabel("s2700-18TP-SI-AC")
s2700_26TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 122)).setLabel("s2700-26TP-SI-AC")
s2700_9TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 123)).setLabel("s2700-9TP-PWR-EI")
s2700_26TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 124)).setLabel("s2700-26TP-PWR-EI")
s3700_28TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 125)).setLabel("s3700-28TP-EI-AC")
s3700_28TP_EI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 126)).setLabel("s3700-28TP-EI-DC")
s3700_28TP_EI_24S_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 127)).setLabel("s3700-28TP-EI-24S-AC")
s3700_52TP_EI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 128)).setLabel("s3700-52TP-EI-AC")
s3700_52TP_EI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 129)).setLabel("s3700-52TP-EI-DC")
s3700_52TP_EI_24S_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 130)).setLabel("s3700-52TP-EI-24S-AC")
s3700_52TP_EI_24S_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 131)).setLabel("s3700-52TP-EI-24S-DC")
s3700_52TP_EI_48S_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 132)).setLabel("s3700-52TP-EI-48S-AC")
s3700_52TP_EI_48S_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 133)).setLabel("s3700-52TP-EI-48S-DC")
s3700_28TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 134)).setLabel("s3700-28TP-SI-AC")
s3700_28TP_SI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 135)).setLabel("s3700-28TP-SI-DC")
s3700_52TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 136)).setLabel("s3700-52TP-SI-AC")
s3700_28TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 137)).setLabel("s3700-28TP-PWR-EI")
s3700_52TP_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 138)).setLabel("s3700-52TP-PWR-EI")
s3700_28TP_EI_MC_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 139)).setLabel("s3700-28TP-EI-MC-AC")
s5700_28C_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 140)).setLabel("s5700-28C-EI")
s5700_28C_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 141)).setLabel("s5700-28C-SI")
s5700_28C_EI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 142)).setLabel("s5700-28C-EI-24S")
s5700_52C_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 143)).setLabel("s5700-52C-EI")
s5700_52C_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 144)).setLabel("s5700-52C-SI")
s5700_24TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 145)).setLabel("s5700-24TP-SI-AC")
s5700_24TP_SI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 146)).setLabel("s5700-24TP-SI-DC")
s5700_48TP_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 147)).setLabel("s5700-48TP-SI-AC")
s5700_48TP_SI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 148)).setLabel("s5700-48TP-SI-DC")
s5700_28C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 149)).setLabel("s5700-28C-PWR-EI")
s5700_52C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 150)).setLabel("s5700-52C-PWR-EI")
s5700_24TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 151)).setLabel("s5700-24TP-PWR-SI")
s5700_48TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 152)).setLabel("s5700-48TP-PWR-SI")
s6324C = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 153))
s6348C = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 154))
s5328C_HI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 155)).setLabel("s5328C-HI")
s5328C_HI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 156)).setLabel("s5328C-HI-24S")
s5306TP_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 157)).setLabel("s5306TP-SI")
s3326C_HI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 158)).setLabel("s3326C-HI")
s5328C_HI_24SA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 159)).setLabel("s5328C-HI-24SA")
s6700_24_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 160)).setLabel("s6700-24-EI")
s6700_48_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 161)).setLabel("s6700-48-EI")
s1728_GWR_4P = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 162)).setLabel("s1728-GWR-4P")
s5700_28P_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 163)).setLabel("s5700-28P-LI")
s5700_28P_PWR_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 164)).setLabel("s5700-28P-PWR-LI-AC")
s5700_52P_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 165)).setLabel("s5700-52P-LI")
s5700_52P_PWR_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 166)).setLabel("s5700-52P-PWR-LI-AC")
s5700_28X_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 167)).setLabel("s5700-28X-EI")
s5700_52X_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 168)).setLabel("s5700-52X-EI")
s5700_28C_HI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 169)).setLabel("s5700-28C-HI")
s5700_28C_HI_24S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 170)).setLabel("s5700-28C-HI-24S")
s5700_6TP_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 171)).setLabel("s5700-6TP-LI-AC")
s3700_26C_HI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 172)).setLabel("s3700-26C-HI")
s5300_28C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 173)).setLabel("s5300-28C-PWR-EI")
s5300_52C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 174)).setLabel("s5300-52C-PWR-EI")
s5310_28P_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 175)).setLabel("s5310-28P-LI")
s5310_52P_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 176)).setLabel("s5310-52P-LI")
s5700_28P_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 177)).setLabel("s5700-28P-LI-DC")
s5700_52P_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 178)).setLabel("s5700-52P-LI-DC")
s5310_28P_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 179)).setLabel("s5310-28P-LI-DC")
s5310_52P_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 180)).setLabel("s5310-52P-LI-DC")
s5700S_28P_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 181)).setLabel("s5700S-28P-LI-AC")
s5700S_52P_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 182)).setLabel("s5700S-52P-LI-AC")
s1700_28GFR_4P_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 183)).setLabel("s1700-28GFR-4P-AC")
s1700_52GFR_4P_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 184)).setLabel("s1700-52GFR-4P-AC")
s1700_28FR_2T2P_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 185)).setLabel("s1700-28FR-2T2P-AC")
s1700_52FR_2T2P_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 186)).setLabel("s1700-52FR-2T2P-AC")
s5700_28C_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 187)).setLabel("s5700-28C-PWR-SI")
s5700_52C_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 188)).setLabel("s5700-52C-PWR-SI")
s5710_28C_PWR_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 189)).setLabel("s5710-28C-PWR-LI")
s5710_52C_PWR_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 190)).setLabel("s5710-52C-PWR-LI")
s5710_28C_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 191)).setLabel("s5710-28C-LI")
s5710_52C_LI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 192)).setLabel("s5710-52C-LI")
e6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 193))
s5710_28C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 194)).setLabel("s5710-28C-PWR-EI")
s5710_52C_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 195)).setLabel("s5710-52C-PWR-EI")
s2710_26TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 196)).setLabel("s2710-26TP-PWR-SI")
s2710_52P_SI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 197)).setLabel("s2710-52P-SI-AC")
s2710_52P_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 198)).setLabel("s2710-52P-PWR-SI")
s2700_52P_PWR_EI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 199)).setLabel("s2700-52P-PWR-EI")
s3700_52P_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 200)).setLabel("s3700-52P-PWR-SI")
s3700_28TP_PWR_SI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 201)).setLabel("s3700-28TP-PWR-SI")
s5710_108C_PWR_HI = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 202)).setLabel("s5710-108C-PWR-HI")
s5700_10P_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 203)).setLabel("s5700-10P-LI-AC")
s5700_10P_PWR_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 204)).setLabel("s5700-10P-PWR-LI-AC")
s5700_26X_SI_12S_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 205)).setLabel("s5700-26X-SI-12S-AC")
s5700_28X_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 206)).setLabel("s5700-28X-LI-AC")
s5700_28X_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 207)).setLabel("s5700-28X-LI-DC")
s5700_52X_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 208)).setLabel("s5700-52X-LI-AC")
s5700_52X_LI_DC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 209)).setLabel("s5700-52X-LI-DC")
s5700_28X_PWR_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 210)).setLabel("s5700-28X-PWR-LI-AC")
s5700_52X_PWR_LI_AC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 211)).setLabel("s5700-52X-PWR-LI-AC")
apon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 24))
ma5101 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 24, 1))
ma5102 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 24, 2))
transmission = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25))
optix155622H = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 1))
optix10Gv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 2))
hsr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 26))
ne16E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 26, 1))
ne08E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 26, 2))
ne05 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 26, 3))
amg5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 27))
umg8900 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 28))
ne20 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 29))
ne20s = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 30))
ne40 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 31))
wcdma = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 32))
sgsn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 32, 1))
mlsr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33))
dslw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34))
dlswNode = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 1))
dlswTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 2))
dlswInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 3))
dlswDirectory = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 4))
dlswCircuit = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 5))
dlswSdlc = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 6))
dlswLlc2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 34, 7))
sm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 35))
mmsc = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 35, 1))
pysmi_as = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 36)).setLabel("as")
p3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 37))
iad = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 38))
iad132 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 38, 1))
wlanAp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39))
wlanApCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 1))
wlanApWA1003 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 2))
wlanApWA1003A = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 3))
wlanApWA1005 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 4))
wlanApWA1008 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 5))
wlanApWA1208 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 6))
wlanApWA1208H = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 7))
wlanApWA1006E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 8))
wlanBridgeWB2010 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 9))
wlanBridgeWB2011 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 10))
wa1208E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 39, 11))
hwinfoX = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 40))
wlanApWA1006 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 43))
ar46_20 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 44)).setLabel("ar46-20")
ar46_40 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 45)).setLabel("ar46-40")
ar46_80 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 46)).setLabel("ar46-80")
ne20_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 47)).setLabel("ne20-2")
ne20_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 48)).setLabel("ne20-4")
ne20_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 49)).setLabel("ne20-8")
eudemon200 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 50))
eudemon1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 51))
vdg10_40 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 52)).setLabel("vdg10-40")
vdg10_41 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 53)).setLabel("vdg10-41")
hwSps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 54))
ar18_18 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 55)).setLabel("ar18-18")
ar18_20 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 56)).setLabel("ar18-20")
ar18_30 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 57)).setLabel("ar18-30")
ar18_31 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 58)).setLabel("ar18-31")
ar18_32 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 59)).setLabel("ar18-32")
ar18_33 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 60)).setLabel("ar18-33")
ar18_34 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 61)).setLabel("ar18-34")
ne5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62))
ne5000SysOid = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2))
ne5000oem = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 1))
ne80E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 2))
ne5000E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 3))
ne5000EMulti = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 4))
ne40E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 5))
ne5000E_BTB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 6)).setLabel("ne5000E-BTB")
ne40E_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 7)).setLabel("ne40E-4")
ne40E_X3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 8)).setLabel("ne40E-X3")
ne40E_X8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 9)).setLabel("ne40E-X8")
ne40E_X16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 10)).setLabel("ne40E-X16")
ne5000E_X16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 11)).setLabel("ne5000E-X16")
ne40E_X1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 12)).setLabel("ne40E-X1")
ne40E_X2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 13)).setLabel("ne40E-X2")
ne40E_X1_M4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 14)).setLabel("ne40E-X1-M4")
ne40E_X2_M8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 15)).setLabel("ne40E-X2-M8")
ne40E_X2_M16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 62, 2, 16)).setLabel("ne40E-X2-M16")
ggsn9811 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 63))
pdsn9660 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 64))
eudemon2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 65))
eudemon2200 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 66))
ua5000ipm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 72))
rm9000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 73))
hwIMAPNorthbound = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 74))
hwBITS = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 75))
hwPv8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 76))
eudemon500 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 77))
ua5000IpmB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 78))
ua5000ApmB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 79))
ma5600 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 80))
softx3000UC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 81))
hwOSTA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 82))
secpath1800F = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 83))
eudemon2300 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 84))
ma5100V600 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 85))
ma5605 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 86))
msp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87))
cX200A = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 1))
cX200B = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 2))
cX300A = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 3))
cX300B = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 4))
cX500A = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 5))
cX380 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 6))
cX600_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 7)).setLabel("cX600-8")
cX600_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 8)).setLabel("cX600-16")
cX200C = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 9))
cX200D = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 10))
cX200D_EA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 11)).setLabel("cX200D-EA")
cX200D_MC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 12)).setLabel("cX200D-MC")
cX600_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 13)).setLabel("cX600-4")
cX380_PBT = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 14)).setLabel("cX380-PBT")
cX380_ME = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 15)).setLabel("cX380-ME")
cX200D_EA_MC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 16)).setLabel("cX200D-EA-MC")
cX600_X3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 17)).setLabel("cX600-X3")
cX600_X8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 18)).setLabel("cX600-X8")
cX600_X16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 19)).setLabel("cX600-X16")
cX600_X1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 20)).setLabel("cX600-X1")
cX600_X2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 21)).setLabel("cX600-X2")
cX600_X1DO = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 22)).setLabel("cX600-X1DO")
cX600_X2DO = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 23)).setLabel("cX600-X2DO")
cX600_X3DO = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 24)).setLabel("cX600-X3DO")
cX600_X8DO = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 25)).setLabel("cX600-X8DO")
cX600_X16DO = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 26)).setLabel("cX600-X16DO")
cX600_X1_M4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 27)).setLabel("cX600-X1-M4")
cX600_X2_M8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 28)).setLabel("cX600-X2-M8")
cX600_X2_M16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 87, 29)).setLabel("cX600-X2-M16")
ne20E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 88))
ne20E_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 88, 1)).setLabel("ne20E-4")
ne20E_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 88, 2)).setLabel("ne20E-8")
ne20E_X6 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 88, 3)).setLabel("ne20E-X6")
me60 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89))
me60_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 1)).setLabel("me60-16")
me60_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 2)).setLabel("me60-8")
me60_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 3)).setLabel("me60-4")
me60_X3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 4)).setLabel("me60-X3")
me60_X8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 5)).setLabel("me60-X8")
me60_X16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 89, 6)).setLabel("me60-X16")
eudemon300 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 113))
eudemonVPN3900 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 114))
eudemonEVPN5900 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 115))
eudemon100E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 116))
eudemon200E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 117))
eudemon200S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 118))
svn3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 124))
usg5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 125))
usg9000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 126))
eudemon200s = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 127))
sig1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 129))
sig9280 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 130))
sig2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 131))
s9300 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170))
s9303 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 1))
s9306 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 2))
s9312 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 3))
vasp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 4))
s9303E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 5))
s9306E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 6))
s9312E = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 170, 7))
s7700 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 223))
s7703 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 223, 1))
s7706 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 223, 2))
s7712 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 223, 3))
s9700 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 236))
s9703 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 236, 1))
s9706 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 236, 2))
s9712 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 236, 3))
ptn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182))
ptn2900 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 1))
ptn6900 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 2))
ptn6900_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 5)).setLabel("ptn6900-16")
ptn6900_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 6)).setLabel("ptn6900-8")
ptn6900_3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 7)).setLabel("ptn6900-3")
ptn6900_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 8)).setLabel("ptn6900-2")
ptn6900_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 182, 9)).setLabel("ptn6900-1")
nse = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187))
ssp1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 1))
ssp2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 2))
ssp3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 3))
ssp1000_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 4)).setLabel("ssp1000-4")
ssp5000_X3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 8)).setLabel("ssp5000-X3")
ssp5000_X8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 9)).setLabel("ssp5000-X8")
ssp5000_X16 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 10)).setLabel("ssp5000-X16")
nse1000_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 5)).setLabel("nse1000-4")
nse1000_8 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 6)).setLabel("nse1000-8")
nse1000_X3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 187, 7)).setLabel("nse1000-X3")
atn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220))
atn980 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220, 1))
atn990 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220, 2))
atn910 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220, 3))
atn950 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220, 4))
atn950B = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 220, 5))
ar = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224))
ar1220 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 1))
ar1220w = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 2))
ar1240 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 3))
ar1240w = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 4))
ar2220 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 5))
ar2240 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 6))
ar3260 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 7))
ar1220v = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 8))
ar201 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 9))
ar206 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 10))
ar207 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 11))
ar207v = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 12))
ar208 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 13))
ar1220vw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 14))
ar1220s = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 15))
ar1220ws = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 224, 16))
s12700 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 225))
s12708 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 225, 1))
s12716 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 225, 2))
vRGW = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 227))
dcswitch = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239))
ce12804 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 1))
ce12808 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 2))
ce12812 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 3))
ce5850_54Q_EI_48T = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 4)).setLabel("ce5850-54Q-EI-48T")
ce6850_52Q_EI_48S = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 5)).setLabel("ce6850-52Q-EI-48S")
ce6850_52Q_EI_48T = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 239, 6)).setLabel("ce6850-52Q-EI-48T")
wlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 240))
acu = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 240, 1))
ac6605_lsw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 240, 2)).setLabel("ac6605-lsw")
ac6605_ac = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 240, 3)).setLabel("ac6605-ac")
huaweiExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 4))
huaweiMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5))
hwAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 1))
hwAaa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 2))
hwLam = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 3))
hwPortal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 4))
hwRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 5))
hwVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 6))
hwDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7))
hwDHCPRelayMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7, 1))
hwDHCPServerMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 7, 2))
hwVprn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 8))
hwFr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 9))
hwAtmCmRm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 10))
hwCes = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 11))
hwMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12))
hwMplsLsr = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 1))
hwMplsLdp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 2))
hwMplsVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 3))
hwMplsFtn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 4))
hwMplsVpls = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 5))
hwMplsLsp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 6))
hwMplsOam = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7))
hwPw = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 8))
hwRouteManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 13))
hwRouteManagementUrm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 13, 1))
hwRouteManagementMrm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 13, 2))
hwRouteManagementRpm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 13, 3))
hwEthernetPort = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 14))
hwVTP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 15))
hwMam = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 16))
hwArpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 17))
hwDhcpProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 18))
hwIgspSnooping = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 19))
hwGarpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 20))
hwRstpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 21))
hwPae8021xExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 22))
hwNat = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 23))
hwVlanProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 24))
hwDatacomm = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25))
hwBRASMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40))
hwImps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 26))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6))
hwEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 1))
hwPower = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 2))
hwDev = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 3))
hwNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 4))
hwMem = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 5))
hwLoadBackup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 6))
hwHgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 7))
hwIppool = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 8))
hwFlash = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 9))
hwConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 10))
hwAtmOam = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 11))
hwAtmPos = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 12))
hwHSL = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 13))
hwMTA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 14))
hwSPC = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 15))
hwV5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 16))
hwIma = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 17))
hwUcl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 18))
hwAtmSvc = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 19))
hwVPRing = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 20))
hwTest = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 21))
hwTestCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 21, 1))
hwNTest = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 21, 2))
hwBtest = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 21, 3))
hwSwitchOver = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 22))
hwVfb = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 23))
hwClk = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 25))
hwCdi = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 26))
hwAti = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 27))
hwDslamNtv = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 28))
hwServerMon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 29))
hwSyntrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 30))
hwAdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 31))
hwVdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 32))
hwHdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 33))
hwDeha = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 34))
hwSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 35))
hwVoip = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 36))
hwVrp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 37))
hwMus = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 38))
hwDns = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 39))
hwNetTest = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 40))
hwMs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 41))
hwPITP = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 42))
hwDslamMacPool = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 43))
hwDslamPPPoA = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 44))
hwDslamPvcProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 45))
hwDslamIpoa = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 46))
hwLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 47))
mibBuilder.exportSymbols("HUAWEI-MIB", eudemon300=eudemon300, s2700_26TP_EI_AC=s2700_26TP_EI_AC, s2318TP_EI=s2318TP_EI,
                         s2326P_EI=s2326P_EI, s2700_52P_PWR_EI=s2700_52P_PWR_EI, mixinfo=mixinfo,
                         ne5000E_X16=ne5000E_X16, wa1208E=wa1208E, netManager=netManager, ac6605_ac=ac6605_ac,
                         s2026Z=s2026Z, ar3260=ar3260, cX300A=cX300A, cX600_X3=cX600_X3, cX200C=cX200C,
                         s5012G_DC=s5012G_DC, ma5600=ma5600, usg9000=usg9000, s2700_52TP_EI_AC=s2700_52TP_EI_AC,
                         s3026=s3026, eudemonVPN3900=eudemonVPN3900, s3352P_EI_24S=s3352P_EI_24S,
                         s3352P_EI_48S=s3352P_EI_48S, pdsn9660=pdsn9660, atn950B=atn950B, hwFlash=hwFlash, ne08E=ne08E,
                         cX600_X3DO=cX600_X3DO, s3352P_EI=s3352P_EI, hwDev=hwDev, s5700_6TP_LI_AC=s5700_6TP_LI_AC,
                         ar18_32=ar18_32, transmission=transmission, wireInScp=wireInScp, s2318TP_SI=s2318TP_SI,
                         nse1000_8=nse1000_8, eudemon2300=eudemon2300, ar2220=ar2220, s2700_9TP_EI_DC=s2700_9TP_EI_DC,
                         s5300_52C_PWR_EI=s5300_52C_PWR_EI, s3700_28TP_EI_DC=s3700_28TP_EI_DC, ne20E_4=ne20E_4,
                         s9706=s9706, ptn=ptn, ar18_34=ar18_34, hwMplsFtn=hwMplsFtn,
                         s3700_52TP_EI_48S_DC=s3700_52TP_EI_48S_DC, hwArpProxy=hwArpProxy, s8016Common=s8016Common,
                         hwMplsLsp=hwMplsLsp, s5700_28X_EI=s5700_28X_EI, wlanApWA1006E=wlanApWA1006E, me60_8=me60_8,
                         cX300B=cX300B, s8016A=s8016A, s5700_28X_LI_AC=s5700_28X_LI_AC,
                         huaweiMemoryPool=huaweiMemoryPool, dlswTConn=dlswTConn, ne80E=ne80E, hwAtmOam=hwAtmOam,
                         hwRadius=hwRadius, s2326TP_SI=s2326TP_SI, wireInSdp=wireInSdp, softx3000UC=softx3000UC,
                         hwDslamNtv=hwDslamNtv, cX200D_MC=cX200D_MC, s5700_48TP_SI_DC=s5700_48TP_SI_DC, hwHdsl=hwHdsl,
                         ar18_20=ar18_20, s3526c_24_12fs=s3526c_24_12fs, cX600_X1DO=cX600_X1DO, cX200B=cX200B,
                         ne20_8=ne20_8, s5700_28X_PWR_LI_AC=s5700_28X_PWR_LI_AC, eudemon200=eudemon200,
                         mobileInSmp=mobileInSmp, s3700_26C_HI=s3700_26C_HI, vasp=vasp, s3526=s3526, cX600_8=cX600_8,
                         s9300=s9300, mobileInIP=mobileInIP, s5700_52X_EI=s5700_52X_EI,
                         hwInternetProtocol=hwInternetProtocol, s3352P_SI=s3352P_SI, ne20s=ne20s, s3026g=s3026g,
                         acdIn=acdIn, ce5850_54Q_EI_48T=ce5850_54Q_EI_48T, s2309P_EI=s2309P_EI,
                         s2309TP_PWR_EI=s2309TP_PWR_EI, huawei=huawei, nse=nse, s5700_28P_PWR_LI_AC=s5700_28P_PWR_LI_AC,
                         dlswDirectory=dlswDirectory, cdmaInIP=cdmaInIP, ne20E_8=ne20E_8, s9700=s9700, ar201=ar201,
                         s2700_9TP_EI_AC=s2700_9TP_EI_AC, hwIMAPNorthbound=hwIMAPNorthbound,
                         s5700_28C_EI_24S=s5700_28C_EI_24S, sig2000=sig2000, cX600_X16DO=cX600_X16DO,
                         s5700_52C_SI=s5700_52C_SI, r8750=r8750, s3328TP_EI_24S=s3328TP_EI_24S,
                         hwPae8021xExt=hwPae8021xExt, hwTest=hwTest, ne5000EMulti=ne5000EMulti,
                         s5710_52C_PWR_EI=s5710_52C_PWR_EI, s2309P_SI=s2309P_SI, hwMplsLdp=hwMplsLdp,
                         wlanApWA1006=wlanApWA1006, ggsn9811=ggsn9811, wireInSmp=wireInSmp, hwHgmp=hwHgmp, hwDns=hwDns,
                         hwHSL=hwHSL, s9306E=s9306E, ar46_80=ar46_80, s3526c=s3526c, s5024G_24_20TP=s5024G_24_20TP,
                         ar46_40=ar46_40, s1700_52FR_2T2P_AC=s1700_52FR_2T2P_AC, hwLocal=hwLocal, s6506=s6506,
                         ar1220ws=ar1220ws, eudemon100E=eudemon100E, s2700_18TP_SI_AC=s2700_18TP_SI_AC, hwAti=hwAti,
                         attr=attr, s3552F_SI=s3552F_SI, hwVPRing=hwVPRing, s5348TP_PWR_SI=s5348TP_PWR_SI,
                         ne40E_X16=ne40E_X16, hwProducts=hwProducts, ne40E=ne40E, wlanBridgeWB2011=wlanBridgeWB2011,
                         s3700_52TP_EI_24S_AC=s3700_52TP_EI_24S_AC, s5710_28C_LI=s5710_28C_LI, s7700=s7700,
                         atmAccess=atmAccess, esr=esr, s3026E=s3026E, ma5605=ma5605,
                         s5700_52P_PWR_LI_AC=s5700_52P_PWR_LI_AC, s9306=s9306, sig9280=sig9280, e026=e026,
                         switch3016=switch3016, s5700_28C_HI=s5700_28C_HI, hwTrans=hwTrans,
                         s3700_52TP_EI_24S_DC=s3700_52TP_EI_24S_DC, s3700_52TP_EI_DC=s3700_52TP_EI_DC, lanSw=lanSw,
                         e050=e050, wireInSsp=wireInSsp, cX600_X16=cX600_X16, s3700_28TP_EI_24S_AC=s3700_28TP_EI_24S_AC,
                         cX200D=cX200D, ne16=ne16, ne05=ne05, wlanApWA1005=wlanApWA1005,
                         hwMusaV100R002Mib=hwMusaV100R002Mib, ar1240=ar1240, iad=iad, hwNovellProtocol=hwNovellProtocol,
                         nse1000_X3=nse1000_X3, ne40E_4=ne40E_4, s2326TP_PWR_EI=s2326TP_PWR_EI,
                         wlanApWA1008=wlanApWA1008, module=module, hwPower=hwPower, s5710_28C_PWR_EI=s5710_28C_PWR_EI,
                         s5310_28P_LI_DC=s5310_28P_LI_DC, hwSyslog=hwSyslog, hwCes=hwCes,
                         s2700_9TP_SI_AC=s2700_9TP_SI_AC, ne20E_X6=ne20E_X6, ssp3000=ssp3000, ssp1000=ssp1000,
                         cdmaInSmp=cdmaInSmp, ne40E_X3=ne40E_X3, mobileInScp=mobileInScp, s3026c_24_12fm=s3026c_24_12fm,
                         s3700_52TP_PWR_EI=s3700_52TP_PWR_EI, s2352P_SI=s2352P_SI, ne40E_X8=ne40E_X8,
                         hwDhcpProxy=hwDhcpProxy, s5700_48TP_SI_AC=s5700_48TP_SI_AC,
                         ce6850_52Q_EI_48S=ce6850_52Q_EI_48S, s2326TP_EI=s2326TP_EI, hwAaa=hwAaa,
                         s1700_28GFR_4P_AC=s1700_28GFR_4P_AC, ce6850_52Q_EI_48T=ce6850_52Q_EI_48T, s3026G_SI=s3026G_SI,
                         hsr=hsr, cX380_PBT=cX380_PBT, radium8750=radium8750, s7712=s7712,
                         hwVlanProtocol=hwVlanProtocol, ne20_2=ne20_2, s8016=s8016, hwGarpExt=hwGarpExt, iNet=iNet,
                         hwNTest=hwNTest, me60_16=me60_16, s3552P=s3552P, s3700_52TP_SI_AC=s3700_52TP_SI_AC, musa=musa,
                         ne80=ne80, s2309TP_SI=s2309TP_SI, s5328C_SI=s5328C_SI, switch2403=switch2403,
                         cX600_X2_M16=cX600_X2_M16, esr8825=esr8825, s3026t=s3026t, ar2240=ar2240,
                         s5012T_12_10GBC=s5012T_12_10GBC, eudemon200s=eudemon200s, cX500A=cX500A,
                         huaweiExperimental=huaweiExperimental, s2710_52P_PWR_SI=s2710_52P_PWR_SI,
                         cX600_X2DO=cX600_X2DO, switch3025_M=switch3025_M, cX600_X8=cX600_X8, s7706=s7706, cX380=cX380,
                         atm=atm, umg8900=umg8900, hwAtmCmRm=hwAtmCmRm, hwDHCPServerMib=hwDHCPServerMib, hwCdi=hwCdi,
                         switch2024_M=switch2024_M, s5700S_28P_LI_AC=s5700S_28P_LI_AC, s3352P_SI_48S=s3352P_SI_48S,
                         s5700_28P_LI=s5700_28P_LI, hwConfig=hwConfig, vdg10_41=vdg10_41, cX200D_EA=cX200D_EA,
                         s5700_52C_PWR_SI=s5700_52C_PWR_SI, s3050C=s3050C, hwLam=hwLam,
                         s5700S_52P_LI_AC=s5700S_52P_LI_AC, ne5000oem=ne5000oem, xdsl=xdsl, s3026F=s3026F,
                         s5310_52P_LI=s5310_52P_LI, s8016B=s8016B, s5710_52C_PWR_LI=s5710_52C_PWR_LI, s12716=s12716,
                         ar46_20=ar46_20, pysmi_as=pysmi_as)
mibBuilder.exportSymbols("HUAWEI-MIB", configFile=configFile, hwAtmSvc=hwAtmSvc, s5352C_EI=s5352C_EI,
                         ssp1000_4=ssp1000_4, hwPortal=hwPortal, hwLicense=hwLicense,
                         s5700_52X_PWR_LI_AC=s5700_52X_PWR_LI_AC, dlswLlc2=dlswLlc2, esrV5R3=esrV5R3,
                         s5306TP_SI=s5306TP_SI, mmsc=mmsc, hwClk=hwClk, me60_X3=me60_X3,
                         s5710_108C_PWR_HI=s5710_108C_PWR_HI, hwinfoX=hwinfoX, ptn6900_3=ptn6900_3,
                         s5700_26X_SI_12S_AC=s5700_26X_SI_12S_AC, s2700_26TP_PWR_EI=s2700_26TP_PWR_EI,
                         hwRouteManagementUrm=hwRouteManagementUrm, s5324TP_SI=s5324TP_SI,
                         s5700_28C_PWR_EI=s5700_28C_PWR_EI, cX600_X8DO=cX600_X8DO, atn980=atn980, hwNtp=hwNtp,
                         s5700_28X_LI_DC=s5700_28X_LI_DC, s5700_10P_PWR_LI_AC=s5700_10P_PWR_LI_AC, s3528P=s3528P,
                         ar207=ar207, s9303E=s9303E, hwIppool=hwIppool, hwImps=hwImps, ne20=ne20,
                         ne40E_X1_M4=ne40E_X1_M4, s3352P_PWR_EI=s3352P_PWR_EI, s3700_52TP_EI_AC=s3700_52TP_EI_AC, sm=sm,
                         s5352C_SI=s5352C_SI, s2700_26TP_SI_AC=s2700_26TP_SI_AC, wlanApWA1208=wlanApWA1208,
                         cdmaInSsp=cdmaInSsp, flash=flash, hwRouteManagement=hwRouteManagement, sig1000=sig1000,
                         s5328C_HI_24SA=s5328C_HI_24SA, s5700_28C_PWR_SI=s5700_28C_PWR_SI, ne40E_X2_M16=ne40E_X2_M16,
                         wcdma=wcdma, e6000=e6000, s1728_GWR_4P=s1728_GWR_4P, hwUcl=hwUcl, ar18_30=ar18_30,
                         hwMA5200Mib=hwMA5200Mib, s3552F_EI=s3552F_EI, hwRouteManagementRpm=hwRouteManagementRpm,
                         s3328TP_PWR_EI=s3328TP_PWR_EI, s5700_24TP_PWR_SI=s5700_24TP_PWR_SI, ne16E=ne16E, s12708=s12708,
                         ua5000ApmB=ua5000ApmB, s2352P_EI=s2352P_EI, esrV5R58825=esrV5R58825, e026_SI=e026_SI,
                         hwEnvironment=hwEnvironment, ar1220=ar1220, vRGW=vRGW, ne5000SysOid=ne5000SysOid,
                         cX600_4=cX600_4, s5700_24TP_SI_DC=s5700_24TP_SI_DC, svn3000=svn3000, hwMplsOam=hwMplsOam,
                         s2026C=s2026C, sgsn=sgsn, s3700_28TP_SI_AC=s3700_28TP_SI_AC, s5700_52P_LI=s5700_52P_LI,
                         s3700_28TP_PWR_SI=s3700_28TP_PWR_SI, honet=honet, eudemon200S=eudemon200S, ar18_18=ar18_18,
                         ar1240w=ar1240w, router=router, s2326P_SI=s2326P_SI, hwVrp=hwVrp, s5516=s5516, s2016=s2016,
                         esrV5R58850=esrV5R58850, dcswitch=dcswitch, hwVfb=hwVfb, cdmaIn=cdmaIn,
                         hwDslamPvcProtocol=hwDslamPvcProtocol, hwTestCommon=hwTestCommon, s5352C_PWR_SI=s5352C_PWR_SI,
                         ar18_31=ar18_31, hwIgspSnooping=hwIgspSnooping, hwMam=hwMam, ptn6900=ptn6900,
                         viewpoint=viewpoint, s5310_28P_LI=s5310_28P_LI, hwLoadBackup=hwLoadBackup, ptn2900=ptn2900,
                         hwAcl=hwAcl, hwAtmPos=hwAtmPos, s3326C_HI=s3326C_HI, s12700=s12700,
                         s5700_48TP_PWR_SI=s5700_48TP_PWR_SI, s9712=s9712, s5700_52X_LI_AC=s5700_52X_LI_AC, ne40=ne40,
                         usg5000=usg5000, s5700_52P_LI_DC=s5700_52P_LI_DC, cX600_X1_M4=cX600_X1_M4, ar1220vw=ar1220vw,
                         hwServerMon=hwServerMon, hwSps=hwSps, ne20E=ne20E, s3328TP_SI_24S=s3328TP_SI_24S,
                         hwPITP=hwPITP, s3328TP_SI=s3328TP_SI, s5700_52C_PWR_EI=s5700_52C_PWR_EI,
                         dlswInterface=dlswInterface, PYSNMP_MODULE_ID=huawei, s5700_28C_HI_24S=s5700_28C_HI_24S,
                         hwMa5300Mib=hwMa5300Mib, s9703=s9703, s6700_48_EI=s6700_48_EI, s6700_24_EI=s6700_24_EI,
                         hwMpls=hwMpls, s2309TP_EI=s2309TP_EI, s2700_18TP_EI_AC=s2700_18TP_EI_AC,
                         wlanApWA1003=wlanApWA1003, hwVdsl=hwVdsl, ptn6900_2=ptn6900_2, as8010=as8010,
                         s5710_28C_PWR_LI=s5710_28C_PWR_LI, s8505e=s8505e, hwRstpExt=hwRstpExt,
                         s5352C_PWR_EI=s5352C_PWR_EI, hwFr=hwFr, s2318P_EI=s2318P_EI, eudemon1000=eudemon1000,
                         vdg10_40=vdg10_40, ssp2000=ssp2000, mpeg_2=mpeg_2, s2710_52P_SI_AC=s2710_52P_SI_AC,
                         huaweiMgmt=huaweiMgmt, s3552G=s3552G, s3328TP_EI_MC=s3328TP_EI_MC, s3318TP_EI_MC=s3318TP_EI_MC,
                         hwVprn=hwVprn, hwMusaV100R001Mib=hwMusaV100R001Mib, s5328C_PWR_EI=s5328C_PWR_EI,
                         cX600_X2=cX600_X2, atn910=atn910, hwMa5100Mib=hwMa5100Mib, s9312E=s9312E, ce12804=ce12804,
                         ar207v=ar207v, hwPw=hwPw, eudemon2100=eudemon2100, msp=msp, cX380_ME=cX380_ME, ups=ups,
                         cX200D_EA_MC=cX200D_EA_MC, mlsr=mlsr, ma5100V600=ma5100V600, ssp5000_X3=ssp5000_X3,
                         s5710_52C_LI=s5710_52C_LI, s7703=s7703, rmonExtend=rmonExtend,
                         s2700_9TP_PWR_EI=s2700_9TP_PWR_EI, s5012T_12_10GBC_DC=s5012T_12_10GBC_DC, ptn6900_1=ptn6900_1,
                         optix155622H=optix155622H, me60=me60, ar208=ar208, apon=apon, ptn6900_16=ptn6900_16,
                         performance=performance, ssp5000_X16=ssp5000_X16, iad132=iad132, ne20_4=ne20_4,
                         hwMplsLsr=hwMplsLsr, secpath1800F=secpath1800F, eudemonEVPN5900=eudemonEVPN5900, atn=atn,
                         access_server=access_server, rm9000=rm9000, dlswCircuit=dlswCircuit, ua5000ipm=ua5000ipm,
                         me60_X16=me60_X16, s5700_10P_LI_AC=s5700_10P_LI_AC, s3528G=s3528G, hwMus=hwMus,
                         s5300_28C_PWR_EI=s5300_28C_PWR_EI, ce12808=ce12808, lswCommon=lswCommon, switch3008=switch3008,
                         s5310_52P_LI_DC=s5310_52P_LI_DC, hwDslamPPPoA=hwDslamPPPoA, mobileInSdp=mobileInSdp,
                         ce12812=ce12812, s3526F=s3526F, ar206=ar206, cdmaInScp=cdmaInScp, hwMplsVpls=hwMplsVpls,
                         cc08=cc08, acu=acu, p3=p3, s6348C=s6348C, s5700_28C_EI=s5700_28C_EI, eudemon200E=eudemon200E,
                         s5328C_EI_24S=s5328C_EI_24S, hwBRASMib=hwBRASMib, ne5000E=ne5000E, ma5101=ma5101,
                         s5700_52C_EI=s5700_52C_EI, s3526E=s3526E, ne5000E_BTB=ne5000E_BTB, s5348TP_SI=s5348TP_SI,
                         s2403H=s2403H, ne40E_X1=ne40E_X1, mobileIn=mobileIn, hwMplsVpn=hwMplsVpn, hwDeha=hwDeha,
                         s6503=s6503, dlswNode=dlswNode, wlanApWA1208H=wlanApWA1208H, wireInIP=wireInIP,
                         ar1220v=ar1220v, hwBtest=hwBtest, hwVTP=hwVTP, s2026=s2026, s3700_52P_PWR_SI=s3700_52P_PWR_SI,
                         ne40E_X2_M8=ne40E_X2_M8, hwAdsl=hwAdsl, ar=ar, s1700_52GFR_4P_AC=s1700_52GFR_4P_AC,
                         hwSwitchOver=hwSwitchOver, s8512=s8512, atn950=atn950, wlanApCommon=wlanApCommon,
                         s3526c_24_12fm=s3526c_24_12fm, dslw=dslw, ne08=ne08, hwIma=hwIma, optix10Gv2=optix10Gv2,
                         hwMd5500Mib=hwMd5500Mib, hwMs=hwMs, hwNat=hwNat, ar1220w=ar1220w, hwSPC=hwSPC,
                         hwDslamIpoa=hwDslamIpoa, hwV5=hwV5, mobileInSsp=mobileInSsp, ptn6900_8=ptn6900_8)
mibBuilder.exportSymbols("HUAWEI-MIB", hwBITS=hwBITS, s2710_26TP_PWR_SI=s2710_26TP_PWR_SI, s2008=s2008, amg5000=amg5000,
                         s9312=s9312, eudemon2200=eudemon2200, cX200A=cX200A, s5328C_HI=s5328C_HI,
                         lan_switch=lan_switch, isn8850=isn8850, hwDslamMacPool=hwDslamMacPool, quidway=quidway,
                         ne5000=ne5000, hwOSTA=hwOSTA, switch2403F=switch2403F, me60_4=me60_4,
                         s5700_28C_SI=s5700_28C_SI, s3026S_SI=s3026S_SI, netEngine=netEngine, ar1220s=ar1220s,
                         dlswSdlc=dlswSdlc, nse1000_4=nse1000_4, s3700_28TP_EI_MC_AC=s3700_28TP_EI_MC_AC,
                         ssp5000_X8=ssp5000_X8, hwDHCPRelayMib=hwDHCPRelayMib, s3026C_SI=s3026C_SI,
                         s5328C_HI_24S=s5328C_HI_24S, eudemon500=eudemon500, wlanAp=wlanAp, s3026V=s3026V,
                         s3026c=s3026c, s8505=s8505, s5328C_PWR_SI=s5328C_PWR_SI, s2318P_SI=s2318P_SI,
                         hwRouteManagementMrm=hwRouteManagementMrm, me60_X8=me60_X8, huaweiUtility=huaweiUtility,
                         s3700_28TP_EI_AC=s3700_28TP_EI_AC, s9303=s9303, s5024G_24_20TP_DC=s5024G_24_20TP_DC,
                         hwDhcp=hwDhcp, atn990=atn990, s5700_28P_LI_DC=s5700_28P_LI_DC, cX600_16=cX600_16,
                         s5324TP_PWR_SI=s5324TP_PWR_SI, cdmaInSdp=cdmaInSdp, routerGeneral=routerGeneral,
                         s3700_28TP_PWR_EI=s3700_28TP_PWR_EI, wlanBridgeWB2010=wlanBridgeWB2010,
                         s2700_26TP_EI_DC=s2700_26TP_EI_DC, cX600_X1=cX600_X1, atmBone=atmBone, s5328C_EI=s5328C_EI,
                         sbs=sbs, wlanApWA1003A=wlanApWA1003A, hwNetTest=hwNetTest, s5700_52X_LI_DC=s5700_52X_LI_DC,
                         hwSyntrap=hwSyntrap, hwEthernetPort=hwEthernetPort, ac6605_lsw=ac6605_lsw, hwMTA=hwMTA,
                         s3026c_24_12fs=s3026c_24_12fs, s1700_28FR_2T2P_AC=s1700_28FR_2T2P_AC, wlan=wlan,
                         cX600_X2_M8=cX600_X2_M8, hwVoip=hwVoip, s5700_24TP_SI_AC=s5700_24TP_SI_AC, s6324C=s6324C,
                         ma5102=ma5102, hwVlan=hwVlan, ar18_33=ar18_33, ias=ias, hwDatacomm=hwDatacomm, adsl=adsl,
                         gprs=gprs, ne40E_X2=ne40E_X2, wireIn=wireIn, s3700_28TP_SI_DC=s3700_28TP_SI_DC,
                         ip_phone=ip_phone, s5012G=s5012G, s3700_52TP_EI_48S_AC=s3700_52TP_EI_48S_AC,
                         s3328TP_EI=s3328TP_EI, ua5000IpmB=ua5000IpmB, hwMem=hwMem, s6506R=s6506R, hwPv8=hwPv8)
