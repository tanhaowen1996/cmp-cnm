from requests.auth import HTTPBasicAuth
from cmp_cnm.settings import RW_USER, RW_PASSWD


class RWMixin:

    @staticmethod
    def get_session():
        rw_session = HTTPBasicAuth(RW_USER, RW_PASSWD)
        return rw_session
