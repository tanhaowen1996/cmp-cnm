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

class cloudngsparameter(base_resource) :
	""" Configuration for cloud ngsparameter resource. """
	def __init__(self) :
		self._blockonallowedngstktprof = None
		self._allowedudtversion = None

	@property
	def blockonallowedngstktprof(self) :
		r"""Enables blocking connections authenticated with a ticket createdby by an entity not whitelisted in allowedngstktprofile.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._blockonallowedngstktprof
		except Exception as e:
			raise e

	@blockonallowedngstktprof.setter
	def blockonallowedngstktprof(self, blockonallowedngstktprof) :
		r"""Enables blocking connections authenticated with a ticket createdby by an entity not whitelisted in allowedngstktprofile.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._blockonallowedngstktprof = blockonallowedngstktprof
		except Exception as e:
			raise e

	@property
	def allowedudtversion(self) :
		r"""Enables the required UDT version to EDT connections in the CGS deployment.<br/>Default value: V4<br/>Possible values = V4, V5, V6.
		"""
		try :
			return self._allowedudtversion
		except Exception as e:
			raise e

	@allowedudtversion.setter
	def allowedudtversion(self, allowedudtversion) :
		r"""Enables the required UDT version to EDT connections in the CGS deployment.<br/>Default value: V4<br/>Possible values = V4, V5, V6
		"""
		try :
			self._allowedudtversion = allowedudtversion
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cloudngsparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cloudngsparameter
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = cloudngsparameter()
		updateresource.blockonallowedngstktprof = resource.blockonallowedngstktprof
		updateresource.allowedudtversion = resource.allowedudtversion
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cloudngsparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of cloudngsparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cloudngsparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cloudngsparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cloudngsparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Allowedudtversion:
		V4 = "V4"
		V5 = "V5"
		V6 = "V6"

	class Blockonallowedngstktprof:
		YES = "YES"
		NO = "NO"

class cloudngsparameter_response(base_response) :
	def __init__(self, length=1) :
		self.cloudngsparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cloudngsparameter = [cloudngsparameter() for _ in range(length)]

