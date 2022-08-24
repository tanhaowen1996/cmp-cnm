
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from cmp_cnm.settings import NS_HOST, NS_TIME, NS_USER, NS_PASSWD, NS_PROTOCOL


class NSMixin:

    @staticmethod
    def get_session():
        ns_session = nitro_service(NS_HOST, NS_PROTOCOL)
        ns_session.login(NS_USER, NS_PASSWD, NS_TIME)
        return ns_session
