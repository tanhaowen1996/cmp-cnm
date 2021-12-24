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

class protocolquicbridge_stats(base_resource) :
	r""" Statistics for QUIC Bridge protocol resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._quicbridgeconn = 0
		self._quicbridgeconnrate = 0
		self._quicbridgemigratedconn = 0
		self._quicbridgemigratedconnrate = 0
		self._quicbridgeqci = 0
		self._quicbridgeqcirate = 0
		self._quicbridgeqpi = 0
		self._quicbridgeqpirate = 0
		self._quicbridgeqpialcfail = 0
		self._quicbridgeqpialcfailrate = 0
		self._quicbridgeqcialcfail = 0
		self._quicbridgeqcialcfailrate = 0

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
	def quicbridgeqpialcfail(self) :
		r"""Number of QUIC Bridge peer info allocation failures.
		"""
		try :
			return self._quicbridgeqpialcfail
		except Exception as e:
			raise e

	@property
	def quicbridgemigratedconnrate(self) :
		r"""Rate (/s) counter for quicbridgemigratedconn.
		"""
		try :
			return self._quicbridgemigratedconnrate
		except Exception as e:
			raise e

	@property
	def quicbridgeqcialcfailrate(self) :
		r"""Rate (/s) counter for quicbridgeqcialcfail.
		"""
		try :
			return self._quicbridgeqcialcfailrate
		except Exception as e:
			raise e

	@property
	def quicbridgeconnrate(self) :
		r"""Rate (/s) counter for quicbridgeconn.
		"""
		try :
			return self._quicbridgeconnrate
		except Exception as e:
			raise e

	@property
	def quicbridgeqcirate(self) :
		r"""Rate (/s) counter for quicbridgeqci.
		"""
		try :
			return self._quicbridgeqcirate
		except Exception as e:
			raise e

	@property
	def quicbridgeqpialcfailrate(self) :
		r"""Rate (/s) counter for quicbridgeqpialcfail.
		"""
		try :
			return self._quicbridgeqpialcfailrate
		except Exception as e:
			raise e

	@property
	def quicbridgeqci(self) :
		r"""Current number of QUIC Bridge connection infos.
		"""
		try :
			return self._quicbridgeqci
		except Exception as e:
			raise e

	@property
	def quicbridgeqpi(self) :
		r"""Current number of QUIC Bridge peer infos.
		"""
		try :
			return self._quicbridgeqpi
		except Exception as e:
			raise e

	@property
	def quicbridgeqcialcfail(self) :
		r"""Number of QUIC Bridge connection info allocation failures.
		"""
		try :
			return self._quicbridgeqcialcfail
		except Exception as e:
			raise e

	@property
	def quicbridgeqpirate(self) :
		r"""Rate (/s) counter for quicbridgeqpi.
		"""
		try :
			return self._quicbridgeqpirate
		except Exception as e:
			raise e

	@property
	def quicbridgemigratedconn(self) :
		r"""Total number of migrated QUIC Bridge connections.
		"""
		try :
			return self._quicbridgemigratedconn
		except Exception as e:
			raise e

	@property
	def quicbridgeconn(self) :
		r"""Total number of QUIC Bridge connections.
		"""
		try :
			return self._quicbridgeconn
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolquicbridge_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolquicbridge
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
		r""" Use this API to fetch the statistics of all protocolquicbridge_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolquicbridge_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolquicbridge_response(base_response) :
	def __init__(self, length=1) :
		self.protocolquicbridge = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolquicbridge = [protocolquicbridge_stats() for _ in range(length)]

