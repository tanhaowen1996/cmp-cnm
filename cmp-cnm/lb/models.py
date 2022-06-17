from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
from .citrixapi import client as citrix_client
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
    network_id = models.UUIDField(
        null=True
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
    status_desc = models.CharField(
        null=True,
        max_length=255
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
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)

    # def get_network(self, os_conn, ):
    #     pass

    @classmethod
    def create_cslb(cls, ns_session, name, address):
        citrix_client.create_lb(ns_session, name, address)

    def delete_cslb(self, ns_session, name):
        citrix_client.delete_lb(ns_session, name)

    def get_cslb(ns_session, name):
        return citrix_client.get_lb(ns_session, name)

    def get_ip(os_conn, network_id):

        network = os_conn.network.get_network(network_id)
        os_port = os_conn.network.create_port(
            network_id=network.id,
            description="Used by LodeBalance VIP",
            tags=["vip"],
            name="LoadBalance_VIP"
        )
        os_conn.network.update_port(
            port=os_port.id,
            tags=["vip"]
        )
        return os_port


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
    pip = models.CharField(
        null=True,
        max_length=64
    )
    # pip 取值：0：ingress, 1: egress, 2: address, 3: nwclss, 4: disable
    ssl_id = models.UUIDField(
        null=True,
    )
    algorithm = models.CharField(
        null=True,
        max_length=64
    )
    status = models.CharField(
        null=True,
        max_length=32
    )
    status_desc = models.CharField(
        null=True,
        max_length=255
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
    def create_lb_listener_v4(cls, ns_session,
                              name,
                              address,
                              port,
                              protocol,
                              lbmethod):
        citrix_client.create_lb_listener_v4(ns_session,
                                            name,
                                            address,
                                            port,
                                            protocol,
                                            lbmethod)

    @classmethod
    def create_lb_listener_v7(cls, ns_session, name, address, port, protocol):
        citrix_client.create_lb_listener_v7(ns_session, name, address, port, protocol)

    def delete_lb_listenet_v4(self, ns_session, name):
        citrix_client.delete_lb_listener_v4(ns_session, name)

    def delete_lb_listenet_v7_check(self, ns_session, name):
        return  citrix_client.delete_lb_listener_v7_check(ns_session, name)

    def delete_lb_listenet_v7(self, ns_session, name):
        citrix_client.delete_lb_listener_v7(ns_session, name)

    @classmethod
    def add_ssl(cls, ns_session, ssl_name, listener_name):
        citrix_client.add_ssl(session=ns_session, ssl_name=ssl_name, listener_name=listener_name)


class LoadBalanceHost(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LBHost_id')
    )
    name = models.CharField(
        null=True,
        max_length=255
    )
    listener_id = models.UUIDField(
        null=True
    )
    host = models.CharField(
        null=True,
        max_length=255
    )
    match_type = models.CharField(
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
    def create_lb_host(cls, ns_session, name, host, match_type, listener, protocol):
        citrix_client.create_lb_host(session=ns_session,
                                     name=name,
                                     host=host,
                                     match_type=match_type,
                                     listener=listener,
                                     protocol=protocol)

    def delete_lb_host(self, ns_session, lb_name):
        citrix_client.delete_lb_host(session=ns_session,
                                     lb_name=lb_name,
                                     host_name=self.name)


class LoadBalancePath(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LBPath id')
    )
    name = models.CharField(
        null=True,
        max_length=255
    )
    host_id = models.UUIDField(
        null=True
    )
    path = models.CharField(
        null=True,
        max_length=255
    )
    algorithm = models.CharField(
        null=True,
        max_length=64
    )
    match_type = models.CharField(
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
    def create_lb_path(cls,
                       ns_session,
                       listener,
                       name,
                       match_type,
                       host_match_type,
                       protocol,
                       lbmethod,
                       lb_host,
                       path):
        return citrix_client.create_lb_path(ns_session,
                                            listener,
                                            name,
                                            match_type,
                                            host_match_type,
                                            protocol,
                                            lbmethod,
                                            lb_host,
                                            path)

    def delete_lb_path(self, ns_session, lb_name):
        citrix_client.delete_lb_path(session=ns_session,
                                     csvs_name=lb_name,
                                     path_name=self.name)


class LoadBalanceMember(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('LBMember id')
    )
    p_id = models.UUIDField(
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


class SSL(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid1,
        verbose_name=_('SSL id')
    )
    name = models.CharField(
        null=True,
        max_length=128
    )
    scope = models.CharField(
        null=True,
        max_length=32
    )
    cert_type = models.CharField(
        null=True,
        max_length=16
    )
    domain = models.CharField(
        null=True,
        max_length=128
    )
    cert = models.TextField(
        null=True
    )
    pkey = models.TextField(
        null=True
    )
    status = models.CharField(
        null=True,
        max_length=64
    )
    cert_begin_time = models.CharField(
        null=True,
        max_length=255
    )
    cert_end_time = models.CharField(
        null=True,
        max_length=255
    )
    tenant_id = models.CharField(
        null=True,
        max_length=64
    )
    tenant_name = models.CharField(
        null=True,
        max_length=255
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
    def get_ssl(cls, ns_session, name):
        return citrix_client.get_ssl(ns_session, name)

    @classmethod
    def create_ssl(cls, ns_session, name, cert, pkey):
        list_cert = cert.split("-----END CERTIFICATE-----")
        if "" in list_cert:
            list_cert.remove("")
        cert_sc = list_cert[0] + "-----END CERTIFICATE-----"
        citrix_client.import_ssl(session=ns_session, name=name, cert=cert_sc, pkey=pkey)
        if len(list_cert) == 2:
            cert_root = list_cert[1] + "-----END CERTIFICATE-----"
            r_name = name + "-root"
            citrix_client.import_root_ssl(ns_session, name=r_name, cert=cert_root)
            citrix_client.ssl_link_root(ns_session, sc_name=name, rsc_name=r_name)

    def delete_ssl(self, ns_session, name):
        citrix_client.delete_ssl(ns_session, name)

