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

class nslicenseparameters(base_resource) :
	""" Configuration for licenseparameters resource. """
	def __init__(self) :
		self._alert1gracetimeout = None
		self._alert2gracetimeout = None

	@property
	def alert1gracetimeout(self) :
		r"""If ADC remains in grace for the configured hours then first grace alert will be raised.<br/>Default value: 6<br/>Maximum length =  24.
		"""
		try :
			return self._alert1gracetimeout
		except Exception as e:
			raise e

	@alert1gracetimeout.setter
	def alert1gracetimeout(self, alert1gracetimeout) :
		r"""If ADC remains in grace for the configured hours then first grace alert will be raised.<br/>Default value: 6<br/>Maximum length =  24
		"""
		try :
			self._alert1gracetimeout = alert1gracetimeout
		except Exception as e:
			raise e

	@property
	def alert2gracetimeout(self) :
		r"""If ADC remains in grace for the configured hours then major grace alert will be raised.<br/>Default value: 240<br/>Minimum length =  24<br/>Maximum length =  720.
		"""
		try :
			return self._alert2gracetimeout
		except Exception as e:
			raise e

	@alert2gracetimeout.setter
	def alert2gracetimeout(self, alert2gracetimeout) :
		r"""If ADC remains in grace for the configured hours then major grace alert will be raised.<br/>Default value: 240<br/>Minimum length =  24<br/>Maximum length =  720
		"""
		try :
			self._alert2gracetimeout = alert2gracetimeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslicenseparameters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslicenseparameters
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
		updateresource = nslicenseparameters()
		updateresource.alert1gracetimeout = resource.alert1gracetimeout
		updateresource.alert2gracetimeout = resource.alert2gracetimeout
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nslicenseparameters.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nslicenseparameters resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nslicenseparameters()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nslicenseparameters resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslicenseparameters()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nslicenseparameters_response(base_response) :
	def __init__(self, length=1) :
		self.nslicenseparameters = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslicenseparameters = [nslicenseparameters() for _ in range(length)]

