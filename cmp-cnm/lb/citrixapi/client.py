from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_cspolicy_binding import csvserver_cspolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csaction import csaction
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.server import server
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslkeyfile import sslkeyfile
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertfile import sslcertfile
from nssrc.com.citrix.netscaler.nitro.resource.config.network.vlan import vlan
from cmp_cnm.settings import URL
import os

"""
负载均衡创建：
创建负载均衡 create_lb
4层负载均衡创建方式：
   创建4层监听：create_lb_listener -> create_lb_true_policy -> create_lb_action(action和lbvs)
   添加member：add_lb_member(lbvs_name==action_name==policy_name) -> 检查是否存在member ->(否) create_lb_member
   -> 检查是否存在server -> (否) 创建service时添加server（server_name == ipaddress）
   lb_name = lb_name
   lb_listener_name = vip:port-protocol
7层负载均衡创建方式：
   创建7层监听：create_lb_listener
   创建域名：create_lb_host(policy) -> 
   添加member：add_lb_member(lbvs_name==action_name==policy_name) -> 检查是否存在member ->(否) create_lb_member
   -> 检查是否存在server -> (否) 创建service时添加server（server_name == ipaddress）
   lb_name = lb_name
   lb_listener_name = vip:port-protocol
   lb_host_name = lb_listener_name-host_name
   lb_path_name = lb_host_name-1,lb_host_name-2....lb_host_name-n
   lb_path_name = lb_action_name = lb_vs_name
   member_name = member_ip:port-protocol
"""


