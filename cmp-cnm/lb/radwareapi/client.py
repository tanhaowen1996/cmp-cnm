import requests
from requests import exceptions
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from cmp_cnm.settings import RW_URL

urllib3.disable_warnings(InsecureRequestWarning)


def check_apply(session):
    check_url = RW_URL + "/monitor?prop=agApplyPending"
    apply_or_not = requests.get(url=check_url, auth=session, verify=False)
    response_dict = apply_or_not.json()
    apply_or_not = response_dict.get("agApplyPending")
    return apply_or_not


def apply_save(session):
    if check_apply(session=session) == 3:
        return
    apply_url = RW_URL + "/config?action=apply"
    save_url = RW_URL + "/config?action=save"
    requests.post(url=apply_url, auth=session, verify=False)
    apply_state_url = RW_URL + "/config?prop=agApplyConfig"
    apply_state = requests.get(url=apply_state_url, auth=session, verify=False)
    response_dict = apply_state.json()
    apply_state = response_dict.get("agApplyConfig")
    if apply_state == 5:
        apply_err_url = RW_URL + "/config/AgApplyTable"
        apply_err = requests.get(url=apply_err_url, auth=session, verify=False).json().get("StringVal")
        raise Exception(apply_err)
    requests.post(url=save_url, auth=session, verify=False)


