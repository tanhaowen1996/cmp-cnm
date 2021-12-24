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

class gslbparameter(base_resource) :
	""" Configuration for GSLB parameter resource. """
	def __init__(self) :
		self._ldnsentrytimeout = None
		self._rtttolerance = None
		self._ldnsmask = None
		self._v6ldnsmasklen = None
		self._ldnsprobeorder = None
		self._dropldnsreq = None
		self._gslbsvcstatedelaytime = None
		self._svcstatelearningtime = None
		self._automaticconfigsync = None
		self._mepkeepalivetimeout = None
		self._gslbsyncinterval = None
		self._gslbsyncmode = None
		self._gslbsynclocfiles = None
		self._gslbconfigsyncmonitor = None
		self._flags = None
		self._builtin = None
		self._feature = None
		self._incarnation = None

	@property
	def ldnsentrytimeout(self) :
		r"""Time, in seconds, after which an inactive LDNS entry is removed.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  65534.
		"""
		try :
			return self._ldnsentrytimeout
		except Exception as e:
			raise e

	@ldnsentrytimeout.setter
	def ldnsentrytimeout(self, ldnsentrytimeout) :
		r"""Time, in seconds, after which an inactive LDNS entry is removed.<br/>Default value: 180<br/>Minimum length =  30<br/>Maximum length =  65534
		"""
		try :
			self._ldnsentrytimeout = ldnsentrytimeout
		except Exception as e:
			raise e

	@property
	def rtttolerance(self) :
		r"""Tolerance, in milliseconds, for newly learned round-trip time (RTT) values. If the difference between the old RTT value and the newly computed RTT value is less than or equal to the specified tolerance value, the LDNS entry in the network metric table is not updated with the new RTT value. Prevents the exchange of metrics when variations in RTT values are negligible.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._rtttolerance
		except Exception as e:
			raise e

	@rtttolerance.setter
	def rtttolerance(self, rtttolerance) :
		r"""Tolerance, in milliseconds, for newly learned round-trip time (RTT) values. If the difference between the old RTT value and the newly computed RTT value is less than or equal to the specified tolerance value, the LDNS entry in the network metric table is not updated with the new RTT value. Prevents the exchange of metrics when variations in RTT values are negligible.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._rtttolerance = rtttolerance
		except Exception as e:
			raise e

	@property
	def ldnsmask(self) :
		r"""The IPv4 network mask with which to create LDNS entries.<br/>Minimum length =  1.
		"""
		try :
			return self._ldnsmask
		except Exception as e:
			raise e

	@ldnsmask.setter
	def ldnsmask(self, ldnsmask) :
		r"""The IPv4 network mask with which to create LDNS entries.<br/>Minimum length =  1
		"""
		try :
			self._ldnsmask = ldnsmask
		except Exception as e:
			raise e

	@property
	def v6ldnsmasklen(self) :
		r"""Mask for creating LDNS entries for IPv6 source addresses. The mask is defined as the number of leading bits to consider, in the source IP address, when creating an LDNS entry.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6ldnsmasklen
		except Exception as e:
			raise e

	@v6ldnsmasklen.setter
	def v6ldnsmasklen(self, v6ldnsmasklen) :
		r"""Mask for creating LDNS entries for IPv6 source addresses. The mask is defined as the number of leading bits to consider, in the source IP address, when creating an LDNS entry.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6ldnsmasklen = v6ldnsmasklen
		except Exception as e:
			raise e

	@property
	def ldnsprobeorder(self) :
		r"""Order in which monitors should be initiated to calculate RTT.<br/>Possible values = PING, DNS, TCP.
		"""
		try :
			return self._ldnsprobeorder
		except Exception as e:
			raise e

	@ldnsprobeorder.setter
	def ldnsprobeorder(self, ldnsprobeorder) :
		r"""Order in which monitors should be initiated to calculate RTT.<br/>Possible values = PING, DNS, TCP
		"""
		try :
			self._ldnsprobeorder = ldnsprobeorder
		except Exception as e:
			raise e

	@property
	def dropldnsreq(self) :
		r"""Drop LDNS requests if round-trip time (RTT) information is not available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropldnsreq
		except Exception as e:
			raise e

	@dropldnsreq.setter
	def dropldnsreq(self, dropldnsreq) :
		r"""Drop LDNS requests if round-trip time (RTT) information is not available.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropldnsreq = dropldnsreq
		except Exception as e:
			raise e

	@property
	def gslbsvcstatedelaytime(self) :
		r"""Amount of delay in updating the state of GSLB service to DOWN when MEP goes down.
		This parameter is applicable only if monitors are not bound to GSLB services.<br/>Default value: 0<br/>Maximum length =  3600.
		"""
		try :
			return self._gslbsvcstatedelaytime
		except Exception as e:
			raise e

	@gslbsvcstatedelaytime.setter
	def gslbsvcstatedelaytime(self, gslbsvcstatedelaytime) :
		r"""Amount of delay in updating the state of GSLB service to DOWN when MEP goes down.
		This parameter is applicable only if monitors are not bound to GSLB services.<br/>Default value: 0<br/>Maximum length =  3600
		"""
		try :
			self._gslbsvcstatedelaytime = gslbsvcstatedelaytime
		except Exception as e:
			raise e

	@property
	def svcstatelearningtime(self) :
		r"""Time (in seconds) within which local or child site services remain in learning phase. GSLB site will enter the learning phase after reboot, HA failover, Cluster GSLB owner node changes or MEP being enabled on local node.  Backup parent (if configured) will selectively move the adopted children's GSLB services to learning phase when primary parent goes down. While a service is in learning period, remote site will not honour the state and stats got through MEP for that service. State can be learnt from health monitor if bound explicitly.<br/>Default value: 0<br/>Maximum length =  3600.
		"""
		try :
			return self._svcstatelearningtime
		except Exception as e:
			raise e

	@svcstatelearningtime.setter
	def svcstatelearningtime(self, svcstatelearningtime) :
		r"""Time (in seconds) within which local or child site services remain in learning phase. GSLB site will enter the learning phase after reboot, HA failover, Cluster GSLB owner node changes or MEP being enabled on local node.  Backup parent (if configured) will selectively move the adopted children's GSLB services to learning phase when primary parent goes down. While a service is in learning period, remote site will not honour the state and stats got through MEP for that service. State can be learnt from health monitor if bound explicitly.<br/>Default value: 0<br/>Maximum length =  3600
		"""
		try :
			self._svcstatelearningtime = svcstatelearningtime
		except Exception as e:
			raise e

	@property
	def automaticconfigsync(self) :
		r"""GSLB configuration will be synced automatically to remote gslb sites if enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._automaticconfigsync
		except Exception as e:
			raise e

	@automaticconfigsync.setter
	def automaticconfigsync(self, automaticconfigsync) :
		r"""GSLB configuration will be synced automatically to remote gslb sites if enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._automaticconfigsync = automaticconfigsync
		except Exception as e:
			raise e

	@property
	def mepkeepalivetimeout(self) :
		r"""Time duartion (in seconds) during which if no new packets received by Local gslb site from Remote gslb site then mark the MEP connection DOWN.<br/>Default value: 10<br/>Minimum length =  1.
		"""
		try :
			return self._mepkeepalivetimeout
		except Exception as e:
			raise e

	@mepkeepalivetimeout.setter
	def mepkeepalivetimeout(self, mepkeepalivetimeout) :
		r"""Time duartion (in seconds) during which if no new packets received by Local gslb site from Remote gslb site then mark the MEP connection DOWN.<br/>Default value: 10<br/>Minimum length =  1
		"""
		try :
			self._mepkeepalivetimeout = mepkeepalivetimeout
		except Exception as e:
			raise e

	@property
	def gslbsyncinterval(self) :
		r"""Time duartion (in seconds) for which the gslb sync process will wait before checking for config changes.<br/>Default value: 10<br/>Minimum length =  1.
		"""
		try :
			return self._gslbsyncinterval
		except Exception as e:
			raise e

	@gslbsyncinterval.setter
	def gslbsyncinterval(self, gslbsyncinterval) :
		r"""Time duartion (in seconds) for which the gslb sync process will wait before checking for config changes.<br/>Default value: 10<br/>Minimum length =  1
		"""
		try :
			self._gslbsyncinterval = gslbsyncinterval
		except Exception as e:
			raise e

	@property
	def gslbsyncmode(self) :
		r"""Mode in which configuration will be synced from master site to remote sites.<br/>Default value: IncrementalSync<br/>Possible values = IncrementalSync, FullSync.
		"""
		try :
			return self._gslbsyncmode
		except Exception as e:
			raise e

	@gslbsyncmode.setter
	def gslbsyncmode(self, gslbsyncmode) :
		r"""Mode in which configuration will be synced from master site to remote sites.<br/>Default value: IncrementalSync<br/>Possible values = IncrementalSync, FullSync
		"""
		try :
			self._gslbsyncmode = gslbsyncmode
		except Exception as e:
			raise e

	@property
	def gslbsynclocfiles(self) :
		r"""If disabled, Location files will not be synced to the remote sites as part of automatic sync.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._gslbsynclocfiles
		except Exception as e:
			raise e

	@gslbsynclocfiles.setter
	def gslbsynclocfiles(self, gslbsynclocfiles) :
		r"""If disabled, Location files will not be synced to the remote sites as part of automatic sync.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._gslbsynclocfiles = gslbsynclocfiles
		except Exception as e:
			raise e

	@property
	def gslbconfigsyncmonitor(self) :
		r"""If enabled, remote gslb site's rsync port will be monitored and site is considered for configuration sync only when the monitor is successful.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._gslbconfigsyncmonitor
		except Exception as e:
			raise e

	@gslbconfigsyncmonitor.setter
	def gslbconfigsyncmonitor(self, gslbconfigsyncmonitor) :
		r"""If enabled, remote gslb site's rsync port will be monitored and site is considered for configuration sync only when the monitor is successful.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._gslbconfigsyncmonitor = gslbconfigsyncmonitor
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""State of the GSLB parameter.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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

	@property
	def incarnation(self) :
		r"""This is a counter to maintain the gslb sync incarnation number.
		"""
		try :
			return self._incarnation
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbparameter
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
		updateresource = gslbparameter()
		updateresource.ldnsentrytimeout = resource.ldnsentrytimeout
		updateresource.rtttolerance = resource.rtttolerance
		updateresource.ldnsmask = resource.ldnsmask
		updateresource.v6ldnsmasklen = resource.v6ldnsmasklen
		updateresource.ldnsprobeorder = resource.ldnsprobeorder
		updateresource.dropldnsreq = resource.dropldnsreq
		updateresource.gslbsvcstatedelaytime = resource.gslbsvcstatedelaytime
		updateresource.svcstatelearningtime = resource.svcstatelearningtime
		updateresource.automaticconfigsync = resource.automaticconfigsync
		updateresource.mepkeepalivetimeout = resource.mepkeepalivetimeout
		updateresource.gslbsyncinterval = resource.gslbsyncinterval
		updateresource.gslbsyncmode = resource.gslbsyncmode
		updateresource.gslbsynclocfiles = resource.gslbsynclocfiles
		updateresource.gslbconfigsyncmonitor = resource.gslbconfigsyncmonitor
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update gslbparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of gslbparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the gslbparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Gslbsyncmode:
		IncrementalSync = "IncrementalSync"
		FullSync = "FullSync"

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

	class Gslbconfigsyncmonitor:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Gslbsynclocfiles:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Automaticconfigsync:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Dropldnsreq:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ldnsprobeorder:
		PING = "PING"
		DNS = "DNS"
		TCP = "TCP"

class gslbparameter_response(base_response) :
	def __init__(self, length=1) :
		self.gslbparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbparameter = [gslbparameter() for _ in range(length)]

