from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _
from .utils import FirewallNetConfMixin


class Firewall(FirewallNetConfMixin, models.Model):
    rule_id = models.IntegerField(
        blank=True,
        verbose_name=_('id')
    )
    name = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('name')
    )
    # source_tenant_id = models.CharField(
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('source_tenant_id')
    # )
    # source_tenant_name = models.CharField(
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('source_tenant_name')
    # )
    source_network = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('source_network')
    )
    # destination_tenant_id = models.CharField(
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('destination_tenant_id')
    # )
    # destination_tenant_name = models.CharField(
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('destination_tenant_name')
    # )
    destination_network = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('destination_network')
    )
    is_allow = models.IntegerField(
        blank=True,
        default='2',
        verbose_name=_('is_allow')
    )
    tenant_id = models.CharField(
        blank=True,
        max_length=100,
        verbose_name=_('tenant id')
    )
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
    region = models.CharField(
        blank=True,
        max_length=30,
        verbose_name=('region')
    )
    status = models.IntegerField(
        blank=True,
        default='1',
        verbose_name=_('status')
    )

    class Meta:
        db_table = 'firewall'
        indexes = (BrinIndex(fields=['modified', 'created']),)
        ordering = ('-modified',)

    def create_rule_id(self):
        with self.get_netconf_conn() as conn:
            rule_id = self.preset_security_policy_id(conn)
            return rule_id
    def create_security_policy(self,rule_id, name, zone_source_network, zone_destination_network):
        with self.get_netconf_conn() as conn:
            self.create_security_policy_rule(conn,rule_id, name, zone_source_network, zone_destination_network)

    def delete_security_policy(self,rule_id):
        with self.get_netconf_conn() as conn:
            self.delete_security_policy_rule(conn, rule_id)

    def update_security_policy(self,rule_id, is_allow):
        with self.get_netconf_conn() as conn:
            self.update_security_policy_rule(conn, rule_id, is_allow)

    def get_securityzone(self, zone_source_network, zone_destination_network):
        with self.get_netconf_conn() as conn:
            securityzone_name_list= self.get_interface_securityzone(conn, zone_source_network, zone_destination_network)
            return securityzone_name_list

    def get_interface_network_list(self):
        with self.get_netconf_conn() as conn:
            network_list = self.get_interface_network(conn)
            return network_list

