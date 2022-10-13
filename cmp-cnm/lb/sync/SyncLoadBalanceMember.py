import json

import requests
from apscheduler.schedulers.background import BackgroundScheduler

from lb.citrixapi.session import NSMixin
from lb.models import LoadBalance, LoadBalanceListener, LoadBalanceMember
from lb.radwareapi.session import RWMixin
from cmp_cnm.settings import WEBHOOK_URL


def CheckLoadBalanceMember():
    ns_conn = NSMixin.get_session()
    rw_conn = RWMixin.get_session()
    listeners = LoadBalanceListener.objects.all()
    try:
        for listener in listeners:
            lb = LoadBalance.objects.get(id=listener.lb_id)
            db_member = []
            real_member = []
            if lb.provider == "citrix":
                ns_members = LoadBalanceMember.get_ns_members(ns_session=ns_conn,
                                                              name=listener.real_listener_identifier)
                if ns_members:
                    for ns_member in ns_members:
                        real_member.append(ns_member.servicename)
            else:
                rw_members = LoadBalanceMember.get_rw_members(rw_session=rw_conn,
                                                              listener_id=listener.real_listener_identifier)
                if rw_members:
                    for rw_member in rw_members:
                        real_member.append(rw_member.get("ServIndex"))
            members = LoadBalanceMember.objects.filter(listener_id=listener.id)
            for member in members:
                db_member.append(member.real_member_identifier)

            if set(db_member).difference(set(real_member)) or set(real_member).difference(set(db_member)):
                print('数据不一致 %s' % listener.id)
                webhook_url = WEBHOOK_URL
                data = {
                    "msgtype": "markdown",
                    "markdown": {"content": "负载均衡设备数据与数据库数据不一致，请及时同步"}
                }
                r = requests.post(url=webhook_url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
                                  verify=False)
                return
    except Exception as e:
        print(e)


scheduler = BackgroundScheduler()

scheduler.add_job(CheckLoadBalanceMember, 'cron', month='*', day='*', hour=23, minute=59, second=00)

scheduler.start()

