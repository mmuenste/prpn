from pysnmp.hlapi import nextCmd, SnmpEngine, CommunityData
from pysnmp.hlapi import UdpTransportTarget, ContextData, ObjectType
from pysnmp.hlapi import  ObjectIdentity


oid = ObjectIdentity('SNMPv2-MIB', 'sysUpTime')

target_addr = ("192.168.181.21", 161)

snmp_engine_obj = SnmpEngine()
com_data_obj = CommunityData("public")
udp_transport_target_obj = UdpTransportTarget(target_addr)
context_data_obj = ContextData()
otype_oid = ObjectType(oid)

gen = nextCmd(snmp_engine_obj, com_data_obj,
              udp_transport_target_obj,
              context_data_obj, otype_oid)

*errorInformation, varBinds = next(gen)

# errorIndication, errorStatus, errorIndex = errorInformation
#print(errorInformation)  # [None, 0, 0]

for rfc1902obj in varBinds:
    print(rfc1902obj.prettyPrint())

# Ein weiterer Aufruf
*errorInformation, varBinds = next(gen)

for rfc1902obj in varBinds:
    print(rfc1902obj.prettyPrint())


