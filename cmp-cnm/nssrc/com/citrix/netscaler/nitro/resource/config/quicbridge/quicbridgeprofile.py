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

class quicbridgeprofile(base_resource) :
	""" Configuration for QUIC BRIDGE profile resource. """
	def __init__(self) :
		self._name = None
		self._routingalgorithm = None
		self._serveridlength = None
		self._refcnt = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the QUIC profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the QUIC profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def routingalgorithm(self) :
		r"""Routing algorithm to generate routable connection IDs.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT.
		"""
		try :
			return self._routingalgorithm
		except Exception as e:
			raise e

	@routingalgorithm.setter
	def routingalgorithm(self, routingalgorithm) :
		r"""Routing algorithm to generate routable connection IDs.<br/>Default value: PLAINTEXT<br/>Possible values = PLAINTEXT
		"""
		try :
			self._routingalgorithm = routingalgorithm
		except Exception as e:
			raise e

	@property
	def serveridlength(self) :
		r"""Length of serverid to encode/decode server information.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  38.
		"""
		try :
			return self._serveridlength
		except Exception as e:
			raise e

	@serveridlength.setter
	def serveridlength(self, serveridlength) :
		r"""Length of serverid to encode/decode server information.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  38
		"""
		try :
			self._serveridlength = serveridlength
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(quicbridgeprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.quicbridgeprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = quicbridgeprofile()
		addresource.name = resource.name
		addresource.routingalgorithm = resource.routingalgorithm
		addresource.serveridlength = resource.serveridlength
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add quicbridgeprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ quicbridgeprofile() for _ in range(len(resource))]
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
		deleteresource = quicbridgeprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete quicbridgeprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = quicbridgeprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ quicbridgeprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ quicbridgeprofile() for _ in range(len(resource))]
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
		updateresource = quicbridgeprofile()
		updateresource.name = resource.name
		updateresource.routingalgorithm = resource.routingalgorithm
		updateresource.serveridlength = resource.serveridlength
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update quicbridgeprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ quicbridgeprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of quicbridgeprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = quicbridgeprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ quicbridgeprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ quicbridgeprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the quicbridgeprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = quicbridgeprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = quicbridgeprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [quicbridgeprofile() for _ in range(len(name))]
						obj = [quicbridgeprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = quicbridgeprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of quicbridgeprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = quicbridgeprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the quicbridgeprofile resources configured on NetScaler.
		"""
		try :
			obj = quicbridgeprofile()
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
		r""" Use this API to count filtered the set of quicbridgeprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = quicbridgeprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Routingalgorithm:
		PLAINTEXT = "PLAINTEXT"

class quicbridgeprofile_response(base_response) :
	def __init__(self, length=1) :
		self.quicbridgeprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.quicbridgeprofile = [quicbridgeprofile() for _ in range(length)]

