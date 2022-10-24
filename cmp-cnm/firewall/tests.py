from django.test import TestCase

# Create your tests here.
import pdb
from ncclient import manager, operations

OPERATION_CREATE = 'create'
OPERATION_DELETE = 'delete'
OPERATION_MERGE = 'merge'
xmlns = "http://www.h3c.com/netconf/data:1.0"
xmlns_xc = "urn:ietf:params:xml:ns:netconf:base:1.0"
target_running = 'running'
max_rule_id = 50000
timeout = 30
device_name = 'h3c'
is_allowed = True
any_network = 'Any'


def get_netconf_conn():
    return manager.connect(
        host='10.209.255.2',
        port=830,
        username='fzyh_mawei',
        password='fzyh_mawei_yh601933',
        hostkey_verify=False,
        look_for_keys=False,
        manager_params={'timeout': timeout},
        device_params={'name': device_name})


def create_rule():
    with get_netconf_conn() as conn:
        preset_security_policy_id(conn)
        create_security_policy_rule(conn)
        delete_security_policy_rule(conn)
        create_static_routing(conn)
        update_static_routing(conn)
        get_all_interfaces(conn)


def preset_security_policy_id(conn):
    xml = f'''<top xmlns="{xmlns}">
            <SecurityPolicies>
                <GetRules>
                    <Rule>
                        <ID></ID>
                    </Rule>
                </GetRules>
            </SecurityPolicies>
        </top>'''
    ret = conn.get(filter=('subtree', xml))
    print(ret)
    id_eles = ret.data.xpath('//n:GetRules/n:Rule/n:ID', namespaces={'n': xmlns})
    if id_eles:
        id = int(id_eles[-1].text) + 1
        print(id)
        return id
    #     if id >= max_rule_id:
    #         raise Exception(f'security policy ipv4 rule id:{ id } is out of range')
    #
    # else:
    #     raise Exception('no security policy ipv4 rules, please check device')


def create_security_policy_rule(conn):
    xml = f'''<config xmlns:xc="{xmlns_xc}">
            <top xmlns="http://www.h3c.com/netconf/config:1.0" xc:operation="replace">
                <SecurityPolicies>
                    <IPv4Rules>
                        <Rule>
                            <ID>252</ID>

                            <Action>{1}</Action>
                        </Rule>
                    </IPv4Rules>

                </SecurityPolicies
            </top>
        </config>'''
    return conn.edit_config(target=target_running, config=xml)


def delete_security_policy_rule(conn):
    xml = f'''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <top xmlns="http://www.h3c.com/netconf/config:1.0">
                <SecurityPolicies>
                    <IPv4Rules>
                        <Rule xc:operation="delete">
                            <ID>245</ID>
                        </Rule>
                    </IPv4Rules>
                </SecurityPolicies>
            </top>
        </config>'''
    return conn.edit_config(target=target_running, config=xml)


def create_static_routing(conn):
    dest_vrf_index = 0
    dest_topology_index = 0
    next_hop_vrf_index = 0
    if_index = 0
    xml = f'''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <StaticRoute xmlns="http://www.h3c.com/netconf/config:1.0">
            <Ipv4StaticRouteConfigurations xc:operation="replace">
                <RouteEntry>
                    <DestVrfIndex>0</DestVrfIndex>
                    <DestTopologyIndex>0</DestTopologyIndex>
                    <Ipv4Address>10.201.1.8</Ipv4Address>
                    <Ipv4PrefixLength>31</Ipv4PrefixLength>
                    <NexthopVrfIndex>0</NexthopVrfIndex>
                    <NexthopIpv4Address>1.1.1.9</NexthopIpv4Address>
                    <IfIndex>0</IfIndex>
                </RouteEntry>
            </Ipv4StaticRouteConfigurations>
        </StaticRoute>
    </config>'''
    return conn.edit_config(target=target_running, config=xml)


def update_static_routing(conn):
    xml = f'''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <StaticRoute xmlns="http://www.h3c.com/netconf/config:1.0">
                <Ipv4StaticRouteConfigurations xc:operation="create">
                    <RouteEntry>
                        <DestVrfIndex>0</DestVrfIndex>
                        <DestTopologyIndex>0</DestTopologyIndex>
                        <Ipv4Address>1.1.1.1</Ipv4Address>
                        <Ipv4PrefixLength>32</Ipv4PrefixLength>
                        <NexthopVrfIndex>0</NexthopVrfIndex>
                        <NexthopIpv4Address>1.1.1.2</NexthopIpv4Address>
                        <IfIndex>0</IfIndex>
                    </RouteEntry>
                </Ipv4StaticRouteConfigurations>
                <Ipv4StaticRouteConfigurations xc:operation="delete">
                    <RouteEntry>
                        <DestVrfIndex>0</DestVrfIndex>
                        <DestTopologyIndex>0</DestTopologyIndex>
                        <Ipv4Address>2.2.2.2</Ipv4Address>
                        <Ipv4PrefixLength>32</Ipv4PrefixLength>
                        <NexthopVrfIndex>0</NexthopVrfIndex>
                        <NexthopIpv4Address>3.3.3.3</NexthopIpv4Address>
                        <IfIndex>0</IfIndex>
                    </RouteEntry>
                </Ipv4StaticRouteConfigurations>
            </StaticRoute>
        </config>'''
    return conn.edit_config(target=target_running, config=xml)


def get_all_interfaces(conn):
    xml1 = f'''
              <top xmlns="http://www.h3c.com/netconf/data:1.0">            
                <SecurityZone>
                  <Interfaces>
                  </Interfaces>
                  </SecurityZone>                 
              </top>  
    '''
    ret1 = conn.get(filter=('subtree', xml1))
    id_eles1 = ret1.data.xpath('//n:SecurityZone/n:Interfaces', namespaces={'n': xmlns})
    li1 = []
    for i in id_eles1[0]:
        li2 = {}
        for j in i:
            li2[j.tag.split("}")[-1]] = j.text
        li1.append(li2)
    print(li1)

    xml2 = f'''
              <top xmlns="http://www.h3c.com/netconf/data:1.0">
                <Ifmgr>
                  <Interfaces>
                    <Interface>
                        <AbbreviatedName>
                        </AbbreviatedName>
                        <InetAddressIPV4>
                        </InetAddressIPV4>
                        <IfIndex>
                        </IfIndex>
                    </Interface>
                  </Interfaces>    
                </Ifmgr>    
              </top>  
    '''
    ret2 = conn.get(filter=('subtree', xml2))
    id_eles = ret2.data.xpath('//n:Ifmgr/n:Interfaces/n:Interface', namespaces={'n': xmlns})
    l3 = []
    for i in id_eles:
        l4 = {}
        for j in i:
            l4[j.tag.split("}")[-1]] = j.text
        if 'InetAddressIPV4' in l4.keys():
            l3.append(l4)
    print(l3)
    zzz = ""
    zone_source_network = '192.168.1.22'
    zone_destination_network = '10.209.239.1'
    for k in l3:
        if zone_source_network == k['InetAddressIPV4']:
            for v in li1:
                if k['IfIndex'] == v['IfIndex']:
                    zzz = v['ZoneName']
    xxx = ''
    for h in l3:
        if zone_destination_network == h['InetAddressIPV4']:
            for f in li1:
                if h['IfIndex'] == f['IfIndex']:
                    xxx = f['ZoneName']
    print(zzz)
    print(xxx)


create_rule()




