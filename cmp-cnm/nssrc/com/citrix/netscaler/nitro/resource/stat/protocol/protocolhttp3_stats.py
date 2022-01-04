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

class protocolhttp3_stats(base_resource) :
	r""" Statistics for http3 resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._http3requestsrcvd = 0
		self._http3requestsrcvdrate = 0
		self._http3requestssent = 0
		self._http3requestssentrate = 0
		self._http3responsesrcvd = 0
		self._http3responsesrcvdrate = 0
		self._http3responsessent = 0
		self._http3responsessentrate = 0
		self._http3conninfalcfail = 0
		self._http3conninfalcfailrate = 0
		self._http3nsbalcfail = 0
		self._http3nsbalcfailrate = 0
		self._http3strminfalcfail = 0
		self._http3strminfalcfailrate = 0
		self._http3strmpcbalcfail = 0
		self._http3strmpcbalcfailrate = 0

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def http3strmpcbalcfail(self) :
		r"""Number of HTTP/3 stream PCB allocation failures.
		"""
		try :
			return self._http3strmpcbalcfail
		except Exception as e:
			raise e

	@property
	def http3responsesrcvdrate(self) :
		r"""Rate (/s) counter for http3responsesrcvd.
		"""
		try :
			return self._http3responsesrcvdrate
		except Exception as e:
			raise e

	@property
	def http3conninfalcfail(self) :
		r"""Number of HTTP/3 connection-info allocation failures.
		"""
		try :
			return self._http3conninfalcfail
		except Exception as e:
			raise e

	@property
	def http3requestsrcvdrate(self) :
		r"""Rate (/s) counter for http3requestsrcvd.
		"""
		try :
			return self._http3requestsrcvdrate
		except Exception as e:
			raise e

	@property
	def http3responsesrcvd(self) :
		r"""Total number of HTTP/3 responses received.
		"""
		try :
			return self._http3responsesrcvd
		except Exception as e:
			raise e

	@property
	def http3requestssent(self) :
		r"""Total number of HTTP/3 requests sent.
		"""
		try :
			return self._http3requestssent
		except Exception as e:
			raise e

	@property
	def http3responsessentrate(self) :
		r"""Rate (/s) counter for http3responsessent.
		"""
		try :
			return self._http3responsessentrate
		except Exception as e:
			raise e

	@property
	def http3strmpcbalcfailrate(self) :
		r"""Rate (/s) counter for http3strmpcbalcfail.
		"""
		try :
			return self._http3strmpcbalcfailrate
		except Exception as e:
			raise e

	@property
	def http3strminfalcfailrate(self) :
		r"""Rate (/s) counter for http3strminfalcfail.
		"""
		try :
			return self._http3strminfalcfailrate
		except Exception as e:
			raise e

	@property
	def http3nsbalcfail(self) :
		r"""Number of HTTP/3 NSB allocation failures.
		"""
		try :
			return self._http3nsbalcfail
		except Exception as e:
			raise e

	@property
	def http3requestsrcvd(self) :
		r"""Total number of HTTP/3 requests received.
		"""
		try :
			return self._http3requestsrcvd
		except Exception as e:
			raise e

	@property
	def http3conninfalcfailrate(self) :
		r"""Rate (/s) counter for http3conninfalcfail.
		"""
		try :
			return self._http3conninfalcfailrate
		except Exception as e:
			raise e

	@property
	def http3nsbalcfailrate(self) :
		r"""Rate (/s) counter for http3nsbalcfail.
		"""
		try :
			return self._http3nsbalcfailrate
		except Exception as e:
			raise e

	@property
	def http3requestssentrate(self) :
		r"""Rate (/s) counter for http3requestssent.
		"""
		try :
			return self._http3requestssentrate
		except Exception as e:
			raise e

	@property
	def http3strminfalcfail(self) :
		r"""Number of HTTP/3 stream-info allocation failures.
		"""
		try :
			return self._http3strminfalcfail
		except Exception as e:
			raise e

	@property
	def http3responsessent(self) :
		r"""Total number of HTTP/3 responses sent.
		"""
		try :
			return self._http3responsessent
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolhttp3_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolhttp3
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all protocolhttp3_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolhttp3_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolhttp3_response(base_response) :
	def __init__(self, length=1) :
		self.protocolhttp3 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolhttp3 = [protocolhttp3_stats() for _ in range(length)]

