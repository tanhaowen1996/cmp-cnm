
from nssrc.com.citrix.netscaler.nitro.resource.config.lb import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.ns import nsip
from nssrc.com.citrix.netscaler.nitro.resource.config.cs import csvserver


def create_lb(session, name, address):
    csvs = csvserver.csvserver()
    csvs.name = name
    csvs.servicetype = "ANY"
    csvs.ipv46 = address
    csvs.port = "*"
    csvserver.csvserver.add(session, csvs)

