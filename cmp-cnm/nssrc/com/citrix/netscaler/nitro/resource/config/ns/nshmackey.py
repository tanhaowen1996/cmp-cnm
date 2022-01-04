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

class nshmackey(base_resource) :
	""" Configuration for HMAC key resource. """
	def __init__(self) :
		self._name = None
		self._digest = None
		self._keyvalue = None
		self._comment = None
		self.___count = None

	@property
	def name(self) :
		r"""Key name.  This follows the same syntax rules as other expression entity names:
		It must begin with an alpha character (A-Z or a-z) or an underscore (_).
		The rest of the characters must be alpha, numeric (0-9) or underscores.
		It cannot be re or xp (reserved for regular and XPath expressions).
		It cannot be an expression reserved word (e.g. SYS or HTTP).
		It cannot be used for an existing expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Key name.  This follows the same syntax rules as other expression entity names:
		It must begin with an alpha character (A-Z or a-z) or an underscore (_).
		The rest of the characters must be alpha, numeric (0-9) or underscores.
		It cannot be re or xp (reserved for regular and XPath expressions).
		It cannot be an expression reserved word (e.g. SYS or HTTP).
		It cannot be used for an existing expression object (HTTP callout, patset, dataset, stringmap, or named expression).<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def digest(self) :
		r"""Digest (hash) function to be used in the HMAC computation.<br/>Possible values = MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA512.
		"""
		try :
			return self._digest
		except Exception as e:
			raise e

	@digest.setter
	def digest(self, digest) :
		r"""Digest (hash) function to be used in the HMAC computation.<br/>Possible values = MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA512
		"""
		try :
			self._digest = digest
		except Exception as e:
			raise e

	@property
	def keyvalue(self) :
		r"""The hex-encoded key to be used in the HMAC computation. The key can be any length (up to a Citrix ADC-imposed maximum of 255 bytes). If the length is less than the digest block size, it will be zero padded up to the block size. If it is greater than the block size, it will be hashed using the digest function to the block size. The block size for each digest is:
		MD2    - 16 bytes
		MD4    - 16 bytes
		MD5    - 16 bytes
		SHA1   - 20 bytes
		SHA224 - 28 bytes
		SHA256 - 32 bytes
		SHA384 - 48 bytes
		SHA512 - 64 bytes
		Note that the key will be encrypted when it it is saved
		There is a special key value AUTO which generates a new random key for the specified digest. This kind of key is
		intended for use cases where the NetScaler both generates and verifies an HMAC on  the same data.
		"""
		try :
			return self._keyvalue
		except Exception as e:
			raise e

	@keyvalue.setter
	def keyvalue(self, keyvalue) :
		r"""The hex-encoded key to be used in the HMAC computation. The key can be any length (up to a Citrix ADC-imposed maximum of 255 bytes). If the length is less than the digest block size, it will be zero padded up to the block size. If it is greater than the block size, it will be hashed using the digest function to the block size. The block size for each digest is:
		MD2    - 16 bytes
		MD4    - 16 bytes
		MD5    - 16 bytes
		SHA1   - 20 bytes
		SHA224 - 28 bytes
		SHA256 - 32 bytes
		SHA384 - 48 bytes
		SHA512 - 64 bytes
		Note that the key will be encrypted when it it is saved
		There is a special key value AUTO which generates a new random key for the specified digest. This kind of key is
		intended for use cases where the NetScaler both generates and verifies an HMAC on  the same data.
		"""
		try :
			self._keyvalue = keyvalue
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Comments associated with this encryption key.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Comments associated with this encryption key.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshmackey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshmackey
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
		addresource = nshmackey()
		addresource.name = resource.name
		addresource.digest = resource.digest
		addresource.keyvalue = resource.keyvalue
		addresource.comment = resource.comment
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nshmackey.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nshmackey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = nshmackey()
		updateresource.name = resource.name
		updateresource.digest = resource.digest
		updateresource.keyvalue = resource.keyvalue
		updateresource.comment = resource.comment
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nshmackey.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nshmackey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nshmackey resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nshmackey()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshmackey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshmackey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = nshmackey()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nshmackey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nshmackey()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshmackey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshmackey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nshmackey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshmackey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nshmackey()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nshmackey() for _ in range(len(name))]
						obj = [nshmackey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nshmackey()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nshmackey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshmackey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nshmackey resources configured on NetScaler.
		"""
		try :
			obj = nshmackey()
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
		r""" Use this API to count filtered the set of nshmackey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshmackey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Digest:
		MD2 = "MD2"
		MD4 = "MD4"
		MD5 = "MD5"
		SHA1 = "SHA1"
		SHA224 = "SHA224"
		SHA256 = "SHA256"
		SHA384 = "SHA384"
		SHA512 = "SHA512"

class nshmackey_response(base_response) :
	def __init__(self, length=1) :
		self.nshmackey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshmackey = [nshmackey() for _ in range(length)]

