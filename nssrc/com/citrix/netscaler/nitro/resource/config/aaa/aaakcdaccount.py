#
# Copyright (c) 2021 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class aaakcdaccount(base_resource) :
	""" Configuration for Kerberos constrained delegation account resource. """
	def __init__(self) :
		self._kcdaccount = None
		self._keytab = None
		self._realmstr = None
		self._delegateduser = None
		self._kcdpassword = None
		self._usercert = None
		self._cacert = None
		self._userrealm = None
		self._enterpriserealm = None
		self._servicespn = None
		self._principle = None
		self._kcdspn = None
		self.___count = None

	@property
	def kcdaccount(self) :
		r"""The name of the KCD account.<br/>Minimum length =  1.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		r"""The name of the KCD account.<br/>Minimum length =  1
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def keytab(self) :
		r"""The path to the keytab file. If specified other parameters in this command need not be given.
		"""
		try :
			return self._keytab
		except Exception as e:
			raise e

	@keytab.setter
	def keytab(self, keytab) :
		r"""The path to the keytab file. If specified other parameters in this command need not be given.
		"""
		try :
			self._keytab = keytab
		except Exception as e:
			raise e

	@property
	def realmstr(self) :
		r"""Kerberos Realm.
		"""
		try :
			return self._realmstr
		except Exception as e:
			raise e

	@realmstr.setter
	def realmstr(self, realmstr) :
		r"""Kerberos Realm.
		"""
		try :
			self._realmstr = realmstr
		except Exception as e:
			raise e

	@property
	def delegateduser(self) :
		r"""Username that can perform kerberos constrained delegation.
		"""
		try :
			return self._delegateduser
		except Exception as e:
			raise e

	@delegateduser.setter
	def delegateduser(self, delegateduser) :
		r"""Username that can perform kerberos constrained delegation.
		"""
		try :
			self._delegateduser = delegateduser
		except Exception as e:
			raise e

	@property
	def kcdpassword(self) :
		r"""Password for Delegated User.
		"""
		try :
			return self._kcdpassword
		except Exception as e:
			raise e

	@kcdpassword.setter
	def kcdpassword(self, kcdpassword) :
		r"""Password for Delegated User.
		"""
		try :
			self._kcdpassword = kcdpassword
		except Exception as e:
			raise e

	@property
	def usercert(self) :
		r"""SSL Cert (including private key) for Delegated User.
		"""
		try :
			return self._usercert
		except Exception as e:
			raise e

	@usercert.setter
	def usercert(self, usercert) :
		r"""SSL Cert (including private key) for Delegated User.
		"""
		try :
			self._usercert = usercert
		except Exception as e:
			raise e

	@property
	def cacert(self) :
		r"""CA Cert for UserCert or when doing PKINIT backchannel.
		"""
		try :
			return self._cacert
		except Exception as e:
			raise e

	@cacert.setter
	def cacert(self, cacert) :
		r"""CA Cert for UserCert or when doing PKINIT backchannel.
		"""
		try :
			self._cacert = cacert
		except Exception as e:
			raise e

	@property
	def userrealm(self) :
		r"""Realm of the user.
		"""
		try :
			return self._userrealm
		except Exception as e:
			raise e

	@userrealm.setter
	def userrealm(self, userrealm) :
		r"""Realm of the user.
		"""
		try :
			self._userrealm = userrealm
		except Exception as e:
			raise e

	@property
	def enterpriserealm(self) :
		r"""Enterprise Realm of the user. This should be given only in certain KDC deployments where KDC expects Enterprise username instead of Principal Name.
		"""
		try :
			return self._enterpriserealm
		except Exception as e:
			raise e

	@enterpriserealm.setter
	def enterpriserealm(self, enterpriserealm) :
		r"""Enterprise Realm of the user. This should be given only in certain KDC deployments where KDC expects Enterprise username instead of Principal Name.
		"""
		try :
			self._enterpriserealm = enterpriserealm
		except Exception as e:
			raise e

	@property
	def servicespn(self) :
		r"""Service SPN. When specified, this will be used to fetch kerberos tickets. If not specified, Citrix ADC will construct SPN using service fqdn.
		"""
		try :
			return self._servicespn
		except Exception as e:
			raise e

	@servicespn.setter
	def servicespn(self, servicespn) :
		r"""Service SPN. When specified, this will be used to fetch kerberos tickets. If not specified, Citrix ADC will construct SPN using service fqdn.
		"""
		try :
			self._servicespn = servicespn
		except Exception as e:
			raise e

	@property
	def principle(self) :
		r"""SPN extracted from keytab file.
		"""
		try :
			return self._principle
		except Exception as e:
			raise e

	@property
	def kcdspn(self) :
		r"""Host SPN extracted from keytab file.
		"""
		try :
			return self._kcdspn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaakcdaccount_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaakcdaccount
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.kcdaccount is not None :
				return str(self.kcdaccount)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = aaakcdaccount()
		addresource.kcdaccount = resource.kcdaccount
		addresource.keytab = resource.keytab
		addresource.realmstr = resource.realmstr
		addresource.delegateduser = resource.delegateduser
		addresource.kcdpassword = resource.kcdpassword
		addresource.usercert = resource.usercert
		addresource.cacert = resource.cacert
		addresource.userrealm = resource.userrealm
		addresource.enterpriserealm = resource.enterpriserealm
		addresource.servicespn = resource.servicespn
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ aaakcdaccount() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = aaakcdaccount()
		deleteresource.kcdaccount = resource.kcdaccount
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				deleteresource = aaakcdaccount()
				if type(resource) !=  type(deleteresource):
					deleteresource.kcdaccount = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].kcdaccount = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = aaakcdaccount()
		updateresource.kcdaccount = resource.kcdaccount
		updateresource.keytab = resource.keytab
		updateresource.realmstr = resource.realmstr
		updateresource.delegateduser = resource.delegateduser
		updateresource.kcdpassword = resource.kcdpassword
		updateresource.usercert = resource.usercert
		updateresource.cacert = resource.cacert
		updateresource.userrealm = resource.userrealm
		updateresource.enterpriserealm = resource.enterpriserealm
		updateresource.servicespn = resource.servicespn
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ aaakcdaccount() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of aaakcdaccount resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaakcdaccount()
				if type(resource) !=  type(unsetresource):
					unsetresource.kcdaccount = resource
				else :
					unsetresource.kcdaccount = resource.kcdaccount
					unsetresource.keytab = resource.keytab
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].kcdaccount = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ aaakcdaccount() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].kcdaccount = resource[i].kcdaccount
							unsetresources[i].keytab = resource[i].keytab
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def check(cls, client, resource) :
		r""" Use this API to check aaakcdaccount.
		"""
		try :
			if type(resource) is not list :
				checkresource = aaakcdaccount()
				checkresource.realmstr = resource.realmstr
				checkresource.delegateduser = resource.delegateduser
				checkresource.kcdpassword = resource.kcdpassword
				checkresource.servicespn = resource.servicespn
				checkresource.userrealm = resource.userrealm
				return checkresource.perform_operationEx(client,"check")
			else :
				if (resource and len(resource) > 0) :
					checkresources = [ aaakcdaccount() for _ in range(len(resource))]
					for i in range(len(resource)) :
						checkresources[i].realmstr = resource[i].realmstr
						checkresources[i].delegateduser = resource[i].delegateduser
						checkresources[i].kcdpassword = resource[i].kcdpassword
						checkresources[i].servicespn = resource[i].servicespn
						checkresources[i].userrealm = resource[i].userrealm
				result = cls.perform_operation_bulk_request(client, checkresources,"check")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaakcdaccount resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaakcdaccount()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = aaakcdaccount()
					obj.kcdaccount = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [aaakcdaccount() for _ in range(len(name))]
						obj = [aaakcdaccount() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = aaakcdaccount()
							obj[i].kcdaccount = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of aaakcdaccount resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaakcdaccount()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the aaakcdaccount resources configured on NetScaler.
		"""
		try :
			obj = aaakcdaccount()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of aaakcdaccount resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaakcdaccount()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class aaakcdaccount_response(base_response) :
	def __init__(self, length=1) :
		self.aaakcdaccount = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaakcdaccount = [aaakcdaccount() for _ in range(length)]

