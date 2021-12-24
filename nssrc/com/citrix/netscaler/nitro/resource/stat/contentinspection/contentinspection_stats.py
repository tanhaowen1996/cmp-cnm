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

class contentinspection_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._inlinerequestssent = 0
		self._inlineresponsessent = 0
		self._inlinereqbytessent = 0
		self._inlinereqbytesrecv = 0
		self._inlinerespbytessent = 0
		self._inlinerespbytesrecv = 0
		self._inlineserverdownreset = 0
		self._inlineserverdowndrop = 0
		self._inlineserverdownbypass = 0
		self._inlinegeneratedresponses = 0
		self._mirrorrequestssent = 0
		self._mirrorresponsessent = 0
		self._mirrorreqbytessent = 0
		self._mirrorrespbytessent = 0
		self._mirrorserverdownreset = 0
		self._mirrorserverdowndrop = 0
		self._mirrorserverdownbypass = 0
		self._icapreqmodrequests = 0
		self._icaprespmodrequests = 0
		self._icappreviewenabledrequests = 0
		self._icap204enabledrequests = 0
		self._icap100contrecv = 0
		self._icap204nocontentrecv = 0
		self._icapadaptiverequests = 0
		self._icapadaptiveresponses = 0
		self._icapcalloutinitiated = 0
		self._icapcalloutcompleted = 0
		self._icaperrorshandled = 0
		self._icapserverdownreset = 0
		self._icapserverdowndrop = 0
		self._icapserverdownbypass = 0

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
	def icapserverdowndrop(self) :
		r"""Number of requests for which serverdown Drop Action is taken.
		"""
		try :
			return self._icapserverdowndrop
		except Exception as e:
			raise e

	@property
	def icapserverdownreset(self) :
		r"""Number of requests for which serverdown Reset Action is taken.
		"""
		try :
			return self._icapserverdownreset
		except Exception as e:
			raise e

	@property
	def inlineserverdownbypass(self) :
		r"""Number of requests bypass content Inspection Module when Inline device is down.
		"""
		try :
			return self._inlineserverdownbypass
		except Exception as e:
			raise e

	@property
	def icappreviewenabledrequests(self) :
		r"""Number of preview requests for ICAP.
		"""
		try :
			return self._icappreviewenabledrequests
		except Exception as e:
			raise e

	@property
	def icapcalloutinitiated(self) :
		r"""Number of callout Requests started.
		"""
		try :
			return self._icapcalloutinitiated
		except Exception as e:
			raise e

	@property
	def inlinereqbytesrecv(self) :
		r"""Number of bytes received for requests from IPS.
		"""
		try :
			return self._inlinereqbytesrecv
		except Exception as e:
			raise e

	@property
	def mirrorrequestssent(self) :
		r"""Number of requests sent for Intrusion Detection.
		"""
		try :
			return self._mirrorrequestssent
		except Exception as e:
			raise e

	@property
	def mirrorserverdownbypass(self) :
		r"""Number of requests bypass ContentInspection module when Mirror device is down.
		"""
		try :
			return self._mirrorserverdownbypass
		except Exception as e:
			raise e

	@property
	def inlinerespbytesrecv(self) :
		r"""Number of bytes received for responses from IPS.
		"""
		try :
			return self._inlinerespbytesrecv
		except Exception as e:
			raise e

	@property
	def inlinereqbytessent(self) :
		r"""Number of bytes transfered for requests to IPS.
		"""
		try :
			return self._inlinereqbytessent
		except Exception as e:
			raise e

	@property
	def icap204nocontentrecv(self) :
		r"""Number of 204 No content responses received.
		"""
		try :
			return self._icap204nocontentrecv
		except Exception as e:
			raise e

	@property
	def icapadaptiverequests(self) :
		r"""Number of Adaptive requests.
		"""
		try :
			return self._icapadaptiverequests
		except Exception as e:
			raise e

	@property
	def inlinerespbytessent(self) :
		r"""Number of bytes transfered for responses to IPS.
		"""
		try :
			return self._inlinerespbytessent
		except Exception as e:
			raise e

	@property
	def inlineserverdowndrop(self) :
		r"""Number of requests Dropped when Inline device is down.
		"""
		try :
			return self._inlineserverdowndrop
		except Exception as e:
			raise e

	@property
	def mirrorserverdowndrop(self) :
		r"""Number of requests Dropped when Mirror device is down.
		"""
		try :
			return self._mirrorserverdowndrop
		except Exception as e:
			raise e

	@property
	def icaperrorshandled(self) :
		r"""Number of errors sent.
		"""
		try :
			return self._icaperrorshandled
		except Exception as e:
			raise e

	@property
	def icapcalloutcompleted(self) :
		r"""Number of callout requests finished.
		"""
		try :
			return self._icapcalloutcompleted
		except Exception as e:
			raise e

	@property
	def mirrorresponsessent(self) :
		r"""Number of responses sent for Intrusion Detection.
		"""
		try :
			return self._mirrorresponsessent
		except Exception as e:
			raise e

	@property
	def inlineresponsessent(self) :
		r"""HTTP/HTTPS responses sent for ContentInspection.
		"""
		try :
			return self._inlineresponsessent
		except Exception as e:
			raise e

	@property
	def mirrorserverdownreset(self) :
		r"""Number of requests Reset when Mirror device is down.
		"""
		try :
			return self._mirrorserverdownreset
		except Exception as e:
			raise e

	@property
	def icap100contrecv(self) :
		r"""Number of 100-continue responses received.
		"""
		try :
			return self._icap100contrecv
		except Exception as e:
			raise e

	@property
	def icapadaptiveresponses(self) :
		r"""Number of Adaptive Responses.
		"""
		try :
			return self._icapadaptiveresponses
		except Exception as e:
			raise e

	@property
	def mirrorrespbytessent(self) :
		r"""Number of response Bytes sent for Intrusion Detection.
		"""
		try :
			return self._mirrorrespbytessent
		except Exception as e:
			raise e

	@property
	def inlineserverdownreset(self) :
		r"""Number of requests Reset when Inline device is down.
		"""
		try :
			return self._inlineserverdownreset
		except Exception as e:
			raise e

	@property
	def icap204enabledrequests(self) :
		r"""Number of 204 Rquests.
		"""
		try :
			return self._icap204enabledrequests
		except Exception as e:
			raise e

	@property
	def inlinerequestssent(self) :
		r"""HTTP/HTTPS requests sent for ContentInspection.
		"""
		try :
			return self._inlinerequestssent
		except Exception as e:
			raise e

	@property
	def icapreqmodrequests(self) :
		r"""Number of requests sent to ICAP Server.
		"""
		try :
			return self._icapreqmodrequests
		except Exception as e:
			raise e

	@property
	def mirrorreqbytessent(self) :
		r"""Number of request Bytes sent for Intrusion Detection.
		"""
		try :
			return self._mirrorreqbytessent
		except Exception as e:
			raise e

	@property
	def icaprespmodrequests(self) :
		r"""Number of responses sent for Intrusion DEtection.
		"""
		try :
			return self._icaprespmodrequests
		except Exception as e:
			raise e

	@property
	def inlinegeneratedresponses(self) :
		r"""Number of Inline device generated Responses.
		"""
		try :
			return self._inlinegeneratedresponses
		except Exception as e:
			raise e

	@property
	def icapserverdownbypass(self) :
		r"""Number of requests for which serverdown Bypass Action is taken.
		"""
		try :
			return self._icapserverdownbypass
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(contentinspection_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.contentinspection
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
		r""" Use this API to fetch the statistics of all contentinspection_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = contentinspection_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class contentinspection_response(base_response) :
	def __init__(self, length=1) :
		self.contentinspection = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.contentinspection = [contentinspection_stats() for _ in range(length)]

