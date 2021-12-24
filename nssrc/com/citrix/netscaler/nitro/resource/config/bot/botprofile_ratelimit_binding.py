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

class botprofile_ratelimit_binding(base_resource) :
	""" Binding class showing the ratelimit that can be bound to botprofile.
	"""
	def __init__(self) :
		self._bot_ratelimit = None
		self._bot_rate_limit_type = None
		self._bot_rate_limit_enabled = None
		self._bot_rate_limit_url = None
		self._cookiename = None
		self._rate = None
		self._timeslice = None
		self._bot_rate_limit_action = None
		self._logmessage = None
		self._bot_bind_comment = None
		self._name = None
		self.___count = None

	@property
	def timeslice(self) :
		r"""Time interval during which requests are tracked to check if they cross the given rate.<br/>Default value: 1000<br/>Minimum value =  10.
		"""
		try :
			return self._timeslice
		except Exception as e:
			raise e

	@timeslice.setter
	def timeslice(self, timeslice) :
		r"""Time interval during which requests are tracked to check if they cross the given rate.<br/>Default value: 1000<br/>Minimum value =  10
		"""
		try :
			self._timeslice = timeslice
		except Exception as e:
			raise e

	@property
	def rate(self) :
		r"""Maximum number of requests that are allowed in this session in the given period time.<br/>Default value: 1<br/>Minimum value =  1.
		"""
		try :
			return self._rate
		except Exception as e:
			raise e

	@rate.setter
	def rate(self, rate) :
		r"""Maximum number of requests that are allowed in this session in the given period time.<br/>Default value: 1<br/>Minimum value =  1
		"""
		try :
			self._rate = rate
		except Exception as e:
			raise e

	@property
	def cookiename(self) :
		r"""Cookie name which is used to identify the session for session rate-limiting.
		"""
		try :
			return self._cookiename
		except Exception as e:
			raise e

	@cookiename.setter
	def cookiename(self, cookiename) :
		r"""Cookie name which is used to identify the session for session rate-limiting.
		"""
		try :
			self._cookiename = cookiename
		except Exception as e:
			raise e

	@property
	def bot_rate_limit_enabled(self) :
		r"""Enable or disable rate-limit binding.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_rate_limit_enabled
		except Exception as e:
			raise e

	@bot_rate_limit_enabled.setter
	def bot_rate_limit_enabled(self, bot_rate_limit_enabled) :
		r"""Enable or disable rate-limit binding.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_rate_limit_enabled = bot_rate_limit_enabled
		except Exception as e:
			raise e

	@property
	def bot_rate_limit_type(self) :
		r"""Rate-limiting type Following rate-limiting types are allowed:
		*SOURCE_IP - Rate-limiting based on the client IP.
		*SESSION - Rate-limiting based on the configured cookie name.
		*URL - Rate-limiting based on the configured URL.<br/>Possible values = SESSION, SOURCE_IP, URL.
		"""
		try :
			return self._bot_rate_limit_type
		except Exception as e:
			raise e

	@bot_rate_limit_type.setter
	def bot_rate_limit_type(self, bot_rate_limit_type) :
		r"""Rate-limiting type Following rate-limiting types are allowed:
		*SOURCE_IP - Rate-limiting based on the client IP.
		*SESSION - Rate-limiting based on the configured cookie name.
		*URL - Rate-limiting based on the configured URL.<br/>Possible values = SESSION, SOURCE_IP, URL
		"""
		try :
			self._bot_rate_limit_type = bot_rate_limit_type
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name for the profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters. Cannot be changed after the profile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the profile. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters. Cannot be changed after the profile is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my profile" or 'my profile').<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def bot_rate_limit_action(self) :
		r"""One or more actions to be taken when the current rate becomes more than the configured rate. Only LOG action can be combined with DROP, REDIRECT or RESET action.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET.
		"""
		try :
			return self._bot_rate_limit_action
		except Exception as e:
			raise e

	@bot_rate_limit_action.setter
	def bot_rate_limit_action(self, bot_rate_limit_action) :
		r"""One or more actions to be taken when the current rate becomes more than the configured rate. Only LOG action can be combined with DROP, REDIRECT or RESET action.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET
		"""
		try :
			self._bot_rate_limit_action = bot_rate_limit_action
		except Exception as e:
			raise e

	@property
	def bot_bind_comment(self) :
		r"""Any comments about this binding.<br/>Minimum length =  1.
		"""
		try :
			return self._bot_bind_comment
		except Exception as e:
			raise e

	@bot_bind_comment.setter
	def bot_bind_comment(self, bot_bind_comment) :
		r"""Any comments about this binding.<br/>Minimum length =  1
		"""
		try :
			self._bot_bind_comment = bot_bind_comment
		except Exception as e:
			raise e

	@property
	def bot_ratelimit(self) :
		r"""Rate-limit binding. Maximum 30 bindings can be configured per profile for rate-limit detection. For SOURCE_IP type, only one binding can be configured, and for URL type, only one binding is allowed per URL, and for SESSION type, only one binding is allowed for a cookie name. To update the values of an existing binding, user has to first unbind that binding, and then needs to bind again with new values.
		"""
		try :
			return self._bot_ratelimit
		except Exception as e:
			raise e

	@bot_ratelimit.setter
	def bot_ratelimit(self, bot_ratelimit) :
		r"""Rate-limit binding. Maximum 30 bindings can be configured per profile for rate-limit detection. For SOURCE_IP type, only one binding can be configured, and for URL type, only one binding is allowed per URL, and for SESSION type, only one binding is allowed for a cookie name. To update the values of an existing binding, user has to first unbind that binding, and then needs to bind again with new values.
		"""
		try :
			self._bot_ratelimit = bot_ratelimit
		except Exception as e:
			raise e

	@property
	def logmessage(self) :
		r"""Message to be logged for this binding.<br/>Minimum length =  1.
		"""
		try :
			return self._logmessage
		except Exception as e:
			raise e

	@logmessage.setter
	def logmessage(self, logmessage) :
		r"""Message to be logged for this binding.<br/>Minimum length =  1
		"""
		try :
			self._logmessage = logmessage
		except Exception as e:
			raise e

	@property
	def bot_rate_limit_url(self) :
		r"""URL for the resource based rate-limiting.
		"""
		try :
			return self._bot_rate_limit_url
		except Exception as e:
			raise e

	@bot_rate_limit_url.setter
	def bot_rate_limit_url(self, bot_rate_limit_url) :
		r"""URL for the resource based rate-limiting.
		"""
		try :
			self._bot_rate_limit_url = bot_rate_limit_url
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botprofile_ratelimit_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botprofile_ratelimit_binding
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
		addresource = botprofile_ratelimit_binding()
		addresource.name = resource.name
		addresource.bot_ratelimit = resource.bot_ratelimit
		addresource.bot_rate_limit_type = resource.bot_rate_limit_type
		addresource.bot_rate_limit_url = resource.bot_rate_limit_url
		addresource.cookiename = resource.cookiename
		addresource.rate = resource.rate
		addresource.timeslice = resource.timeslice
		addresource.bot_rate_limit_action = resource.bot_rate_limit_action
		addresource.bot_rate_limit_enabled = resource.bot_rate_limit_enabled
		addresource.logmessage = resource.logmessage
		addresource.bot_bind_comment = resource.bot_bind_comment
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [botprofile_ratelimit_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = botprofile_ratelimit_binding()
		deleteresource.name = resource.name
		deleteresource.bot_ratelimit = resource.bot_ratelimit
		deleteresource.bot_rate_limit_type = resource.bot_rate_limit_type
		deleteresource.bot_rate_limit_url = resource.bot_rate_limit_url
		deleteresource.cookiename = resource.cookiename
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [botprofile_ratelimit_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch botprofile_ratelimit_binding resources.
		"""
		try :
			if not name :
				obj = botprofile_ratelimit_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = botprofile_ratelimit_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of botprofile_ratelimit_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile_ratelimit_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count botprofile_ratelimit_binding resources configued on NetScaler.
		"""
		try :
			obj = botprofile_ratelimit_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of botprofile_ratelimit_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile_ratelimit_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Bot_blacklist_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		RESET = "RESET"
		REDIRECT = "REDIRECT"

	class Bot_tps_type:
		SOURCE_IP = "SOURCE_IP"
		GEOLOCATION = "GEOLOCATION"
		REQUEST_URL = "REQUEST_URL"
		Host = "Host"

	class Category:
		IP = "IP"
		BOTNETS = "BOTNETS"
		SPAM_SOURCES = "SPAM_SOURCES"
		SCANNERS = "SCANNERS"
		DOS = "DOS"
		REPUTATION = "REPUTATION"
		PHISHING = "PHISHING"
		PROXY = "PROXY"
		NETWORK = "NETWORK"
		MOBILE_THREATS = "MOBILE_THREATS"

	class Bot_iprep_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_captcha_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_rate_limit_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_tps_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"
		MITIGATION = "MITIGATION"

	class Bot_rate_limit_type:
		SESSION = "SESSION"
		SOURCE_IP = "SOURCE_IP"
		URL = "URL"

	class Bot_whitelist_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_rate_limit_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Bot_log_expression_enabled:
		ON = "ON"
		OFF = "OFF"

	class Log:
		ON = "ON"
		OFF = "OFF"

	class Bot_blacklist_type:
		IPv4 = "IPv4"
		SUBNET = "SUBNET"
		EXPRESSION = "EXPRESSION"

	class Bot_blacklist_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_trap_url_insertion_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_km_detection_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_captcha_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Bot_whitelist_type:
		IPv4 = "IPv4"
		SUBNET = "SUBNET"
		EXPRESSION = "EXPRESSION"

	class Bot_iprep_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"
		MITIGATION = "MITIGATION"

class botprofile_ratelimit_binding_response(base_response) :
	def __init__(self, length=1) :
		self.botprofile_ratelimit_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botprofile_ratelimit_binding = [botprofile_ratelimit_binding() for _ in range(length)]

