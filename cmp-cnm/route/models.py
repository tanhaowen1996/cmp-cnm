from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import StaticRoutingNetConfMixin

# Create your models here.


class StaticRoute(StaticRoutingNetConfMixin, models.Model):
    name = models.CharField(
        blank=True,
        max_length=100,
        # unique=True,
        verbose_name=_('static router name'))
    region = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=('region')
    )
    destination_subnet = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('destination subnet'))
    ip_next_hop_address = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('ip next hop address'))
    cluster_code = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('cluster code'))
    tenant_id = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('tenant id'))
    tenant_name = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=_('tenant name')
    )
    # creater = models.CharField(
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('creater'))
    created = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name=_('created time'))
    modified = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name=_('updated time')
    )
    status = models.IntegerField(
        blank=True,
        default='1',
        verbose_name=_('status')
    )

    class Meta:
        db_table = 'route'
        indexes = (BrinIndex(fields=['modified', 'created']),)
        ordering = ('-modified',)

    def create_route(self, destination_subnet, ip_next_hop_address,cluster_code):
        with self.get_netconf_conn() as conn:
            created, errors = self.create_static_routing(conn, destination_subnet, ip_next_hop_address, cluster_code)
            if errors:
                raise Exception(errors)

    def destroy_routing(self,destination_subnet, ip_next_hop_address, cluster_code):
        with self.get_netconf_conn() as conn:
            deleted, errors = self.delete_static_routing(conn, destination_subnet, ip_next_hop_address, cluster_code)
            if errors:
                raise Exception(errors)
