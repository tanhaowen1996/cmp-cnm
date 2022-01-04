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

class botprofile(base_resource) :
	""" Configuration for Bot profile resource. """
	def __init__(self) :
		self._name = None
		self._signature = None
		self._errorurl = None
		self._trapurl = None
		self._comment = None
		self._bot_enable_white_list = None
		self._bot_enable_black_list = None
		self._bot_enable_rate_limit = None
		self._devicefingerprint = None
		self._devicefingerprintaction = None
		self._bot_enable_ip_reputation = None
		self._trap = None
		self._trapaction = None
		self._signaturenouseragentheaderaction = None
		self._signaturemultipleuseragentheaderaction = None
		self._bot_enable_tps = None
		self._devicefingerprintmobile = None
		self._clientipexpression = None
		self._kmjavascriptname = None
		self._kmdetection = None
		self._kmeventspostbodylimit = None
		self._builtin = None
		self._feature = None
		self.___count = None

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
	def signature(self) :
		r"""Name of object containing bot static signature details.<br/>Minimum length =  1.
		"""
		try :
			return self._signature
		except Exception as e:
			raise e

	@signature.setter
	def signature(self, signature) :
		r"""Name of object containing bot static signature details.<br/>Minimum length =  1
		"""
		try :
			self._signature = signature
		except Exception as e:
			raise e

	@property
	def errorurl(self) :
		r"""URL that Bot protection uses as the Error URL.<br/>Minimum length =  1.
		"""
		try :
			return self._errorurl
		except Exception as e:
			raise e

	@errorurl.setter
	def errorurl(self, errorurl) :
		r"""URL that Bot protection uses as the Error URL.<br/>Minimum length =  1
		"""
		try :
			self._errorurl = errorurl
		except Exception as e:
			raise e

	@property
	def trapurl(self) :
		r"""URL that Bot protection uses as the Trap URL.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._trapurl
		except Exception as e:
			raise e

	@trapurl.setter
	def trapurl(self, trapurl) :
		r"""URL that Bot protection uses as the Trap URL.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._trapurl = trapurl
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.<br/>Minimum length =  1.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.<br/>Minimum length =  1
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def bot_enable_white_list(self) :
		r"""Enable white-list bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_enable_white_list
		except Exception as e:
			raise e

	@bot_enable_white_list.setter
	def bot_enable_white_list(self, bot_enable_white_list) :
		r"""Enable white-list bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_enable_white_list = bot_enable_white_list
		except Exception as e:
			raise e

	@property
	def bot_enable_black_list(self) :
		r"""Enable black-list bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_enable_black_list
		except Exception as e:
			raise e

	@bot_enable_black_list.setter
	def bot_enable_black_list(self, bot_enable_black_list) :
		r"""Enable black-list bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_enable_black_list = bot_enable_black_list
		except Exception as e:
			raise e

	@property
	def bot_enable_rate_limit(self) :
		r"""Enable rate-limit bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_enable_rate_limit
		except Exception as e:
			raise e

	@bot_enable_rate_limit.setter
	def bot_enable_rate_limit(self, bot_enable_rate_limit) :
		r"""Enable rate-limit bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_enable_rate_limit = bot_enable_rate_limit
		except Exception as e:
			raise e

	@property
	def devicefingerprint(self) :
		r"""Enable device-fingerprint bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._devicefingerprint
		except Exception as e:
			raise e

	@devicefingerprint.setter
	def devicefingerprint(self, devicefingerprint) :
		r"""Enable device-fingerprint bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._devicefingerprint = devicefingerprint
		except Exception as e:
			raise e

	@property
	def devicefingerprintaction(self) :
		r"""Action to be taken for device-fingerprint based bot detection.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET, MITIGATION.
		"""
		try :
			return self._devicefingerprintaction
		except Exception as e:
			raise e

	@devicefingerprintaction.setter
	def devicefingerprintaction(self, devicefingerprintaction) :
		r"""Action to be taken for device-fingerprint based bot detection.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET, MITIGATION
		"""
		try :
			self._devicefingerprintaction = devicefingerprintaction
		except Exception as e:
			raise e

	@property
	def bot_enable_ip_reputation(self) :
		r"""Enable IP-reputation bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_enable_ip_reputation
		except Exception as e:
			raise e

	@bot_enable_ip_reputation.setter
	def bot_enable_ip_reputation(self, bot_enable_ip_reputation) :
		r"""Enable IP-reputation bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_enable_ip_reputation = bot_enable_ip_reputation
		except Exception as e:
			raise e

	@property
	def trap(self) :
		r"""Enable trap bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trap
		except Exception as e:
			raise e

	@trap.setter
	def trap(self, trap) :
		r"""Enable trap bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trap = trap
		except Exception as e:
			raise e

	@property
	def trapaction(self) :
		r"""Action to be taken for bot trap based bot detection.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET.
		"""
		try :
			return self._trapaction
		except Exception as e:
			raise e

	@trapaction.setter
	def trapaction(self, trapaction) :
		r"""Action to be taken for bot trap based bot detection.<br/>Default value: NONE<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET
		"""
		try :
			self._trapaction = trapaction
		except Exception as e:
			raise e

	@property
	def signaturenouseragentheaderaction(self) :
		r"""Actions to be taken if no User-Agent header in the request (Applicable if Signature check is enabled).<br/>Default value: DROP<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET.
		"""
		try :
			return self._signaturenouseragentheaderaction
		except Exception as e:
			raise e

	@signaturenouseragentheaderaction.setter
	def signaturenouseragentheaderaction(self, signaturenouseragentheaderaction) :
		r"""Actions to be taken if no User-Agent header in the request (Applicable if Signature check is enabled).<br/>Default value: DROP<br/>Possible values = NONE, LOG, DROP, REDIRECT, RESET
		"""
		try :
			self._signaturenouseragentheaderaction = signaturenouseragentheaderaction
		except Exception as e:
			raise e

	@property
	def signaturemultipleuseragentheaderaction(self) :
		r"""Actions to be taken if multiple User-Agent headers are seen in a request (Applicable if Signature check is enabled). Log action should be combined with other actions.<br/>Default value: CHECKLAST<br/>Possible values = CHECKLAST, LOG, DROP, REDIRECT, RESET.
		"""
		try :
			return self._signaturemultipleuseragentheaderaction
		except Exception as e:
			raise e

	@signaturemultipleuseragentheaderaction.setter
	def signaturemultipleuseragentheaderaction(self, signaturemultipleuseragentheaderaction) :
		r"""Actions to be taken if multiple User-Agent headers are seen in a request (Applicable if Signature check is enabled). Log action should be combined with other actions.<br/>Default value: CHECKLAST<br/>Possible values = CHECKLAST, LOG, DROP, REDIRECT, RESET
		"""
		try :
			self._signaturemultipleuseragentheaderaction = signaturemultipleuseragentheaderaction
		except Exception as e:
			raise e

	@property
	def bot_enable_tps(self) :
		r"""Enable TPS.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._bot_enable_tps
		except Exception as e:
			raise e

	@bot_enable_tps.setter
	def bot_enable_tps(self, bot_enable_tps) :
		r"""Enable TPS.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._bot_enable_tps = bot_enable_tps
		except Exception as e:
			raise e

	@property
	def devicefingerprintmobile(self) :
		r"""Enabling bot device fingerprint protection for mobile clients.<br/>Default value: NONE<br/>Possible values = NONE, Android.
		"""
		try :
			return self._devicefingerprintmobile
		except Exception as e:
			raise e

	@devicefingerprintmobile.setter
	def devicefingerprintmobile(self, devicefingerprintmobile) :
		r"""Enabling bot device fingerprint protection for mobile clients.<br/>Default value: NONE<br/>Possible values = NONE, Android
		"""
		try :
			self._devicefingerprintmobile = devicefingerprintmobile
		except Exception as e:
			raise e

	@property
	def clientipexpression(self) :
		r"""Expression to get the client IP.
		"""
		try :
			return self._clientipexpression
		except Exception as e:
			raise e

	@clientipexpression.setter
	def clientipexpression(self, clientipexpression) :
		r"""Expression to get the client IP.
		"""
		try :
			self._clientipexpression = clientipexpression
		except Exception as e:
			raise e

	@property
	def kmjavascriptname(self) :
		r"""Name of the JavaScript file that the Bot Management feature will insert in the response for keyboard-mouse based detection.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my javascript file name" or 'my javascript file name').
		"""
		try :
			return self._kmjavascriptname
		except Exception as e:
			raise e

	@kmjavascriptname.setter
	def kmjavascriptname(self, kmjavascriptname) :
		r"""Name of the JavaScript file that the Bot Management feature will insert in the response for keyboard-mouse based detection.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my javascript file name" or 'my javascript file name').
		"""
		try :
			self._kmjavascriptname = kmjavascriptname
		except Exception as e:
			raise e

	@property
	def kmdetection(self) :
		r"""Enable keyboard-mouse based bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._kmdetection
		except Exception as e:
			raise e

	@kmdetection.setter
	def kmdetection(self, kmdetection) :
		r"""Enable keyboard-mouse based bot detection.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._kmdetection = kmdetection
		except Exception as e:
			raise e

	@property
	def kmeventspostbodylimit(self) :
		r"""Size of the KM data send by the browser, needs to be processed on ADC.<br/>Minimum length =  1<br/>Maximum length =  204800.
		"""
		try :
			return self._kmeventspostbodylimit
		except Exception as e:
			raise e

	@kmeventspostbodylimit.setter
	def kmeventspostbodylimit(self, kmeventspostbodylimit) :
		r"""Size of the KM data send by the browser, needs to be processed on ADC.<br/>Minimum length =  1<br/>Maximum length =  204800
		"""
		try :
			self._kmeventspostbodylimit = kmeventspostbodylimit
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if bot profille is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botprofile
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
		addresource = botprofile()
		addresource.name = resource.name
		addresource.signature = resource.signature
		addresource.errorurl = resource.errorurl
		addresource.trapurl = resource.trapurl
		addresource.comment = resource.comment
		addresource.bot_enable_white_list = resource.bot_enable_white_list
		addresource.bot_enable_black_list = resource.bot_enable_black_list
		addresource.bot_enable_rate_limit = resource.bot_enable_rate_limit
		addresource.devicefingerprint = resource.devicefingerprint
		addresource.devicefingerprintaction = resource.devicefingerprintaction
		addresource.bot_enable_ip_reputation = resource.bot_enable_ip_reputation
		addresource.trap = resource.trap
		addresource.trapaction = resource.trapaction
		addresource.signaturenouseragentheaderaction = resource.signaturenouseragentheaderaction
		addresource.signaturemultipleuseragentheaderaction = resource.signaturemultipleuseragentheaderaction
		addresource.bot_enable_tps = resource.bot_enable_tps
		addresource.devicefingerprintmobile = resource.devicefingerprintmobile
		addresource.clientipexpression = resource.clientipexpression
		addresource.kmjavascriptname = resource.kmjavascriptname
		addresource.kmdetection = resource.kmdetection
		addresource.kmeventspostbodylimit = resource.kmeventspostbodylimit
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add botprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ botprofile() for _ in range(len(resource))]
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
		updateresource = botprofile()
		updateresource.name = resource.name
		updateresource.signature = resource.signature
		updateresource.errorurl = resource.errorurl
		updateresource.trapurl = resource.trapurl
		updateresource.comment = resource.comment
		updateresource.bot_enable_white_list = resource.bot_enable_white_list
		updateresource.bot_enable_black_list = resource.bot_enable_black_list
		updateresource.bot_enable_rate_limit = resource.bot_enable_rate_limit
		updateresource.devicefingerprint = resource.devicefingerprint
		updateresource.devicefingerprintaction = resource.devicefingerprintaction
		updateresource.bot_enable_ip_reputation = resource.bot_enable_ip_reputation
		updateresource.trap = resource.trap
		updateresource.signaturenouseragentheaderaction = resource.signaturenouseragentheaderaction
		updateresource.signaturemultipleuseragentheaderaction = resource.signaturemultipleuseragentheaderaction
		updateresource.trapaction = resource.trapaction
		updateresource.bot_enable_tps = resource.bot_enable_tps
		updateresource.devicefingerprintmobile = resource.devicefingerprintmobile
		updateresource.clientipexpression = resource.clientipexpression
		updateresource.kmjavascriptname = resource.kmjavascriptname
		updateresource.kmdetection = resource.kmdetection
		updateresource.kmeventspostbodylimit = resource.kmeventspostbodylimit
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update botprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ botprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of botprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = botprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ botprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ botprofile() for _ in range(len(resource))]
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
		deleteresource = botprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete botprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = botprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ botprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ botprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the botprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = botprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = botprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [botprofile() for _ in range(len(name))]
						obj = [botprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = botprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of botprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the botprofile resources configured on NetScaler.
		"""
		try :
			obj = botprofile()
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
		r""" Use this API to count filtered the set of botprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = botprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Trapaction:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Trap:
		ON = "ON"
		OFF = "OFF"

	class Kmdetection:
		ON = "ON"
		OFF = "OFF"

	class Signaturenouseragentheaderaction:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Bot_enable_tps:
		ON = "ON"
		OFF = "OFF"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"
		APIGateway = "APIGateway"

	class Devicefingerprintaction:
		NONE = "NONE"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"
		MITIGATION = "MITIGATION"

	class Devicefingerprintmobile:
		NONE = "NONE"
		Android = "Android"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Bot_enable_rate_limit:
		ON = "ON"
		OFF = "OFF"

	class Bot_enable_black_list:
		ON = "ON"
		OFF = "OFF"

	class Bot_enable_white_list:
		ON = "ON"
		OFF = "OFF"

	class Devicefingerprint:
		ON = "ON"
		OFF = "OFF"

	class Signaturemultipleuseragentheaderaction:
		CHECKLAST = "CHECKLAST"
		LOG = "LOG"
		DROP = "DROP"
		REDIRECT = "REDIRECT"
		RESET = "RESET"

	class Bot_enable_ip_reputation:
		ON = "ON"
		OFF = "OFF"

class botprofile_response(base_response) :
	def __init__(self, length=1) :
		self.botprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botprofile = [botprofile() for _ in range(length)]

