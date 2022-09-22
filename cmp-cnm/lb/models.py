from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
from .citrixapi import client as citrix_client
from .radwareapi import client as radware_client
from .utils import OpenstackMixin
import uuid


class LoadBalance(models.Model, OpenstackMixin):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LB id')
    )
    name = models.CharField(
        null=True,
        max_length=256
    )
    net_type = models.CharField(
        null=True,
        max_length=64
    )
    ip = models.CharField(
        null=True,
        max_length=64
    )
    network_id = models.CharField(
        null=True,
        max_length=128
    )
    subnet_id = models.CharField(
        null=True,
        max_length=128
    )
    port_id = models.CharField(
        null=True,
        max_length=128
    )
    provider = models.CharField(
        null=True,
        max_length=32,
        default="citrix"
    )
    status = models.CharField(
        null=True,
        max_length=32
    )
    description = models.CharField(
        null=True,
        max_length=255
    )
    tenant_id = models.CharField(
        null=True,
        max_length=32
    )
    tenant_name = models.CharField(
        null=True,
        max_length=128
    )
    real_lb_identifier = models.CharField(
        null=True,
        max_length=64
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)

    @classmethod
    def create_nslb(cls, ns_session, name, address):
        pass
        # citrix_client.create_lb(ns_session, name, address)

    def delete_nslb(self, ns_session, name):
        # import pdb
        # pdb.set_trace()
        if citrix_client.get_lb(session=ns_session, name=name):
            citrix_client.delete_lb(ns_session, name)
        pass
        # citrix_client.delete_lb(ns_session, name)

    def get_ip(os_conn, network_id):
        network = os_conn.network.get_network(network_id)
        os_port = os_conn.network.create_port(
            network_id=network.id,
            description="Used by LodeBalance VIP",
            name="LoadBalance_VIP"
        )
        os_conn.network.set_tags(
            os_port,
            tags=["vip"]
        )
        return os_port

    # def get_cslb(ns_session, name):
    #     return citrix_client.get_lb(ns_session, name)
    def create_rwlb(rw_session, lb_id, address):
        radware_client.create_lb(session=rw_session, lb_id=lb_id, address=address)

    def delete_rwlb(rw_session, lb_id):
        radware_client.delete_lb(session=rw_session, lb_id=str(lb_id))



class LoadBalanceListener(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LBListener id')
    )
    name = models.CharField(
        null=True,
        max_length=128
    )
    lb_id = models.UUIDField(
        null=True
    )
    protocol = models.CharField(
        null=True,
        max_length=16
    )
    port = models.IntegerField(
        null=True
    )
    type = models.CharField(
        null=True,
        max_length=64
    )
    algorithm = models.CharField(
        null=True,
        max_length=64
    )
    status = models.CharField(
        null=True,
        max_length=32
    )
    member_num = models.IntegerField(
        null=True
    )
    all_member = models.TextField(
        null=True
    )
    real_listener_identifier = models.CharField(
        null=True,
        max_length=64
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)

    @classmethod
    def create_lb_listener(cls, ns_session,
                           name,
                           address,
                           port,
                           protocol,
                           lbmethod):
        citrix_client.create_lb_listener(ns_session,
                                         name,
                                         address,
                                         port,
                                         protocol,
                                         lbmethod)

    def delete_lb_listener(self, ns_session, name):
        citrix_client.delete_lb_listener(ns_session, name)

    def delete_csvs(self, ns_session, name):
        citrix_client.delete_lb_listener_csvs(ns_session, name)

    def get_status(ns_session, name):
        listener = citrix_client.get_lbvs(session=ns_session, name=name)
        member = citrix_client.lb_vs_member_list(session=ns_session, lb_vs_name=name)
        return listener, member

    def create_rd_lb_listener(rw_session, lb_id, listener_id, address, port, protocol):
        radware_client.create_listener(session=rw_session,
                                       lb_id=str(lb_id),
                                       listener_id=str(listener_id),
                                       address=address,
                                       port=port,
                                       protocol=protocol)

    def delete_rw_listener(rw_session, lb_id, port, listener_id, protocol):
        radware_client.delete_listener(session=rw_session,
                                       lb_id=str(lb_id),
                                       port=port,
                                       listener_id=str(listener_id),
                                       protocol=protocol)


class LoadBalanceMember(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LBMember id')
    )
    listener_id = models.UUIDField(
        null=True
    )
    ip = models.CharField(
        null=True,
        max_length=32
    )
    port = models.IntegerField(
        null=True
    )
    weight = models.IntegerField(
        null=True
    )
    real_member_identifier = models.CharField(
        null=True,
        max_length=64
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)

    @classmethod
    def add_member(cls, ns_session, address,
                   port, weight, protocol, vs_name):
        citrix_client.add_lb_member(ns_session,
                                    address,
                                    port,
                                    weight,
                                    protocol,
                                    vs_name)

    def delete_lb_member(self, ns_session, lbvs_name, member_name):
        citrix_client.delete_lb_member(session=ns_session, name=lbvs_name, member_name=member_name)

    def update_lb_member(self, ns_session, lbvs_name, member_name, ip, port, weight, protocol):
        citrix_client.update_lb_member(ns_session, lbvs_name, member_name, ip, port, weight, protocol)

    def add_rw_member(rw_session, ip, port, member_id, listener_id, weight=1):
        radware_client.add_member(session=rw_session,
                                  ip=ip, port=port,
                                  member_id=str(member_id),
                                  weight=weight,
                                  listener_id=str(listener_id))

    def delete_rw_member(rw_session, member_id):
        radware_client.delete_member(session=rw_session, member_id=str(member_id))

    def get_info_member(rw_session, member_id):
        return radware_client.get_member_info(session=rw_session, member_id=str(member_id))

    def get_ns_members(ns_session, name):
        members = citrix_client.lb_vs_member_list(session=ns_session, lb_vs_name=name)
        return members

    def get_rw_members(rw_session, listener_id):
        members = radware_client.lb_member_list(session=rw_session, listener_id=str(listener_id))
        return members