def create_lb(session, lb_id, address):
    url = RW_URL + "/config/SlbNewCfgEnhVirtServerTable/" + lb_id + "/"
    payload = '''
    {
        "VirtServerIpAddress": %s,
        "VirtServerState": 2
    }
    '''
    payload = payload % address
    try:
        requests.post(url, auth=session, data=payload, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    # else:
    # return response.json()


def get_lb_list(session):
    url = RW_URL + "/config/SlbNewCfgEnhVirtServerTable"
    r = requests.get(url, auth=session, verify=False)
    response_dict = r.json()
    try:
        VServers = response_dict.get("SlbNewCfgEnhVirtServerTable")
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        return VServers


def get_lb(session, lb_id):
    url = RW_URL + "/config/SlbNewCfgEnhVirtServerTable/" + lb_id
    response = requests.get(url, auth=session, verify=False)
    response_dict = response.json()
    try:
        VServer = response_dict.get("SlbNewCfgEnhVirtServerTable")
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        return VServer


def delete_lb(session, lb_id):
    url = RW_URL + "/config/SlbNewCfgEnhVirtServerTable/" + lb_id
    try:
        requests.delete(url, auth=session, verify=False)
        lb_id_udp = lb_id + "_udp"
        if get_lb(session=session, lb_id=lb_id_udp):
            url = RW_URL + "/config/SlbNewCfgEnhVirtServerTable/" + lb_id_udp
            requests.delete(url, auth=session, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def create_listener(session, lb_id, listener_id, address, port, protocol, persistence):
    UDPBalance = 3
    PBind = 3
    if protocol == "UDP":  # 如果是udp协议的则重新创建一个新的负载均衡，该负载均衡不被数据库记录，查询时通过id_udp查询
        UDPBalance = 2
        lb_id = lb_id + "_udp"
        if not get_lb(session=session, lb_id=lb_id):
            create_lb(session=session, lb_id=lb_id, address=address)
    lb = get_lb_listener_list(session=session, lb_id=lb_id)
    index = 1
    if lb:
        for index in range(1, len(lb) + 1):
            if index != lb[index - 1].get("Index"):
                break
            index = index + 1
        # index = lb[len(lb) - 1].get("Index") + 1
    create_group(session=session, listener_id=listener_id)
    url1 = RW_URL + "/config/SlbNewCfgEnhVirtServicesTable/" + lb_id + "/" + str(index)
    if persistence:
        PBind = 2
    payload1 = '''
                {
                    "VirtPort": %d,
                    "RealPort": 0,
                    "DBind": 2,
                    "PBind": %d,
                    "UDPBalance": %d
                }
                '''
    payload1 = payload1 % (port, PBind, UDPBalance)
    requests.post(url=url1, auth=session, data=payload1, verify=False)
    url5 = RW_URL + "/config/SlbNewCfgEnhVirtServicesFifthPartTable/" + lb_id + "/" + str(index)
    ServApplicationType = 1
    if port == 443:
        ServApplicationType = 8
    if port == 80:
        ServApplicationType = 6
        # url1 = RW_URL + "/config/SlbNewCfgEnhVirtServicesTable/" + lb_id + "/" + str(index)
        # payload1 = '''
        #             {
        #                 "NonHTTP": 1
        #             }
        #             '''
        # requests.put(url=url1, auth=session, data=payload1, verify=False)
    payload5 = '''
            {
                "ServApplicationType": %s
            }
            '''
    payload5 = payload5 % ServApplicationType
    requests.put(url=url5, auth=session, data=payload5, verify=False)
    payload7 = '''
        {
            "RealGroup": %s,
            "PersistentTimeOut": 0,
            "ProxyIpMode": 2,
            "ProxyIpaddr": %s,
            "ProxyIpMask": "255.255.255.255"
        }
        '''
    payload7 = payload7 % (listener_id, address)
    # import pdb
    # pdb.set_trace()
    url7 = RW_URL + "/config/SlbNewCfgEnhVirtServicesSeventhPartTable/" + lb_id + "/" + str(index)
    try:
        requests.put(url=url7, auth=session, data=payload7, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def get_lb_listener_list(session, lb_id):
    url = RW_URL + "/config/SlbNewCfgEnhVirtServicesTable/" + lb_id
    try:
        response = requests.get(url=url, auth=session, verify=False)
        response_dict = response.json()
        VService = response_dict.get("SlbNewCfgEnhVirtServicesTable")
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        return VService


def get_listener_index(session, lb_id, port):
    VServices = get_lb_listener_list(session=session, lb_id=lb_id)
    for VService in VServices:
        if port == VService.get("VirtPort"):
            return VService.get("Index")
    return 1


def get_listener(session, lb_id, port):
    index = get_listener_index(session=session, lb_id=lb_id, port=port)
    url = RW_URL + "/config/SlbNewCfgEnhVirtServicesTable/" + lb_id + "/" + str(index)
    try:
        response = requests.get(url=url, auth=session, verify=False)
        response_dict = response.json()
        VService = response_dict.get("SlbNewCfgEnhVirtServicesTable")
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    else:
        return VService


def delete_listener(session, lb_id, port, listener_id, protocol):
    if protocol == "UDP":
        lb_id = lb_id + "_udp"
    index = get_listener_index(session=session, lb_id=lb_id, port=port)
    url = RW_URL + "/config/SlbNewCfgEnhVirtServicesTable/" + lb_id + "/" + str(index)
    try:
        requests.delete(url=url, auth=session, verify=False)
        delete_group(session=session, listener_id=listener_id)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def create_group(session, listener_id):
    url = RW_URL + "/config/SlbNewCfgEnhGroupTable/" + listener_id
    payload = '''
        {
            "Metric": 1,
            "HealthCheckLayer": 2
        }
        '''
    try:
        requests.post(url=url, auth=session, data=payload, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def delete_group(session, listener_id):
    url = RW_URL + "/config/SlbNewCfgEnhGroupTable/" + listener_id
    try:
        requests.delete(url=url, auth=session, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def create_member(session, member_id, ip, port, weight):
    url = RW_URL + "/config/SlbNewCfgEnhRealServerTable/" + member_id
    payload = '''
            {
                "IpAddr": %s,
                "State": 2,
                "Type": 1,
                "Weight": %d
            }
            '''
    payload = payload % (ip, weight)
    try:
        requests.post(url=url, auth=session, data=payload, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)
    payload_port = '''
            {
                "RealPort": %d
            }
            '''
    payload_port = payload_port % port
    url_port = RW_URL + "/config/SlbNewCfgEnhRealServPortTable/" + member_id + "/1"
    try:
        requests.post(url=url_port, auth=session, data=payload_port, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def add_member(session, ip, port, member_id, weight, listener_id):
    create_member(session=session, member_id=member_id, ip=ip, port=port, weight=weight)
    url = RW_URL + "/config/SlbNewCfgEnhGroupTable/" + listener_id
    payload = '''
                {
                    "AddServer": %s
                }
                '''
    payload = payload % member_id
    try:
        requests.put(url=url, auth=session, data=payload, verify=False)
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def delete_member(session, member_id):
    url = RW_URL + "/config/SlbNewCfgEnhRealServerTable/" + member_id
    try:
        requests.delete(url=url, auth=session, verify=False)  # 需要保证每个member都只被唯一一个group使用
    except exceptions.Timeout as e:
        print(e)
    except exceptions.HTTPError as e:
        print(e)


def get_members(session, listener_id):
    url = RW_URL + "/config/SlbEnhGroupRealServersTable/" + listener_id
    response = requests.get(url=url, auth=session, verify=False)
    response_dict = response.json()
    VService = response_dict.get("SlbEnhGroupRealServersTable")
    return VService


def get_member_info(session, member_id):
    url = RW_URL + "/config/SlbEnhRealServerInfoTable/" + member_id
    response = requests.get(url=url, auth=session, verify=False)
    response_dict = response.json()
    member = response_dict.get("SlbEnhRealServerInfoTable")
    return member


def lb_member_list(session, listener_id):
    url = RW_URL + "/config/SlbNewCfgEnhGroupRealServerTable/" + listener_id
    member_r = requests.get(url, auth=session, verify=False)
    response_dict_member = member_r.json()
    members = response_dict_member.get("SlbNewCfgEnhGroupRealServerTable")
    return members


def get_member(session, member_id):
    url = RW_URL + "/config/SlbNewCfgEnhRealServPortTable/" + member_id
    response = requests.get(url=url, auth=session, verify=False)
    response_dict = response.json()
    member = response_dict.get("SlbNewCfgEnhRealServPortTable")
    return member

