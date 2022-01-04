from django.test import TestCase

# Create your tests here.

from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
# from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_binding import lbvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_cspolicy_binding import csvserver_cspolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.cspolicy import cspolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey_sslvserver_binding import sslcertkey_sslvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey_binding import sslcertkey_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey_service_binding import sslcertkey_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslvserver_sslcertkey_binding import sslvserver_sslcertkey_binding
import os


ns_session = nitro_service("10.208.240.252", "http")
# ns_session.login("nsroot", "u&ht3&lV#v7", 3600)
ns_session.login("fzyh_mawei", "fzyh_mawei_yh601933", 3600)



ssl = sslvserver_sslcertkey_binding()
ssl.vservername = "10.208.224.123:443-SSL"
ssl.certkeyname = "yonghui.cn"
sslvserver_sslcertkey_binding.add(ns_session, ssl)
# sslvserver_sslcertkey_binding.delete(ns_session, ssl)


# lb_vserver = lbvserver()
# lb_vserver.name = "lllllll"
# lb_vserver.servicetype = "TCP"
# lb_vserver.lbmethod = "ROUNDROBIN"
# lbvserver.add(ns_session, lb_vserver)


# lb_vs = lbvserver_service_binding()
# lb_vs.name = "10.208.224.123:22-TCP-lbvs"
# lb_vs.servicename = "10.208.224.105:22-TCP"
#
# lbvserver_service_binding.delete(ns_session, lb_vs)

