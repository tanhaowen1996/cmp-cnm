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

class botprofile_captcha_binding(base_resource) :
	""" Binding class showing the captcha that can be bound to botprofile.
	"""
	def __init__(self) :
		self._captcharesource = None
		self._bot_captcha_url = None
		self._bot_captcha_enabled = None
		self._waittime = None
		self._graceperiod = None
		self._muteperiod = None
		self._requestsizelimit = None
		self._retryattempts = None
		self._bot_captcha_action = None
		self._logmessage = None
		self._bot_bind_comment = None
		self._name = None
		self.___count = None

	@property
	def waittime(self) :
		r"""Wait time in seconds for which ADC needs to wait for the Captcha response. This is to avoid DOS attacks.<br/>Default value: 15<br/>Minimum value =  10<br/>Maximum value =  60.
		"""
		try :
			return self._waittime
		except Exception as e:
			raise e

	@waittime.setter
	def waittime(self, waittime) :
		r"""Wait time in seconds for which ADC needs to wait for the Captcha response. This is to avoid DOS attacks.<br/>Default value: 15<br/>Minimum value =  10<br/>Maximum value =  60
		"""
		try :
			self._waittime = waittime
		except Exception as e:
			raise e

	@property
	def requestsizelimit(self) :
		r"""Length of body request (in Bytes) up to (equal or less than) which captcha challenge will be provided to client. Above this length threshold the request will be dropped. This is to avoid DOS and DDOS attacks.<br/>Default value: 8000<br/>Minimum value =  10<br/>Maximum value =  30000.
		"""
		try :
			return self._requestsizelimit
		except Exception as e:
			raise e

	@requestsizelimit.setter
	def requestsizelimit(self, requestsizelimit) :
		r"""Length of body request (in Bytes) up to (equal or less than) which captcha challenge will be provided to client. Above this length threshold the request will be dropped. This is to avoid DOS and DDOS attacks.<br/>Default value: 8000<br/>Minimum value =  10<br/>Maximum value =  30000
		"""
		try :
			self._requestsizelimit = requestsizelimit
		except Exception as e:
			raise e

	@property
	def bot_captcha_enabled(self) :
		r"""Enable or disable the captcha binding.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_captcha_enabled
		except Exception as e:
			raise e

	@bot_captcha_enabled.setter
	def bot_captcha_enabled(self, bot_captcha_enabled) :
		r"""Enable or disable the captcha binding.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_captcha_enabled = bot_captcha_enabled
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
	def muteperiod(self) :
		r"""Time (in seconds) duration for which client which failed captcha need to wait until allowed to try again. The requests from this client are silently dropped during the mute period.<br/>Default value: 300<br/>Minimum value =  60<br/>Maximum value =  900.
		"""
		try :
			return self._muteperiod
		except Exception as e:
			raise e

	@muteperiod.setter
	def muteperiod(self, muteperiod) :
		r"""Time (in seconds) duration for which client which failed captcha need to wait until allowed to try again. The requests from this client are silently dropped during the mute period.<br/>Default value: 300<br/>Minimum value =  60<br/>Maximum value =  900
		"""
		try :
			self._muteperiod = muteperiod
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
	def graceperiod(self) :
		r"""Time (in seconds) duration for which no new captcha challenge is sent after current captcha challenge has been answered successfully.<br/>Default value: 900<br/>Minimum value =  60<br/>Maximum value =  900.
		"""
		try :
			return self._graceperiod
		except Exception as e:
			raise e

	@graceperiod.setter
	def graceperiod(self, graceperiod) :
		r"""Time (in seconds) duration for which no new captcha challenge is sent after current captcha challenge has been answered successfully.<br/>Default value: 900<br/>Minimum value =  60<br/>Maximum value =  900
		"""
		try :
			self._graceperiod = graceperiod
		except Exception as e:
			raise e

	@property
	def bot_captcha_url(self) :
		r"""URL for which the Captcha action, if configured under IP reputation, TPS or device fingerprint, need to be applied.<br/>Minimum length =  1.
		"""
		try :
			return self._bot_captcha_url
		except Exception as e:
			raise e

	@bot_captcha_url.setter
	def bot_captcha_url(self, bot_captcha_url) :
		r"""URL for which the Captcha action, if configured under IP reputation, TPS or device fingerprint, need to be applied.<br/>Minimum length =  1
		"""
		try :
			self._bot_captcha_url = bot_captcha_url
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
	def retryattempts(self) :
		r"""Number of times client can retry solving the captcha.<br/>Default value: 3<br/>Minimum value =  1<br/>Maximum value =  10.
		"""
		try :
			return self._retryattempts
		except Exception as e:
			raise e

	@retryattempts.setter
	def retryattempts(self, retryattempts) :
		r"""Number of times client can retry solving the captcha.<br/>Default value: 3<br/>Minimum value =  1<br/>Maximum value =  10
		"""
		try :
			self._retryattempts = retryattempts
		except Exception as e:
			raise e

	@property
	def captcharesource(self) :
		r"""Captcha action binding. For each URL, only one binding is allowed. To update the values of an existing URL binding, user has to first unbind that binding, and then needs to bind the URL again with new values. Maximum 30 bindings can be configured per profile.
		"""
		try :
			return self._captcharesource
		except Exception as e:
			raise e

	@captcharesource.setter
	def captcharesource(self, captcharesource) :
		r"""Captcha action binding. For each URL, only one binding is allowed. To update the values of an existing URL binding, user has to first unbind that binding, and then needs to bind the URL again with new values. Maximum 30 bindings can be configured per profile.
		"""
		try :
			self._captcharesource = captcharesource
		except Exception as e:
			raise e

	@property
	def bot_captcha_action(self) :
		r"""One or more actions to be taken when client fails captcha challenge. Only, log action can be configured with DROP, REDIRECT or RESET action.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET.
		"""
		try :
			return self._bot_captcha_action
		except Exception as e:
			raise e

	@bot_captcha_action.setter
	def bot_captcha_action(self, bot_captcha_action) :
		r"""One or more actions to be taken when client fails captcha challenge. Only, log action can be configured with DROP, REDIRECT or RESET action.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET
		"""
		try :
			self._bot_captcha_action = bot_captcha_action
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botprofile_captcha_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botprofile_captcha_binding
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
		addresource = botprofile_captcha_binding()
		addresource.name = resource.name
		addresource.captcharesource = resource.captcharesource
		addresource.bot_captcha_url = resource.bot_captcha_url
		addresource.waittime = resource.waittime
		addresource.graceperiod = resource.graceperiod
		addresource.muteperiod = resource.muteperiod
		addresource.requestsizelimit = resource.requestsizelimit
		addresource.retryattempts = resource.retryattempts
		addresource.bot_captcha_action = resource.bot_captcha_action
		addresource.bot_captcha_enabled = resource.bot_captcha_enabled
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
					updateresources = [botprofile_captcha_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = botprofile_captcha_binding()
		deleteresource.name = resource.name
		deleteresource.captcharesource = resource.captcharesource
		deleteresource.bot_captcha_url = resource.bot_captcha_url
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [botprofile_captcha_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch botprofile_captcha_binding resources.
		"""
		try :
			if not name :
				obj = botprofile_captcha_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = botprofile_captcha_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of botprofile_captcha_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile_captcha_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count botprofile_captcha_binding resources configued on NetScaler.
		"""
		try :
			obj = botprofile_captcha_binding()
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
		r""" Use this API to count the filtered set of botprofile_captcha_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile_captcha_binding()
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

	class Bot_rate_limit_enabled:
		ON = "ON"
		OFF = "OFF"

	class Bot_captcha_enabled:
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

	class Bot_whitelist_type:
		IPv4 = "IPv4"
		SUBNET = "SUBNET"
		EXPRESSION = "EXPRESSION"

	class Bot_captcha_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Bot_iprep_action:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"
		MITIGATION = "MITIGATION"

class botprofile_captcha_binding_response(base_response) :
	def __init__(self, length=1) :
		self.botprofile_captcha_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botprofile_captcha_binding = [botprofile_captcha_binding() for _ in range(length)]

