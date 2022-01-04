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

class botprofile_binding(base_resource):
	""" Binding class showing the resources that can be bound to botprofile_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.botprofile_tps_binding = []
		self.botprofile_ipreputation_binding = []
		self.botprofile_ratelimit_binding = []
		self.botprofile_blacklist_binding = []
		self.botprofile_kmdetectionexpr_binding = []
		self.botprofile_trapinsertionurl_binding = []
		self.botprofile_whitelist_binding = []
		self.botprofile_logexpression_binding = []
		self.botprofile_captcha_binding = []

	@property
	def name(self) :
		r"""Name of the bot management profile.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the bot management profile.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def botprofile_tps_bindings(self) :
		r"""tps that can be bound to botprofile.
		"""
		try :
			return self._botprofile_tps_binding
		except Exception as e:
			raise e

	@property
	def botprofile_blacklist_bindings(self) :
		r"""blacklist that can be bound to botprofile.
		"""
		try :
			return self._botprofile_blacklist_binding
		except Exception as e:
			raise e

	@property
	def botprofile_ipreputation_bindings(self) :
		r"""ipreputation that can be bound to botprofile.
		"""
		try :
			return self._botprofile_ipreputation_binding
		except Exception as e:
			raise e

	@property
	def botprofile_ratelimit_bindings(self) :
		r"""ratelimit that can be bound to botprofile.
		"""
		try :
			return self._botprofile_ratelimit_binding
		except Exception as e:
			raise e

	@property
	def botprofile_captcha_bindings(self) :
		r"""captcha that can be bound to botprofile.
		"""
		try :
			return self._botprofile_captcha_binding
		except Exception as e:
			raise e

	@property
	def botprofile_logexpression_bindings(self) :
		r"""logexpression that can be bound to botprofile.
		"""
		try :
			return self._botprofile_logexpression_binding
		except Exception as e:
			raise e

	@property
	def botprofile_kmdetectionexpr_bindings(self) :
		r"""kmdetectionexpr that can be bound to botprofile.
		"""
		try :
			return self._botprofile_kmdetectionexpr_binding
		except Exception as e:
			raise e

	@property
	def botprofile_whitelist_bindings(self) :
		r"""whitelist that can be bound to botprofile.
		"""
		try :
			return self._botprofile_whitelist_binding
		except Exception as e:
			raise e

	@property
	def botprofile_trapinsertionurl_bindings(self) :
		r"""trapinsertionurl that can be bound to botprofile.
		"""
		try :
			return self._botprofile_trapinsertionurl_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botprofile_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botprofile_binding
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
	def get(self, service, name="", option_="") :
		r""" Use this API to fetch botprofile_binding resource.
		"""
		try :
			if not name :
				obj = botprofile_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = botprofile_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [botprofile_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class botprofile_binding_response(base_response) :
	def __init__(self, length=1) :
		self.botprofile_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botprofile_binding = [botprofile_binding() for _ in range(length)]