# cs = csvserver()
# cs = csvserver_cspolicy_binding()
# cs.policyname = "10.208.224.123:8090-HTTP-testeeddss"
# cs.name = "10.208.224.123:8090-HTTP"
# cs.priority = 1000
# ss=csvserver.get(ns_session, "http-vm-80")
# csvserver_cspolicy_binding.delete(ns_session, cs)
# ssl = sslcertkey()
# ssl.certkey = "test"
# cert = """-----BEGIN CERTIFICATE-----
# MIIHXjCCBkagAwIBAgIQC4iI0orj/ZTvieHx3yvIgDANBgkqhkiG9w0BAQsFADBE
# MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMR4wHAYDVQQDExVH
# ZW9UcnVzdCBSU0EgQ04gQ0EgRzIwHhcNMjEwNzE1MDAwMDAwWhcNMjIwODA0MjM1
# OTU5WjB1MQswCQYDVQQGEwJDTjESMBAGA1UECAwJ56aP5bu655yBMRIwEAYDVQQH
# DAnnpo/lt57luIIxJzAlBgNVBAoMHuawuOi+iei2heW4guiCoeS7veaciemZkOWF
# rOWPuDEVMBMGA1UEAwwMKi55b25naHVpLmNuMIICIjANBgkqhkiG9w0BAQEFAAOC
# Ag8AMIICCgKCAgEApnnp46TrHUq0rY/0milamEkdMQZS6RqLdyXnzJxzlf9MEqot
# Qo1JMhvWW8NrTYoxd1bfVIcpeLcEVB+2lU/0Ehu12sRS55BdWF7IJDXG8q1+ke+2
# aS4Eix50KHP2uUMoeYTu0e+MUpik9M6NcfjejleaFY3wRqXCOMwxVyKhcEAkSg5b
# kJPeSNi8NJaCcavyVGbapDfc/ZgVkW+e4ZQYUwRy18SFONOf6BXG3Ri2sWcQS6TM
# KouQ/ur5+Dm0eJemQ7TsCTD4U8LucM49BrZQqh8vO9CmYs8MW0lb4fZnNDvfhHkT
# 27MoVXrgAU7rUFhjesSGzkUQWZItUoBVgjzf6ivJ/5EgDKOeormfoIbbvTvVErw2
# 7bRyt3dKax3+CyZAD1dPMgrd3vex3uviU87LJ8FZRJJF87G/VcdyrMdkeSgMXf8i
# +0RsXU2iEaUlsdRUVgtaypwyYQNYLDVuBUqu7YxvUpLy303h9otEQwn9S0E0hRH2
# eKqbIkOkWEMjp9Hr7ivYQQB0n1tHdq31HuteBFA6u01hj/tZ15vlE7rCghHjzWTJ
# mpTTLcVWchVDkOcF9HxBYxMGGjXUvksIsgUFXhOorvbu14Nw9jT3MbmO0gRl77cD
# Uxh7mlkeVECQixY1+ruTANbmk+XY/67kbURTbEBPa7YdJbRgFPyW2geuRM8CAwEA
# AaOCAxkwggMVMB8GA1UdIwQYMBaAFCRvkT+Jh4cOMsJAGN/FTOtPyEkyMB0GA1Ud
# DgQWBBRtE8HvnMM3hh5S90U3EX+iojqG1DAjBgNVHREEHDAaggwqLnlvbmdodWku
# Y26CCnlvbmdodWkuY24wDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUF
# BwMBBggrBgEFBQcDAjA9BgNVHR8ENjA0MDKgMKAuhixodHRwOi8vY3JsLmRpZ2lj
# ZXJ0LmNuL0dlb1RydXN0UlNBQ05DQUcyLmNybDA+BgNVHSAENzA1MDMGBmeBDAEC
# AjApMCcGCCsGAQUFBwIBFhtodHRwOi8vd3d3LmRpZ2ljZXJ0LmNvbS9DUFMwcQYI
# KwYBBQUHAQEEZTBjMCMGCCsGAQUFBzABhhdodHRwOi8vb2NzcC5kaWdpY2VydC5j
# bjA8BggrBgEFBQcwAoYwaHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY24vR2VvVHJ1
# c3RSU0FDTkNBRzIuY3J0MAwGA1UdEwEB/wQCMAAwggF9BgorBgEEAdZ5AgQCBIIB
# bQSCAWkBZwB2AEalVet1+pEgMLWiiWn0830RLEF0vv1JuIWr8vxw/m1HAAABeqgb
# os8AAAQDAEcwRQIhAN8vYs57tSMwG3lHALolEFvITbg1DR8l1lA8uzX5E8ugAiB7
# GxSGAmW1sAjoiww7PraqbmdVXBrn1cLvbWcfHCL4sgB2AEHIyrHfIkZKEMahOglC
# h15OMYsbA+vrS8do8JBilgb2AAABeqgbom0AAAQDAEcwRQIgf+uOicvpuskESyGI
# I0XjQ75AtYG6+jq5xtjlj9jAwSwCIQDhR2sDDtpAA63SHKuqvYo82yhXxUOOebeA
# UlIPrFuX9AB1AN+lXqtogk8fbK3uuF9OPlrqzaISpGpejjsSwCBEXCpzAAABeqgb
# oqcAAAQDAEYwRAIgH+qbWkZnBDoFugJJbDz2LBnoC4Ae3W3eoIQgPflOu9MCIEcD
# Aiz4Az8pHC4TeYIq7b0Bd+ot7Xx5Nqu0OInSRGSqMA0GCSqGSIb3DQEBCwUAA4IB
# AQCBf3Ak2cT6rJ36NXXqHYgpsJUXCCwFMkdHlBVqy7RfpMrDw0OE3QkZAAg+bs4A
# XXhxLPTx7RVLui+1+4T06Y2MBItAV1jKgRRYiBxI6KVbimvzT9MS9933OG4s9D/I
# hPoOfmc9tJKnh2WgIIf1LAwIT//M3/xL4SfDzAk6Zw2k0z1ivFzUbphljKDy45u/
# ZaQ7ue25oQ+8mGPy38Wn017ETeXPzdkiKZ/hgNGq4innbVYDjyapJw5zlMmNknUk
# rBnhyRl2avW5vvF6RMFl9SjZ12oX1fDOfm4OQY4DOZ6RznuYRqSB5c2J796j7wvu
# rudxq3PqJX90EhV/Kn0VzI3u
# -----END CERTIFICATE-----"""
# key = """-----BEGIN CERTIFICATE-----
# MIIFDzCCA/egAwIBAgIQCxNitu5qnT6WiTDxbiB9OTANBgkqhkiG9w0BAQsFADBh
# MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
# d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBD
# QTAeFw0yMDAzMDQxMjA0NDBaFw0zMDAzMDQxMjA0NDBaMEQxCzAJBgNVBAYTAlVT
# MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxHjAcBgNVBAMTFUdlb1RydXN0IFJTQSBD
# TiBDQSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANA1OZJJtZUI
# 7zj4qFHT79g+Otks4TEfmUEDhrNKBEEjb/i29GBfnpvFdT36azCg2VODJRSjIzFn
# 4qADcc84EmfKiDEM97HFsQPp9RRkqxH5cB51EU2eBE9Ua95x+wQp/KSdCqITCQ/v
# yvm3J4Upjl0wlW8wRCPCWcYw3pKClGRkNzVtI1KXnfpn7fG3N84n7wlBb9IGKJFa
# c/6+hxvZx2qnfLsxdIKR0Q/biGoU6Z8Iy/R/p7GoPO8vamV090+QHEL5AdSzKtEh
# U9vdvcuWjjLxVnaJLfj/6WoGZj8UWn3zFbEoTVaAfp2xqdzW7yRvi2r148m9ev7l
# jDqHo8UX69sCAwEAAaOCAd4wggHaMB0GA1UdDgQWBBQkb5E/iYeHDjLCQBjfxUzr
# T8hJMjAfBgNVHSMEGDAWgBQD3lA1VtFMu2bwo+IbG8OXsj3RVTAOBgNVHQ8BAf8E
# BAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQI
# MAYBAf8CAQAwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzABhhdodHRwOi8vb2Nz
# cC5kaWdpY2VydC5jbjBABgNVHR8EOTA3MDWgM6Axhi9odHRwOi8vY3JsLmRpZ2lj
# ZXJ0LmNuL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNybDCB3QYDVR0gBIHVMIHSMIHF
# BglghkgBhv1sAQEwgbcwKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3LmRpZ2ljZXJ0
# LmNvbS9DUFMwgYoGCCsGAQUFBwICMH4MfEFueSB1c2Ugb2YgdGhpcyBDZXJ0aWZp
# Y2F0ZSBjb25zdGl0dXRlcyBhY2NlcHRhbmNlIG9mIHRoZSBSZWx5aW5nIFBhcnR5
# IEFncmVlbWVudCBsb2NhdGVkIGF0IGh0dHBzOi8vd3d3LmRpZ2ljZXJ0LmNvbS9y
# cGEtdWEwCAYGZ4EMAQICMA0GCSqGSIb3DQEBCwUAA4IBAQCzkcXq0TN0oSn4UeXp
# FBW7U8zrHBIhH9MXHNBp+Yy/yN19133UY05uuHXHaU2Uv0hxefckjPdkaX7ARso+
# O3Ar6nf7YfBwCqSpqsNckKT7KKtf3Ot95wYFpKDa64jcRUfxzRWnmq12IVzczqHI
# sIvUZQINw/UHSQcWekdUnMg58bQSHyTjwkj9jcX2RURxaVZkr15wxo/Z3Ydo2PVK
# 3afEr0/vcuFvE7QeGXiI2DJdVt3JefatZ3rj4VTW2aUZwHGUiWWIUudBfQKR0JEp
# lJ8MFaKDh4/A2VEJnXILu1iwvc1m3jCaPuzZKdoHM/1234bznJI2aAfhfIhoHw90
# tPO+
# -----END CERTIFICATE-----
# """
#
# with open('/tmp/test.crt', 'w') as cert_file:
#     cert_file.write(cert)
# cert_file.close()
# with open('/tmp/test.key', 'w') as key_file:
#     key_file.write(key)
# key_file.close()
# os.path = "/tmp/"
# ssl.cert = "test.crt"
# ssl.key = "test.key"
# sslcertkey.add(ns_session, ssl)
# ssl_name = ssl.get(ns_session, "yonghui.cn")


