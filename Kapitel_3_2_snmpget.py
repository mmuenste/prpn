from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData
from pysnmp.hlapi import UdpTransportTarget, ContextData, ObjectType
from pysnmp.hlapi import  ObjectIdentity


oid = ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)

target_addr = ("192.168.181.21", 161)

snmp_engine_obj = SnmpEngine()
com_data_obj = CommunityData("public")
udp_transport_target_obj = UdpTransportTarget(target_addr)
context_data_obj = ContextData()
otype_oid = ObjectType(oid)

gen = getCmd(snmp_engine_obj, com_data_obj,
              udp_transport_target_obj,
              context_data_obj, otype_oid)

*errorInformation, varBinds = next(gen)

# errorIndication, errorStatus, errorIndex = errorInformation
#print(errorInformation)  # [None, 0, 0]

for rfc1902obj in varBinds:
    print(rfc1902obj.prettyPrint())



