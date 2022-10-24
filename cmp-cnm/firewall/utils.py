import logging
from ncclient import operations
from route.utils import NetConf

logger = logging.getLogger(__package__)


class FirewallNetConfMixin(NetConf):
    OPERATION_CREATE = 'create'
    OPERATION_DELETE = 'delete'
    OPERATION_REPLACE = 'replace'
    xmlns = "http://www.h3c.com/netconf/data:1.0"
    xmlns_xc = "urn:ietf:params:xml:ns:netconf:base:1.0"
    xmlns_config = "http://www.h3c.com/netconf/config:1.0"
    target_running = 'running'
    max_rule_id = 50000
    timeout = 30
    device_name = 'h3c'
    is_allowed = True
    any_network = 'Any'

    def edit_config(self, conn, xml):
        try:
            ret = conn.edit_config(target=self.target_running, config=xml)
        except operations.rpc.RPCError as exc:
            logger.error(f"netconf edit config:{xml}, result: {exc}")
            return False, str(exc)
        else:
            logger.info(f"netconf edit config:{xml}, result: ok")
            return ret.ok, ret.errors

    def preset_security_policy_id(self, conn):
        xml = f'''<top xmlns="{ self.xmlns }">
            <SecurityPolicies>
                <GetRules>
                    <Rule>
                        <ID></ID>
                    </Rule>
                </GetRules>
            </SecurityPolicies>
        </top>'''
        ret = conn.get(filter=('subtree', xml))
        id_eles = ret.data.xpath('//n:GetRules/n:Rule/n:ID', namespaces={'n': self.xmlns})
        if id_eles:
            self.id = int(id_eles[-1].text) + 1
            if self.id >= self.max_rule_id:
                raise Exception(f'security policy ipv4 rule id:{ self.id } is out of range')
            return self.id
        else:
            raise Exception('no security policy ipv4 rules, please check device')

    def create_security_policy_rule(self, conn, rule_id, name, zone_source_network, zone_destination_network):
        xml = f'''<config xmlns:xc="{ self.xmlns_xc }">
            <top xmlns="{ self.xmlns_config }" xc:operation="{ self.OPERATION_CREATE }">
                <SecurityPolicies>
                    <IPv4Rules>
                        <Rule>
                            <ID>{ rule_id }</ID>
                            <RuleName>{ name }</RuleName>
                            <Action>{ 2 }</Action>
                        </Rule>
                    </IPv4Rules>
                    <IPv4SrcSecZone>
                        <SrcSecZone>
                            <ID>{ rule_id }</ID>
                            <SeqNum>1</SeqNum>
                            <IsIncrement>true</IsIncrement>
                            <NameList>
                                <NameItem>{ zone_source_network }</NameItem>
                            </NameList>
                        </SrcSecZone>
                    </IPv4SrcSecZone>
                    <IPv4DestSecZone>
                        <DestSecZone>
                            <ID>{ rule_id }</ID>
                            <SeqNum>1</SeqNum>
                            <IsIncrement>true</IsIncrement>
                            <NameList>
                                <NameItem>{ zone_destination_network }</NameItem>
                            </NameList>
                        </DestSecZone>
                    </IPv4DestSecZone>
                </SecurityPolicies>
            </top>
        </config>'''
        return conn.edit_config(target =self.target_running ,config=xml)

    def delete_security_policy_rule(self, conn, rule_id):
        xml = f'''<config xmlns:xc="{ self.xmlns_xc }">
                <top xmlns="{ self.xmlns_config }">
                    <SecurityPolicies>
                        <IPv4Rules>
                            <Rule xc:operation="{ self.OPERATION_DELETE }">
                                <ID>{ rule_id }</ID>
                            </Rule>
                        </IPv4Rules>
                    </SecurityPolicies>
                </top>
            </config>'''
        return conn.edit_config(target=self.target_running, config=xml)

    def update_security_policy_rule(self, conn, rule_id, is_allow):
        xml = f'''<config xmlns:xc="{self.xmlns_xc}">
                <top xmlns="{ self.xmlns_config }" xc:operation="{ self.OPERATION_REPLACE }">
                    <SecurityPolicies>
                        <IPv4Rules>
                            <Rule>
                                <ID>{ rule_id }</ID>
                                <Action>{ int(is_allow) }</Action>
                            </Rule>
                        </IPv4Rules>
                    </SecurityPolicies>
                </top>
            </config>'''
        return conn.edit_config(target=self.target_running, config=xml)

    def get_interface_securityzone(self, conn, zone_source_network_ipv4, zone_destination_network_ipv4):
        xml_securityzone = f'''
                  <top xmlns="{ self.xmlns }">            
                      <SecurityZone>
                      <Interfaces>
                      </Interfaces>
                      </SecurityZone>                 
                  </top>  
        '''
        res_securityzone_subtree = conn.get(filter=('subtree', xml_securityzone))
        res_securityzone_xpath = res_securityzone_subtree.data.xpath('//n:SecurityZone/n:Interfaces', namespaces={'n': self.xmlns})
        interfaces_list = []
        for res_securityzone in res_securityzone_xpath[0]:
            res_securityzone_dict = {}
            for securityzone in res_securityzone:
                res_securityzone_dict[securityzone.tag.split("}")[-1]] = securityzone.text
            interfaces_list.append(res_securityzone_dict)
        xml_ifmgr = f'''
                  <top xmlns="{ self.xmlns }">
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
        res_ifmgr_subtree = conn.get(filter=('subtree', xml_ifmgr))
        res_ifmgr_xpath = res_ifmgr_subtree.data.xpath('//n:Ifmgr/n:Interfaces/n:Interface', namespaces={'n': self.xmlns})
        interface_list = []
        for res_ifmgr in res_ifmgr_xpath:
            res_ifmgr_dict = {}
            for ifmgr in res_ifmgr:
                res_ifmgr_dict[ifmgr.tag.split("}")[-1]] = ifmgr.text
            if 'InetAddressIPV4' in res_ifmgr_dict.keys():
                interface_list.append(res_ifmgr_dict)
        zone_source_network_str = ''
        for sou_interface in interface_list:
            if zone_source_network_ipv4 == sou_interface['InetAddressIPV4']:
                for sou_interfaces in interfaces_list:
                    if sou_interface['IfIndex'] == sou_interfaces['IfIndex']:
                        zone_source_network_str = sou_interfaces['ZoneName']
        zone_destination_network_str = ''
        for des_interface in interface_list:
            if zone_destination_network_ipv4 == des_interface['InetAddressIPV4']:
                for des_interfaces in interfaces_list:
                    if des_interface['IfIndex'] == des_interfaces['IfIndex']:
                        zone_destination_network_str = des_interfaces['ZoneName']
        return {'zone_source_network':zone_source_network_str, 'zone_destination_network':zone_destination_network_str}

    def get_interface_network(self, conn):
        xml_ifmgr = f'''
                  <top xmlns="{ self.xmlns }">
                      <Ifmgr>
                      <Interfaces>
                          <Interface>
                              <InetAddressIPV4>
                              </InetAddressIPV4>
                          </Interface>
                      </Interfaces>    
                    </Ifmgr>    
                  </top>  
            '''
        res_ifmgr_subtree = conn.get(filter=('subtree', xml_ifmgr))
        res_ifmgr_xpath = res_ifmgr_subtree.data.xpath('//n:Ifmgr/n:Interfaces/n:Interface', namespaces={'n': self.xmlns})
        interface_list = []
        for res_ifmgr in res_ifmgr_xpath:
            res_ifmgr_dict = {}
            for ifmgr in res_ifmgr:
                res_ifmgr_dict[ifmgr.tag.split("}")[-1]] = ifmgr.text
            if 'InetAddressIPV4' in res_ifmgr_dict.keys():
                interface_list.append(res_ifmgr_dict)
        return interface_list