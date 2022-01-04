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

class protocolquic_stats(base_resource) :
	r""" Statistics for QUIC protocol resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._quicclientdgrmrcvd = 0
		self._quicclientdgrmrcvdrate = 0
		self._quicserverdgrmrcvd = 0
		self._quicserverdgrmrcvdrate = 0
		self._quicclientdgrmsent = 0
		self._quicclientdgrmsentrate = 0
		self._quicserverdgrmsent = 0
		self._quicserverdgrmsentrate = 0
		self._quiccurclientconn = 0
		self._quiccurclientconnrate = 0
		self._quiccurserverconn = 0
		self._quiccurserverconnrate = 0
		self._quiclocalconnid = 0
		self._quiclocalconnidrate = 0
		self._quictotclientconn = 0
		self._quicclientconnrate = 0
		self._quictotserverconn = 0
		self._quicserverconnrate = 0
		self._quicmigratedconn = 0
		self._quicmigratedconnrate = 0
		self._quicjumboframesrcvd = 0
		self._quicjumboframesrcvdrate = 0
		self._quicretrypktsent = 0
		self._quicretrypktsentrate = 0
		self._quichandshakecmpltd = 0
		self._quichandshakecmpltdrate = 0
		self._quictransptconnclosepktsent = 0
		self._quictransptconnclosepktsentrate = 0
		self._quicappconnclosepktsent = 0
		self._quicappconnclosepktsentrate = 0
		self._quicconninfoalcfail = 0
		self._quicconninfoalcfailrate = 0
		self._quicnsbalcfail = 0
		self._quicnsbalcfailrate = 0
		self._quictlsalertsent = 0
		self._quictlsalertsentrate = 0
		self._quicstlessconnclosepktsent = 0
		self._quicstlessconnclosepktsentrate = 0
		self._quicvernegpktsent = 0
		self._quicvernegpktsentrate = 0
		self._quictransptconnclosepktfail = 0
		self._quictransptconnclosepktfailrate = 0
		self._quicappconnclosepktfail = 0
		self._quicappconnclosepktfailrate = 0
		self._quicretrytokenverfail = 0
		self._quicretrytokenverfailrate = 0
		self._quicnewtokenverfail = 0
		self._quicnewtokenverfailrate = 0

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
	def quicserverdgrmrcvd(self) :
		r"""Total QUIC server UDP datagrams received.
		"""
		try :
			return self._quicserverdgrmrcvd
		except Exception as e:
			raise e

	@property
	def quicstlessconnclosepktsent(self) :
		r"""Number of QUIC stateless Connection Close packets sent.
		"""
		try :
			return self._quicstlessconnclosepktsent
		except Exception as e:
			raise e

	@property
	def quichandshakecmpltdrate(self) :
		r"""Rate (/s) counter for quichandshakecmpltd.
		"""
		try :
			return self._quichandshakecmpltdrate
		except Exception as e:
			raise e

	@property
	def quichandshakecmpltd(self) :
		r"""Number of QUIC handshake messages completed.
		"""
		try :
			return self._quichandshakecmpltd
		except Exception as e:
			raise e

	@property
	def quiccurclientconn(self) :
		r"""Current QUIC client connections.
		"""
		try :
			return self._quiccurclientconn
		except Exception as e:
			raise e

	@property
	def quictransptconnclosepktsent(self) :
		r"""Number of QUIC transport no-error Connection Close packets sent.
		"""
		try :
			return self._quictransptconnclosepktsent
		except Exception as e:
			raise e

	@property
	def quicretrypktsentrate(self) :
		r"""Rate (/s) counter for quicretrypktsent.
		"""
		try :
			return self._quicretrypktsentrate
		except Exception as e:
			raise e

	@property
	def quictransptconnclosepktfail(self) :
		r"""Number of QUIC transport error Connection Close packets sent.
		"""
		try :
			return self._quictransptconnclosepktfail
		except Exception as e:
			raise e

	@property
	def quictotserverconn(self) :
		r"""Total QUIC server connections.
		"""
		try :
			return self._quictotserverconn
		except Exception as e:
			raise e

	@property
	def quiccurclientconnrate(self) :
		r"""Rate (/s) counter for quiccurclientconn.
		"""
		try :
			return self._quiccurclientconnrate
		except Exception as e:
			raise e

	@property
	def quiclocalconnid(self) :
		r"""Current QUIC local connection IDs allocated.
		"""
		try :
			return self._quiclocalconnid
		except Exception as e:
			raise e

	@property
	def quiccurserverconn(self) :
		r"""Current QUIC server connections.
		"""
		try :
			return self._quiccurserverconn
		except Exception as e:
			raise e

	@property
	def quicclientconnrate(self) :
		r"""Rate (/s) counter for quictotclientconn.
		"""
		try :
			return self._quicclientconnrate
		except Exception as e:
			raise e

	@property
	def quictransptconnclosepktfailrate(self) :
		r"""Rate (/s) counter for quictransptconnclosepktfail.
		"""
		try :
			return self._quictransptconnclosepktfailrate
		except Exception as e:
			raise e

	@property
	def quicserverconnrate(self) :
		r"""Rate (/s) counter for quictotserverconn.
		"""
		try :
			return self._quicserverconnrate
		except Exception as e:
			raise e

	@property
	def quicserverdgrmsentrate(self) :
		r"""Rate (/s) counter for quicserverdgrmsent.
		"""
		try :
			return self._quicserverdgrmsentrate
		except Exception as e:
			raise e

	@property
	def quicserverdgrmsent(self) :
		r"""Total QUIC server UDP datagrams sent.
		"""
		try :
			return self._quicserverdgrmsent
		except Exception as e:
			raise e

	@property
	def quicretrypktsent(self) :
		r"""Number of QUIC Retry packets sent.
		"""
		try :
			return self._quicretrypktsent
		except Exception as e:
			raise e

	@property
	def quicvernegpktsentrate(self) :
		r"""Rate (/s) counter for quicvernegpktsent.
		"""
		try :
			return self._quicvernegpktsentrate
		except Exception as e:
			raise e

	@property
	def quicjumboframesrcvd(self) :
		r"""Total number of QUIC jumbo frames received.
		"""
		try :
			return self._quicjumboframesrcvd
		except Exception as e:
			raise e

	@property
	def quicstlessconnclosepktsentrate(self) :
		r"""Rate (/s) counter for quicstlessconnclosepktsent.
		"""
		try :
			return self._quicstlessconnclosepktsentrate
		except Exception as e:
			raise e

	@property
	def quicretrytokenverfail(self) :
		r"""Number of times QUIC Retry token verification failed.
		"""
		try :
			return self._quicretrytokenverfail
		except Exception as e:
			raise e

	@property
	def quicappconnclosepktfail(self) :
		r"""Number of QUIC application error Connection Close packets sent.
		"""
		try :
			return self._quicappconnclosepktfail
		except Exception as e:
			raise e

	@property
	def quiccurserverconnrate(self) :
		r"""Rate (/s) counter for quiccurserverconn.
		"""
		try :
			return self._quiccurserverconnrate
		except Exception as e:
			raise e

	@property
	def quicmigratedconn(self) :
		r"""Total number of migrated QUIC connections.
		"""
		try :
			return self._quicmigratedconn
		except Exception as e:
			raise e

	@property
	def quicconninfoalcfailrate(self) :
		r"""Rate (/s) counter for quicconninfoalcfail.
		"""
		try :
			return self._quicconninfoalcfailrate
		except Exception as e:
			raise e

	@property
	def quictransptconnclosepktsentrate(self) :
		r"""Rate (/s) counter for quictransptconnclosepktsent.
		"""
		try :
			return self._quictransptconnclosepktsentrate
		except Exception as e:
			raise e

	@property
	def quicnewtokenverfail(self) :
		r"""Number of times QUIC NEW_TOKEN token verification failed.
		"""
		try :
			return self._quicnewtokenverfail
		except Exception as e:
			raise e

	@property
	def quicappconnclosepktsent(self) :
		r"""Number of QUIC application no-error Connection Close packets sent.
		"""
		try :
			return self._quicappconnclosepktsent
		except Exception as e:
			raise e

	@property
	def quiclocalconnidrate(self) :
		r"""Rate (/s) counter for quiclocalconnid.
		"""
		try :
			return self._quiclocalconnidrate
		except Exception as e:
			raise e

	@property
	def quicserverdgrmrcvdrate(self) :
		r"""Rate (/s) counter for quicserverdgrmrcvd.
		"""
		try :
			return self._quicserverdgrmrcvdrate
		except Exception as e:
			raise e

	@property
	def quicjumboframesrcvdrate(self) :
		r"""Rate (/s) counter for quicjumboframesrcvd.
		"""
		try :
			return self._quicjumboframesrcvdrate
		except Exception as e:
			raise e

	@property
	def quicretrytokenverfailrate(self) :
		r"""Rate (/s) counter for quicretrytokenverfail.
		"""
		try :
			return self._quicretrytokenverfailrate
		except Exception as e:
			raise e

	@property
	def quicclientdgrmsent(self) :
		r"""Total QUIC client UDP datagrams sent.
		"""
		try :
			return self._quicclientdgrmsent
		except Exception as e:
			raise e

	@property
	def quictlsalertsentrate(self) :
		r"""Rate (/s) counter for quictlsalertsent.
		"""
		try :
			return self._quictlsalertsentrate
		except Exception as e:
			raise e

	@property
	def quicconninfoalcfail(self) :
		r"""Quic session allocations failed.
		"""
		try :
			return self._quicconninfoalcfail
		except Exception as e:
			raise e

	@property
	def quicvernegpktsent(self) :
		r"""Number of QUIC Version Negotiation packets sent.
		"""
		try :
			return self._quicvernegpktsent
		except Exception as e:
			raise e

	@property
	def quictotclientconn(self) :
		r"""Total QUIC client connections.
		"""
		try :
			return self._quictotclientconn
		except Exception as e:
			raise e

	@property
	def quicmigratedconnrate(self) :
		r"""Rate (/s) counter for quicmigratedconn.
		"""
		try :
			return self._quicmigratedconnrate
		except Exception as e:
			raise e

	@property
	def quicnsbalcfail(self) :
		r"""Quic NSB allocations failed.
		"""
		try :
			return self._quicnsbalcfail
		except Exception as e:
			raise e

	@property
	def quicappconnclosepktsentrate(self) :
		r"""Rate (/s) counter for quicappconnclosepktsent.
		"""
		try :
			return self._quicappconnclosepktsentrate
		except Exception as e:
			raise e

	@property
	def quicclientdgrmrcvdrate(self) :
		r"""Rate (/s) counter for quicclientdgrmrcvd.
		"""
		try :
			return self._quicclientdgrmrcvdrate
		except Exception as e:
			raise e

	@property
	def quicnsbalcfailrate(self) :
		r"""Rate (/s) counter for quicnsbalcfail.
		"""
		try :
			return self._quicnsbalcfailrate
		except Exception as e:
			raise e

	@property
	def quicclientdgrmrcvd(self) :
		r"""Total QUIC client UDP datagrams received.
		"""
		try :
			return self._quicclientdgrmrcvd
		except Exception as e:
			raise e

	@property
	def quicnewtokenverfailrate(self) :
		r"""Rate (/s) counter for quicnewtokenverfail.
		"""
		try :
			return self._quicnewtokenverfailrate
		except Exception as e:
			raise e

	@property
	def quicappconnclosepktfailrate(self) :
		r"""Rate (/s) counter for quicappconnclosepktfail.
		"""
		try :
			return self._quicappconnclosepktfailrate
		except Exception as e:
			raise e

	@property
	def quicclientdgrmsentrate(self) :
		r"""Rate (/s) counter for quicclientdgrmsent.
		"""
		try :
			return self._quicclientdgrmsentrate
		except Exception as e:
			raise e

	@property
	def quictlsalertsent(self) :
		r"""Total QUIC TLS 1.3 transport errors sent.
		"""
		try :
			return self._quictlsalertsent
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolquic_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolquic
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
		r""" Use this API to fetch the statistics of all protocolquic_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolquic_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolquic_response(base_response) :
	def __init__(self, length=1) :
		self.protocolquic = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolquic = [protocolquic_stats() for _ in range(length)]

