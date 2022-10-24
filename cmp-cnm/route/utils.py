from ncclient import manager, operations
from cmp_cnm.settings import H3C_HOST
from cmp_cnm.settings import H3C_PORT
from cmp_cnm.settings import H3C_USER
from cmp_cnm.settings import H3C_PASSWORD

import logging

logger = logging.getLogger(__package__)

class NetConf:
    OPERATION_CREATE = 'create'
    OPERATION_DELETE = 'delete'
    xmlns = "http://www.h3c.com/netconf/data:1.0"
    xmlns_xc = "urn:ietf:params:xml:ns:netconf:base:1.0"
    target_running = 'running'
    max_rule_id = 50000
    timeout = 30
    device_name = 'h3c'
    any_network = 'Any'

    @classmethod
    def get_netconf_conn(cls):
        return manager.connect(
        host=H3C_HOST,
        port=H3C_PORT,
        username=H3C_USER,
        password=H3C_PASSWORD,
        hostkey_verify=False,
        look_for_keys=False,
        manager_params={'timeout': cls.timeout},
        device_params={'name': cls.device_name})

    def edit_config(self, conn, xml):
        try:
            ret = conn.edit_config(target=self.target_running, config=xml)
        except operations.rpc.RPCError as exc:
            logger.error(f"netconf edit config:{xml}, result: {exc}")
            return False, str(exc)
        else:
            logger.info(f"netconf edit config:{xml}, result: ok")
            return ret.ok, ret.errors


class StaticRoutingNetConfMixin(NetConf):
    dest_vrf_index = 0
    dest_topology_index = 0
    next_hop_vrf_index = 0
    if_index = 0

    def create_static_routing(self, conn, destination_subnet,ip_next_hop_address,cluster_code):
        xml = f'''<config xmlns:xc="{ self.xmlns_xc }">
             <StaticRoute xmlns="{ self.xmlns }">
                 <Ipv4StaticRouteConfigurations xc:operation="{ self.OPERATION_CREATE }">
                     <RouteEntry>
                         <DestVrfIndex>{ self.dest_vrf_index }</DestVrfIndex>
                         <DestTopologyIndex>{ self.dest_topology_index }</DestTopologyIndex>
                         <Ipv4Address>{ destination_subnet[0] }</Ipv4Address>
                         <Ipv4PrefixLength>{ cluster_code[0] }</Ipv4PrefixLength>
                         <NexthopVrfIndex>{ self.next_hop_vrf_index }</NexthopVrfIndex>
                         <NexthopIpv4Address>{ ip_next_hop_address[0] }</NexthopIpv4Address>
                         <IfIndex>{ self.if_index }</IfIndex>
                     </RouteEntry>
                 </Ipv4StaticRouteConfigurations>
             </StaticRoute>
         </config>'''
        return self.edit_config(conn, xml)

    def delete_static_routing(self, conn, destination_subnet, ip_next_hop_address, cluster_code):
        xml = f'''<config xmlns:xc="{ self.xmlns_xc }">
             <StaticRoute xmlns="{ self.xmlns }">
                 <Ipv4StaticRouteConfigurations xc:operation="{ self.OPERATION_DELETE }">
                     <RouteEntry>
                         <DestVrfIndex>{ self.dest_vrf_index }</DestVrfIndex>
                         <DestTopologyIndex>{ self.dest_topology_index }</DestTopologyIndex>
                         <Ipv4Address>{ destination_subnet }</Ipv4Address>
                         <Ipv4PrefixLength>{ cluster_code }</Ipv4PrefixLength>
                         <NexthopVrfIndex>{ self.next_hop_vrf_index }</NexthopVrfIndex>
                         <NexthopIpv4Address>{ ip_next_hop_address }</NexthopIpv4Address>
                         <IfIndex>{ self.if_index }</IfIndex>
                     </RouteEntry>
                 </Ipv4StaticRouteConfigurations>
             </StaticRoute>
         </config>'''
        return self.edit_config(conn, xml)