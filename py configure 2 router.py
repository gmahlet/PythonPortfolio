Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from pysnmp.hlapi import*
community_Ro = 'public'
community_Rw = 'cisco@123'
router1_ip = '10.1.1.1'
router2_ip = '10.1.1.2'
host_ip = '172.18.42.10'
def configure_snmp(router_ip):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(snmpEngine(),
               CommunityData(community_Rw),
               UdpTransportTarget((router_ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0),'Router'),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0),'Location'),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0),'Contact'),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0),'Router Description'),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysUpTime',0),'1'),
               ObjectType(ObjectIdentity('SNMPv2-MIB','sysServices',0),'72')
         )
        )
    if errorIndication:
        print(f"Error configuring SNMP on {router_ip}:{errorIndication}")
def retrieve_snmp_data(router_ip):
    
SyntaxError: invalid syntax
def retrieve_snmp_data(router_ip):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community_Ro),
        UdpTransportTarget((router_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0)),
        ObjectType(ObjectIdentity('IF-MIB','ifDescr')),
        ObjectType(ObjectIdentity('IF-MIB','ifInOctets')),
        ObjectType(ObjectIdentity('IF-MIB','ifDOutOctets')),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysUpTime',0)),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0)),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0)),
        LexicographicMode=False
     ):
        if errorIndication:
            print(f"Error retrieving SNMP data from {router_ip}: {errorIndication}")
            break
        elif errorStatus:
            print(f"SNMP error from {router_ip}: {errorStatus}")
            break
        else:
            for varBind in varBinds:
                print(varBind.prettyPrint())

                
configure_snmp(router1_ip)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    configure_snmp(router1_ip)
NameError: name 'configure_snmp' is not defined
configure_snmp(router_ip)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    configure_snmp(router_ip)
NameError: name 'configure_snmp' is not defined
   configure_snmp(router1_ip)
   
SyntaxError: unexpected indent
    def retrieve_snmp_data(router_ip):
        for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
            SnmpEngine(),
            CommunityData(community_Ro),
            UdpTransportTarget((router_ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0)),
            ObjectType(ObjectIdentity('IF-MIB','ifDescr')),
            ObjectType(ObjectIdentity('IF-MIB','ifInOctets')),
            ObjectType(ObjectIdentity('IF-MIB','ifDOutOctets')),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysUpTime',0)),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0)),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0)),
            LexicographicMode=False
         ):
            if errorIndication:
                print(f"Error retrieving SNMP data from {router_ip}: {errorIndication}")
                break
            elif errorStatus:
                print(f"SNMP error from {router_ip}: {errorStatus}")
                break
            else:
                for varBind in varBinds:
                    print(varBind.prettyPrint())
                    
SyntaxError: unexpected indent
def retrieve_snmp_data(router_ip):
    for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community_Ro),
        UdpTransportTarget((router_ip, 161)),
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0)),
        ObjectType(ObjectIdentity('IF-MIB','ifDescr')),
        ObjectType(ObjectIdentity('IF-MIB','ifInOctets')),
        ObjectType(ObjectIdentity('IF-MIB','ifDOutOctets')),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysUpTime',0)),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0)),
        ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0)),
        LexicographicMode=False
     ):
        if errorIndication:
            print(f"Error retrieving SNMP data from {router_ip}: {errorIndication}")
            break
        elif errorStatus:
            print(f"SNMP error from {router_ip}: {errorStatus}")
            break
        else:
...             for varBind in varBinds:
...                 print(varBind.prettyPrint())
...     configure_snmp(router1_ip)
...     configure_snmp(router2_ip)
...     print("SNMP data from Router 1:")
... 
...     
>>> print("SNMP data from Router 1:")
SNMP data from Router 1:
>>> def retrieve_snmp_data(router_ip):
...     for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
...         SnmpEngine(),
...         CommunityData(community_Ro),
...         UdpTransportTarget((router_ip, 161)),
...         ContextData(),
...         ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0)),
...         ObjectType(ObjectIdentity('IF-MIB','ifDescr')),
...         ObjectType(ObjectIdentity('IF-MIB','ifInOctets')),
...         ObjectType(ObjectIdentity('IF-MIB','ifDOutOctets')),
...         ObjectType(ObjectIdentity('SNMPv2-MIB','sysUpTime',0)),
...         ObjectType(ObjectIdentity('SNMPv2-MIB','sysContact',0)),
...         ObjectType(ObjectIdentity('SNMPv2-MIB','sysLocation',0)),
...         LexicographicMode=False
...      ):
...         if errorIndication:
...             print(f"Error retrieving SNMP data from {router_ip}: {errorIndication}")
...             break
...         elif errorStatus:
...             print(f"SNMP error from {router_ip}: {errorStatus}")
...             break
...         else:
...             for varBind in varBinds:
...                 print(varBind.prettyPrint())
...     configure_snmp(router1_ip)
...     configure_snmp(router2_ip)
...     print("SNMP data from Router 1:")
...     retrieve_snmp_data(route1_ip)
...     print("SNMP data from Router2:")
...     retrieve_snmp_data(route2_ip)
