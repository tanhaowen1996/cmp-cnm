from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
from nssrc.com.citrix.netscaler.nitro.resource.config.lb import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ns import nsip
from nssrc.com.citrix.netscaler.nitro.resource.config.cs import csvserver
import uuid


class LoadBalance(models.Model):
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
    type = models.IntegerField(
        null=True,
        default=1
    )
    ip = models.CharField(
        null=True,
        max_length=64
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
        max_length=32
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
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)

    @classmethod
    def create_cslb(cls, ns_session, name, address):
        import pdb
        pdb.set_trace()
        new_csvs = csvserver.csvserver()
        new_csvs.name = name
        new_csvs.servicetype = "ANY"
        new_csvs.ipv46 = address
        new_csvs.port = "*"
        csvserver.csvserver.add(ns_session, new_csvs)


class LoadBalanceHost(models.Model):
    id = models.UUIDField(
        primary_key=True
    )
    listener_id = models.UUIDField(
        null=True
    )
    host = models.CharField(
        null=True,
        max_length=255
    )
    match_type = models.IntegerField(
        null=True,
        default=3
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated time'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created time'))

    class Meta:
        indexes = (BrinIndex(fields=['updated_at', 'created_at']),)


class LoadBalanceListener(models.Model):
    id = models.UUIDField(
        primary_key=True
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
    type = models.IntegerField(
        null=True
    )
    pip = models.IntegerField(
        null=True,
        default=2
    )
    ssl_id = models.CharField(
        null=True,
        max_length=16
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


class LoadBalanceMember(models.Model):
    id = models.UUIDField(
        primary_key=True
    )
    p_id = models.CharField(
        null=True,
        max_length=32
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


class LoadBalancePath(models.Model):
    id = models.UUIDField(
        primary_key=True
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
    match_type = models.IntegerField(
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


class SSL(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=16
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
    pkey = models.CharField(
        null=True,
        max_length=4096
    )
    status = models.IntegerField(
        null=True
    )
    cert_begin_time = models.DateTimeField(
        null=True
    )
    cert_end_time = models.DateTimeField(
        null=True
    )
    update_time = models.DateTimeField(
        null=True
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
