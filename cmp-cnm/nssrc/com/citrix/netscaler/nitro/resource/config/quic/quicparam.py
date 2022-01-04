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

class quicparam(base_resource) :
	""" Configuration for Citrix ADC QUIC parameters resource. """
	def __init__(self) :
		self._quicsecrettimeout = None

	@property
	def quicsecrettimeout(self) :
		r"""Rotation frequency, in seconds, for the secret used to generate address validation tokens that will be issued in QUIC Retry packets and QUIC NEW_TOKEN frames sent by the Citrix ADC. A value of 0 can be configured if secret rotation is not desired.<br/>Default value: 3600<br/>Maximum length =  31536000.
		"""
		try :
			return self._quicsecrettimeout
		except Exception as e:
			raise e

	@quicsecrettimeout.setter
	def quicsecrettimeout(self, quicsecrettimeout) :
		r"""Rotation frequency, in seconds, for the secret used to generate address validation tokens that will be issued in QUIC Retry packets and QUIC NEW_TOKEN frames sent by the Citrix ADC. A value of 0 can be configured if secret rotation is not desired.<br/>Default value: 3600<br/>Maximum length =  31536000
		"""
		try :
			self._quicsecrettimeout = quicsecrettimeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(quicparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.quicparam
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
		updateresource = quicparam()
		updateresource.quicsecrettimeout = resource.quicsecrettimeout
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update quicparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of quicparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = quicparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the quicparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = quicparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class quicparam_response(base_response) :
	def __init__(self, length=1) :
		self.quicparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.quicparam = [quicparam() for _ in range(length)]

