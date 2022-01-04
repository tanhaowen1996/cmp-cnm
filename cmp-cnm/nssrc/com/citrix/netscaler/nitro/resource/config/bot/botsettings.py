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

class botsettings(base_resource) :
	""" Configuration for Bot engine settings resource. """
	def __init__(self) :
		self._defaultprofile = None
		self._javascriptname = None
		self._sessiontimeout = None
		self._sessioncookiename = None
		self._dfprequestlimit = None
		self._signatureautoupdate = None
		self._signatureurl = None
		self._proxyserver = None
		self._proxyport = None
		self._trapurlautogenerate = None
		self._trapurlinterval = None
		self._trapurllength = None
		self._builtin = None
		self._feature = None

	@property
	def defaultprofile(self) :
		r"""Profile to use when a connection does not match any policy. Default setting is " ", which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Minimum length =  1.
		"""
		try :
			return self._defaultprofile
		except Exception as e:
			raise e

	@defaultprofile.setter
	def defaultprofile(self, defaultprofile) :
		r"""Profile to use when a connection does not match any policy. Default setting is " ", which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Minimum length =  1
		"""
		try :
			self._defaultprofile = defaultprofile
		except Exception as e:
			raise e

	@property
	def javascriptname(self) :
		r"""Name of the JavaScript that the Bot Management feature  uses in response.
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1.
		"""
		try :
			return self._javascriptname
		except Exception as e:
			raise e

	@javascriptname.setter
	def javascriptname(self, javascriptname) :
		r"""Name of the JavaScript that the Bot Management feature  uses in response.
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1
		"""
		try :
			self._javascriptname = javascriptname
		except Exception as e:
			raise e

	@property
	def sessiontimeout(self) :
		r"""Timeout, in seconds, after which a user session is terminated.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._sessiontimeout
		except Exception as e:
			raise e

	@sessiontimeout.setter
	def sessiontimeout(self, sessiontimeout) :
		r"""Timeout, in seconds, after which a user session is terminated.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._sessiontimeout = sessiontimeout
		except Exception as e:
			raise e

	@property
	def sessioncookiename(self) :
		r"""Name of the SessionCookie that the Bot Management feature uses for tracking.
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1.
		"""
		try :
			return self._sessioncookiename
		except Exception as e:
			raise e

	@sessioncookiename.setter
	def sessioncookiename(self, sessioncookiename) :
		r"""Name of the SessionCookie that the Bot Management feature uses for tracking.
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1
		"""
		try :
			self._sessioncookiename = sessioncookiename
		except Exception as e:
			raise e

	@property
	def dfprequestlimit(self) :
		r"""Number of requests to allow without bot session cookie if device fingerprint is enabled.<br/>Minimum length =  1.
		"""
		try :
			return self._dfprequestlimit
		except Exception as e:
			raise e

	@dfprequestlimit.setter
	def dfprequestlimit(self, dfprequestlimit) :
		r"""Number of requests to allow without bot session cookie if device fingerprint is enabled.<br/>Minimum length =  1
		"""
		try :
			self._dfprequestlimit = dfprequestlimit
		except Exception as e:
			raise e

	@property
	def signatureautoupdate(self) :
		r"""Flag used to enable/disable bot auto update signatures.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._signatureautoupdate
		except Exception as e:
			raise e

	@signatureautoupdate.setter
	def signatureautoupdate(self, signatureautoupdate) :
		r"""Flag used to enable/disable bot auto update signatures.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._signatureautoupdate = signatureautoupdate
		except Exception as e:
			raise e

	@property
	def signatureurl(self) :
		r"""URL to download the bot signature mapping file from server.<br/>Default value: https://nsbotsignatures.s3.amazonaws.com/BotSignatureMapping.json.
		"""
		try :
			return self._signatureurl
		except Exception as e:
			raise e

	@signatureurl.setter
	def signatureurl(self, signatureurl) :
		r"""URL to download the bot signature mapping file from server.<br/>Default value: https://nsbotsignatures.s3.amazonaws.com/BotSignatureMapping.json
		"""
		try :
			self._signatureurl = signatureurl
		except Exception as e:
			raise e

	@property
	def proxyserver(self) :
		r"""Proxy Server IP to get updated signatures from AWS.
		"""
		try :
			return self._proxyserver
		except Exception as e:
			raise e

	@proxyserver.setter
	def proxyserver(self, proxyserver) :
		r"""Proxy Server IP to get updated signatures from AWS.
		"""
		try :
			self._proxyserver = proxyserver
		except Exception as e:
			raise e

	@property
	def proxyport(self) :
		r"""Proxy Server Port to get updated signatures from AWS.<br/>Default value: 8080<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._proxyport
		except Exception as e:
			raise e

	@proxyport.setter
	def proxyport(self, proxyport) :
		r"""Proxy Server Port to get updated signatures from AWS.<br/>Default value: 8080<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._proxyport = proxyport
		except Exception as e:
			raise e

	@property
	def trapurlautogenerate(self) :
		r"""Enable/disable trap URL auto generation. When enabled, trap URL is updated within the configured interval.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._trapurlautogenerate
		except Exception as e:
			raise e

	@trapurlautogenerate.setter
	def trapurlautogenerate(self, trapurlautogenerate) :
		r"""Enable/disable trap URL auto generation. When enabled, trap URL is updated within the configured interval.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._trapurlautogenerate = trapurlautogenerate
		except Exception as e:
			raise e

	@property
	def trapurlinterval(self) :
		r"""Time in seconds after which trap URL is updated.<br/>Default value: 3600<br/>Minimum length =  300<br/>Maximum length =  86400.
		"""
		try :
			return self._trapurlinterval
		except Exception as e:
			raise e

	@trapurlinterval.setter
	def trapurlinterval(self, trapurlinterval) :
		r"""Time in seconds after which trap URL is updated.<br/>Default value: 3600<br/>Minimum length =  300<br/>Maximum length =  86400
		"""
		try :
			self._trapurlinterval = trapurlinterval
		except Exception as e:
			raise e

	@property
	def trapurllength(self) :
		r"""Length of the auto-generated trap URL.<br/>Default value: 32<br/>Minimum length =  10<br/>Maximum length =  255.
		"""
		try :
			return self._trapurllength
		except Exception as e:
			raise e

	@trapurllength.setter
	def trapurllength(self, trapurllength) :
		r"""Length of the auto-generated trap URL.<br/>Default value: 32<br/>Minimum length =  10<br/>Maximum length =  255
		"""
		try :
			self._trapurllength = trapurllength
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if bot engine setting is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(botsettings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botsettings
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
		updateresource = botsettings()
		updateresource.defaultprofile = resource.defaultprofile
		updateresource.javascriptname = resource.javascriptname
		updateresource.sessiontimeout = resource.sessiontimeout
		updateresource.sessioncookiename = resource.sessioncookiename
		updateresource.dfprequestlimit = resource.dfprequestlimit
		updateresource.signatureautoupdate = resource.signatureautoupdate
		updateresource.signatureurl = resource.signatureurl
		updateresource.proxyserver = resource.proxyserver
		updateresource.proxyport = resource.proxyport
		updateresource.trapurlautogenerate = resource.trapurlautogenerate
		updateresource.trapurlinterval = resource.trapurlinterval
		updateresource.trapurllength = resource.trapurllength
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update botsettings.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of botsettings resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = botsettings()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the botsettings resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = botsettings()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


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

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Trapurlautogenerate:
		ON = "ON"
		OFF = "OFF"

	class Signatureautoupdate:
		ON = "ON"
		OFF = "OFF"

class botsettings_response(base_response) :
	def __init__(self, length=1) :
		self.botsettings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botsettings = [botsettings() for _ in range(length)]

