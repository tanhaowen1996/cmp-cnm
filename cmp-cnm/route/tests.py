from django.test import TestCase

# Create your tests here.
import requests


class Test:
    url = 'http://127.0.0.1:8000/v2'
    headers = {
        'Region': 'test',
        'Os-Token': 'gAAAAABjR3TcHWuPGG0Di7SbkXFcgfwiEzG3B_912ghErEq5Q8PVVozHjUML9hXnN7sJjpQgXxzvR_41wq4Fr68bwuYRA6w9t_-lh_DJKMF3n-yZmLkcpkOVz-L-kgRgEg2myBZTVJi5NB0m7hjVRHipJe9jScfqhzl1fZx2k3isBn7vUNlsBooY2VqKPdH95tb1RoYsJ4XG',
        'IsPlatform': '0',
        'ProjectId': 'a193a3b9161a4483b82fe61d13eb28dc'
    }

    def create_route(self):
        data = {
            'name': 'qwas112',
            'destination_subnet': '10.0.0.115',
            'ip_next_hop_address': '10.0.0.223',
            'cluster_code': '32'
        }
        req = requests.post(url=self.url+'/route',data=data,headers=self.headers)
        print(req.text)

    def delete_route(self):
        req = requests.delete(url=self.url+'/route/9', headers=self.headers)
        print(req)

    def get_route(self):
        req = requests.get(url=self.url+'/route',headers=self.headers)
        print(req.text)


    def create_firewall(self):
        data = {
            "name": "ASDFq12",
            "source_tenant_id": "123",
            "source_tenant_name": "123",
            "source_network": "10.209.8.1",
            "destination_tenant_id": "123",
            "destination_tenant_name": "123",
            "destination_network": "10.209.239.1",
        }
        req = requests.post(url=self.url+'/firewall', headers=self.headers, data=data)
        print(req.text)

    def delete_firewall(self,id):
        req = requests.delete(url=self.url+'/firewall/{}'.format(id), headers=self.headers)
        print(req)
    def update_firwewall(self,id):
        data = {
            'is_allow':'2'
        }
        req = requests.patch(url=self.url+'/firewall/{}'.format(id), headers=self.headers, data=data)
        print(req.text)

    def get_firewall(self):
        req = requests.get(url=self.url+'/firewall',headers=self.headers)
        print(req.text)

if __name__ == '__main__':
    test = Test()
    # test.create_route()
    # test.delete_route()
    # test.get_route()
    test.create_firewall()
    test.delete_firewall(27)
    test.update_firwewall(id)
    # test.get_firewall()