def create_lb(session, name, address):
    """
    新建Content Switching vs 作为负载均衡，默认先创建一个协议为any的Content Switching
    """
    try:
        csvs = csvserver()
        csvs.name = name
        csvs.servicetype = "ANY"
        csvs.ipv46 = address
        csvs.port = "*"
        csvserver.add(session, csvs)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb(session, name):
    try:
        csvs_list = csvserver()
        csvs_list.delete(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def get_lb(session, name):
    try:
        csvs = csvserver()
        return csvs.get(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_listener_v4(session, name, address, port, protocol, lbmethod):
    """
    新建4层带有端口和协议的Content Switching vs，作为负载均衡的监听器
    """
    try:
        lb_listener = csvserver()
        lb_listener.name = name
        lb_listener.servicetype = protocol
        lb_listener.ipv46 = address
        lb_listener.port = port
        csvserver.add(session, lb_listener)
        create_lb_true_policy(session, address, port, protocol, lbmethod)
        listener_policy = csvserver_cspolicy_binding()
        listener_policy.name = name
        listener_policy.policyname = name
        listener_policy.priority = 100
        csvserver_cspolicy_binding.add(session, listener_policy)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_listener_v4(session, name):
    try:
        lb_listener = csvserver()
        lb_listener.delete(session, name)
        delete_lb_ture_policy(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_listener_v7(session, name, address, port, protocol):
    """
    新建7层带有端口和协议的Content Switching vs，作为负载均衡的监听器
    """
    try:
        protocol_lb = protocol
        if protocol == "HTTPS":
            protocol_lb = "SSL"
        print(protocol_lb)
        lb_listener = csvserver()
        lb_listener.name = name
        lb_listener.servicetype = protocol_lb
        lb_listener.ipv46 = address
        lb_listener.port = port
        csvserver.add(session, lb_listener)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def add_ssl(session, ssl_name, listener_name):
    try:
        csvs = sslvserver_sslcertkey_binding()
        csvs.vservername = listener_name
        csvs.certkeyname = ssl_name
        sslvserver_sslcertkey_binding.add(session, csvs)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_listener_v7_check(session, name):
    try:
        lb_policy = csvserver_cspolicy_binding.get(session, name)
        return lb_policy
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_listener_v7(session, name):
    try:
        lb_listener = csvserver()
        lb_listener.delete(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_host(session, name, host, match_type, listener, protocol):
    """
    新建Content Switching policies ，作为域名策略
    match_type:
    HTTP.REQ.HOSTNAME.EQ("test.com")   Equal
    HTTP.REQ.HOSTNAME.
    """
    try:
        lb_host = cspolicy()
        lb_host.policyname = name
        lb_host.rule = "HTTP.REQ.HOSTNAME.{0}(\"{1}\")".format(match_type, host)
        create_lb_action(session, name, protocol, lbmethod="ROUNDROBIN")
        lb_host.action = name
        cspolicy.add(session, lb_host)
        csvs_host = csvserver_cspolicy_binding()
        csvs_host.name = listener
        csvs_host.policyname = name
        priority = 100000
        priority_list = []
        paths = csvserver_cspolicy_binding.get(session, listener)
        for path in paths:
            priority_list.append(path.priority)
        for i in range(100000, 10000000):
            if str(priority) in priority_list:
                priority = priority + 1
            else:
                break
        csvs_host.priority = priority
        csvserver_cspolicy_binding.add(session, csvs_host)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_host(session, lb_name, host_name):
    try:
        delete_csvs_policy(session, lb_name, host_name)
        lb_host = cspolicy()
        lb_host.delete(session, host_name)
        delete_lb_action(session, host_name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_path(session, listener, name, match_type, host_match_type, protocol, lbmethod, lb_host, path='/'):
    """
    新建Content Switching policies ，作为host+url策略
    match_type:
    HTTP.REQ.URL.EQ("test.com")   Equal
    HTTP.REQ.URL.
    """
    try:
        lb_path = cspolicy()
        for i in range(1, 1000):
            policy_name = name + "-" + str(i)
            try:
                lb_path.get(session, policy_name)
            except:
                name = policy_name
                break
        lb_path.policyname = name
        lb_path.action = path
        lb_path.rule = "HTTP.REQ.HOSTNAME.{0}(\"{1}\") && HTTP.REQ.URL.{2}(\"{3}\")".format(
            host_match_type, lb_host, match_type, path)
        create_lb_action(session, name, protocol, lbmethod)
        lb_path.action = name
        cspolicy.add(session, lb_path)
        priority = 100
        priority_list = []
        paths = csvserver_cspolicy_binding.get(session, listener)
        for path in paths:
            priority_list.append(path.priority)
        for i in range(1, 10000):
            if str(priority) in priority_list:
                priority = priority + 10
            else:
                break
        csvs_path = csvserver_cspolicy_binding()
        csvs_path.name = listener
        csvs_path.policyname = name
        csvs_path.priority = priority
        csvserver_cspolicy_binding.add(session, csvs_path)
        return name
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_path(session, csvs_name, path_name):
    try:
        delete_csvs_policy(session, csvs_name, path_name)
        lb_path = cspolicy()
        lb_path.delete(session, path_name)
        delete_lb_action(session, path_name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_true_policy(session, address, port, protocol, lbmethod):
    try:
        name = address + ":" + str(port) + "-" + protocol
        create_lb_action(session, name, protocol, lbmethod)
        lb_true_policy = cspolicy()
        lb_true_policy.policyname = name
        lb_true_policy.rule = "true"
        lb_true_policy.action = name
        cspolicy.add(session, lb_true_policy)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_ture_policy(session, name):
    try:
        cspolicy.delete(session, name)
        delete_lb_action(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_csvs_policy(session, csvs_name, policy_name):
    try:
        csvs = csvserver_cspolicy_binding()
        csvs.name = csvs_name
        csvs.policyname = policy_name
        csvserver_cspolicy_binding.delete(session, csvs)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_action(session, name, protocol, lbmethod):
    """
    创建Content Switching策略的action和lb_vs
    """
    try:
        lb_action = csaction()
        lb_action.name = name
        lb_name = name + "-lbvs"
        create_lb_vs(session, lb_name, protocol, lbmethod)
        lb_action.targetlbvserver = lb_name
        csaction.add(session, lb_action)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_action(session, name):
    try:
        lb_action = csaction()
        lb_action.delete(session, name)
        delete_lb_vs(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_vs(session, name, protocol, lbmethod):
    """
    新建负载均衡的lbvs，用于关联Content Switching策略的action，以及向lbvs中添加member
    lbmethod: 轮询 ROUNDROBIN ，最小连接数 LEASTCONNECTION
    """
    try:
        protocol_lb = protocol
        if protocol == "HTTPS":
            protocol_lb = "SSL"
        lb_vserver = lbvserver()
        lb_vserver.name = name
        lb_vserver.servicetype = protocol_lb
        lb_vserver.lbmethod = lbmethod
        lbvserver.add(session, lb_vserver)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_vs(session, name):
    try:
        lb_vserver = lbvserver()
        lb_name = name + "-lbvs"
        lb_vserver.delete(session, lb_name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def lb_vs_member_list(session, lb_vs_name):
    """
    获取lbvs下的lb_service的列表
    """
    try:
        service_list = lbvserver_service_binding.get(session, lb_vs_name)
        if service_list:
            return service_list
        else:
            print("EXception::getservice ERROR")
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def lb_member_list(session):
    """
    获取lb下的service的列表
    """
    try:
        lb_service = service()
        result = lb_service.get(session)
        lb_member = []
        for member_name in result:
            lb_member.append(member_name.name)
        return lb_member
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def add_lb_member(session, address, port, weight, protocol, vs_name):
    """
    向vs_name的lbvs中添加lb_services
    """
    try:
        name = address + ":" + str(port) + "-" + protocol
        if name not in lb_member_list(session):
            create_lb_member(session, address, port, protocol)
        lb_member = lbvserver_service_binding()
        lb_member.servicename = name
        lb_member.weight = weight
        lb_member.name = vs_name
        lbvserver_service_binding.add(session, lb_member)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_lb_member(session, name, member_name):
    try:
        lb_member = lbvserver_service_binding()
        lb_member.name = name
        lb_member.servicename = member_name
        lbvserver_service_binding.delete(session, lb_member)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def update_lb_member(session, name, member_name, ip, port, weight, protocol):
    try:
        lb_member = lbvserver_service_binding()
        lb_member.name = name
        lb_member.servicename = member_name
        lbvserver_service_binding.delete(session, lb_member)
        add_lb_member(session, ip, port, weight, protocol, name)
    except nitro_exception as exc:
        lbvserver_service_binding.add(session, lb_member)
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        lbvserver_service_binding.add(session, lb_member)
        print("Exception::message=" + str(exc.args))
        raise exc


def list_server(session):
    try:
        servers = server()
        result = servers.get(session)
        lb_servers = []
        for lb_server in result:
            lb_servers.append(lb_server.ipaddress)
        return lb_servers
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_lb_member(session, address, port, protocol):
    """
    新建lb_service
    """
    try:
        protocol_lb = protocol
        if protocol == "HTTPS":
            protocol_lb = "SSL"
        lb_member = service()
        lb_member.name = address + ":" + str(port) + "-" + protocol
        if address not in list_server(session):
            lb_member.ip = address
        else:
            lb_member.servername = address
        lb_member.port = port
        lb_member.servicetype = protocol_lb
        lb_member.add(session, lb_member)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def ssl_key_file(session, pkey, name):
    try:
        with open("/opt/media/{0}.key".format(name), 'w') as key_file:
            key_file.write(pkey)
        key_file.close()
        ssl = sslkeyfile()
        ssl.name = "{0}.key".format(name)
        ssl.src = "http://{0}/media/{1}.key".format(URL, name)
        sslkeyfile.Import(session, ssl)
        os.system("rm -f /opt/media/{0}.key".format(name))
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def ssl_cert_file(session, cert, name):
    try:
        with open("/opt/media/{0}.crt".format(name), 'w') as cert_file:
            cert_file.write(cert)
        cert_file.close()
        ssl = sslcertfile()
        ssl.name = "{0}.crt".format(name)
        ssl.src = "http://{0}/media/{1}.crt".format(URL, name)
        sslcertfile.Import(session, ssl)
        os.system("rm -f /opt/media/{0}.crt".format(name))
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def import_ssl(session, name, cert, pkey):
    try:
        ssl_cert = sslcertkey()
        ssl_cert.certkey = name
        ssl_cert_file(session, cert, name)
        ssl_key_file(session, pkey, name)
        ssl_cert.cert = "{0}.crt".format(name)
        ssl_cert.key = "{0}.key".format(name)
        sslcertkey.add(session, ssl_cert)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def import_root_ssl(session, name, cert):
    try:
        ssl_cert = sslcertkey()
        ssl_cert.certkey = name
        ssl_cert_file(session, cert, name)
        ssl_cert.cert = "{0}.crt".format(name)
        sslcertkey.add(session, ssl_cert)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        # raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        # raise exc


def ssl_link_root(session, sc_name, rsc_name):
    try:
        ssl_link = sslcertkey()
        ssl_link.certkey = sc_name
        ssl_link.linkcertkeyname = rsc_name
        sslcertkey.link(session, ssl_link)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def ssl_unlink(session, sc_name):
    try:
        ssl_link = sslcertkey()
        ssl_link.certkey = sc_name
        sslcertkey.unlink(session, ssl_link)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def delete_ssl(session, name):
    try:
        ssl_cert = sslcertkey()
        if sslcertkey.get(session, name).linkcertkeyname:
            ssl_unlink(session, name)
        ssl_cert.delete(session, name)
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def get_ssl(session, name):
    try:
        ssl = sslcertkey.get(session, name)
        return ssl
    except nitro_exception as exc:
        print("Exception::errorcode=" + str(exc.errorcode) + ",message=" + exc.message)
        raise exc
    except Exception as exc:
        print("Exception::message=" + str(exc.args))
        raise exc


def create_vlan(session, name, vlan_id):
    vlan_new = vlan()
    vlan_new.id = vlan_id
    vlan_new.vlantd