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

class appfwjsonerrorpage(base_resource) :
	""" Configuration for JSON error page resource. """
	def __init__(self) :
		self._name = None
		self._src = None
		self._comment = None
		self._overwrite = None
		self._response = None

	@property
	def name(self) :
		r"""Indicates name of the imported json error page to be removed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Indicates name of the imported json error page to be removed.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def src(self) :
		r"""URL (protocol, host, path, and name) for the location at which to store the imported JSON error object.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		r"""URL (protocol, host, path, and name) for the location at which to store the imported JSON error object.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments to preserve information about the JSON error object.<br/>Maximum length =  128.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments to preserve information about the JSON error object.<br/>Maximum length =  128
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def overwrite(self) :
		r"""Overwrite any existing JSON error object of the same name.
		"""
		try :
			return self._overwrite
		except Exception as e:
			raise e

	@overwrite.setter
	def overwrite(self, overwrite) :
		r"""Overwrite any existing JSON error object of the same name.
		"""
		try :
			self._overwrite = overwrite
		except Exception as e:
			raise e

	@property
	def response(self) :
		r"""JSON error object contents.
		"""
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwjsonerrorpage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwjsonerrorpage
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
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = appfwjsonerrorpage()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete appfwjsonerrorpage.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwjsonerrorpage()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		r""" Use this API to Import appfwjsonerrorpage.
		"""
		try :
			if type(resource) is not list :
				Importresource = appfwjsonerrorpage()
				Importresource.src = resource.src
				Importresource.name = resource.name
				Importresource.comment = resource.comment
				Importresource.overwrite = resource.overwrite
				return Importresource.perform_operation(client,"Import")
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		changeresource = appfwjsonerrorpage()
		changeresource.name = resource.name
		return changeresource

	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change appfwjsonerrorpage.
		"""
		try :
			if type(resource) is not list :
				changeresource = cls.filter_update_parameters(resource)
				return changeresource.perform_operation(client,"update")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwjsonerrorpage resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwjsonerrorpage()
				response = obj.get_resources(client, option_)
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = appfwjsonerrorpage()
					obj.name = name
					response = obj.get_resource(client, option_)
			return response
		except Exception as e :
			raise e


class appfwjsonerrorpage_response(base_response) :
	def __init__(self, length=1) :
		self.appfwjsonerrorpage = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwjsonerrorpage = [appfwjsonerrorpage() for _ in range(length)]

