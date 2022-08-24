import requests
from requests.auth import HTTPBasicAuth
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)


url = "https://10.210.240.254/config/SlbCurCfgEnhVirtServerTable"
user_pwd = "admin:radware"


r = requests.get(url, auth=HTTPBasicAuth('admin', 'radware'), verify=False)
print(r.status_code)

respone_dict = r.json()

vs = respone_dict.get("SlbCurCfgEnhVirtServerTable")

for v in vs:
    print(v)