# lb_service = service()
# result = lb_service.get(ns_session, "vm1-http")
# print(result)

# lb_path = cspolicy()
# name = "vm-test"
# for i in range(1, 10):
#     policy_name = name+str(i)
#     try:
#         lb_path.get(ns_session, policy_name)
#     except:
#         name = policy_name
#         break


# resource = lb_path.get(ns_session, "vm-test")


#
# lb_member = lbvserver_service_binding()
# lb_member.servicename = "10.208.16.103:80"
# lb_member.ipv46 = "address"
# lb_member.servicetype = "HTTP"
# lb_member.weight = 2
# lb_member.name = "test-4"
# result = lbvserver_service_binding.add(ns_session, lb_member)

# result = lbvserver_service_binding.get(ns_session, "yonghui.cn:80")
# import pdb
# pdb.set_trace()
# print(result.get_lbvserver_service_bindings())
# if result:
#     for i in range(len(result)):
#         if result[i].get_lbvserver_service_bindings() :
#             print("getlbvs_svc_bind_bulk - version= "+result[i].name + ", services= " + result[i].lbvserver_service_bindings.length)
# else:
#     print("getlbvs_svc_bind_bulk - Done")



# lb_vserver = lbvserver()
# lb_vserver.name = "name"
# lb_vserver.servicetype = "HTTP"
# lbvserver.add(ns_session, lb_vserver)

# obj = lbvserver_binding()
# obj.name = "lb_vip"
# result = lbvserver_binding.lbvserver_service_bindings(ns_session, "yonghui.cn:80")
import pdb
pdb.set_trace()
# if result:
#     print("getlbvserver_bindings result::name="+result.name)
# else:
#     print("getlbvserver_svc_bindings :: Done")

# url = "http://10.208.240.252/nitro/v1/config/login"
# headers = {
#     "Content-Type": "application/json"
# }
# request_body = {
#     "login": {
#         "username": "fzyh_mawei",
#         "password": "fzyh_mawei_yh601933"
#     }
# }
# request_body = json.dumps(request_body)
# res = requests.post(url, data=request_body, headers=headers)
#
# url = "http://10.208.240.252/nitro/v1/config/lbvserver"
# headers = {
#     "Cookie": "sessionid={0}".format(json.loads(res.text).get("sessionid")),
#     "Content-Type": "application/json"
# }
# request_body = {
#     "lbvserver": {
#         "name": "thw3",
#         "servicetype": "http",
#         "ipv46": "10.208.224.20",
#         "port": 8080,
#     }
# }
# request_body = json.dumps(request_body)
# res = requests.post(url, data=request_body, headers=headers)
# import pdb
# pdb.set_trace()

# new_lbvserver_obj = lbvserver.lbvserver.get(ns_session, "test-vm-1")


#
# lbvserver.lbvserver  1
# lbparameter.lbparameter.
# lbmonitor.lbmonitor.  1
# lbmetrictable   1
# lbmonbindings
# lbgroup.lbgroup.
# lbprofile
# lbroute
# lbroute6
# lbsipparameters
# lbwlm








# print(new_lbvserver_obj.name)
# print(new_lbvserver_obj.servicetype)

# new_ip = nsip.nsip()
# new_ip.ipaddress = "10.208.224.19"
# new_ip.type = "SNIP"
# new_ip.netmask = "255.255.255.0"
#
# nsip.nsip.add(ns_session, new_ip)


# new_lb_service = lbmonbindings_service_binding.lbmonbindings_service_binding()
# new_lb_service.servicename = "thw-1"
# new_lb_service.ipaddress = "10.208.224.89"
# new_lb_service.port = 88
# new_lb_service.Servicetype = "HTTP"
# lbmonbindings_service_binding.lbmonbindings_service_binding.add_resource(ns_session, new_lb_service)
# new_lbvserver_obj = lbvserver.lbvserver()
# new_lbvserver_obj.name = "thw22"
# new_lbvserver_obj.ipv46 = "10.208.240.89"
# new_lbvserver_obj.port = 8080
# new_lbvserver_obj.servicetype = "HTTP"

# new_lbvserver_obj.lbmethod = "ROUNDROBIN"
#
# #Upload the resource to CItrix ADC
# lb = lbvserver.lbvserver.add(ns_session, new_lbvserver_obj)

# import pdb
# pdb.set_trace()


