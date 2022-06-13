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

class protocolhttp2_stats(base_resource) :
	r""" Statistics for http2 resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._http2requests = 0
		self._http2requestsrate = 0
		self._http2responses = 0
		self._http2responsesrate = 0
		self._http2totgrpcrequest = 0
		self._http2grpcrequestrate = 0
		self._http2totgrpcresponse = 0
		self._http2grpcresponserate = 0
		self._http2totgrpcsuccess = 0
		self._http2grpcsuccessrate = 0
		self._http2totgrpcfailure = 0
		self._http2grpcfailurerate = 0
		self._http2direct = 0
		self._http2directrate = 0
		self._http2serverdirect = 0
		self._http2serverdirectrate = 0
		self._http2requpg = 0
		self._http2requpgrate = 0
		self._http2nomatcipher = 0
		self._http2nomatcipherrate = 0
		self._http2serverdirectfailed = 0
		self._http2serverdirectfailedrate = 0
		self._http2serverupgradefailed = 0
		self._http2serverupgradefailedrate = 0
		self._http2requestupgradefailed = 0
		self._http2requestupgradefailedrate = 0
		self._http2dataframessent = 0
		self._http2dataframessentrate = 0
		self._http2headerframessent = 0
		self._http2headerframessentrate = 0
		self._http2priorityframessent = 0
		self._http2priorityframessentrate = 0
		self._http2rststreamframessent = 0
		self._http2rststreamframessentrate = 0
		self._http2settingframessent = 0
		self._http2settingframessentrate = 0
		self._http2pushpromiseframessent = 0
		self._http2pushpromiseframessentrate = 0
		self._http2pingframessent = 0
		self._http2pingframessentrate = 0
		self._http2goawayframessent = 0
		self._http2goawayframessentrate = 0
		self._http2windowupdateframessent = 0
		self._http2windowupdateframessentrate = 0
		self._http2continuationframessent = 0
		self._http2continuationframessentrate = 0
		self._http2altsvcframessent = 0
		self._http2altsvcframessentrate = 0
		self._http2dataframesrcvd = 0
		self._http2dataframesrcvdrate = 0
		self._http2headerframesrcvd = 0
		self._http2headerframesrcvdrate = 0
		self._http2priorityframesrcvd = 0
		self._http2priorityframesrcvdrate = 0
		self._http2rststreamframesrcvd = 0
		self._http2rststreamframesrcvdrate = 0
		self._http2settingframesrcvd = 0
		self._http2settingframesrcvdrate = 0
		self._http2pushpromframesrcvd = 0
		self._http2pushpromframesrcvdrate = 0
		self._http2pingframesrcvd = 0
		self._http2pingframesrcvdrate = 0
		self._http2goawayframesrcvd = 0
		self._http2goawayframesrcvdrate = 0
		self._http2winupdateframesrcvd = 0
		self._http2winupdateframesrcvdrate = 0
		self._http2continuationframesrcvd = 0
		self._http2continuationframesrcvdrate = 0
		self._http2indataframes = 0
		self._http2indataframesrate = 0
		self._http2inheaderframes = 0
		self._http2inheaderframesrate = 0
		self._http2inpriorityframes = 0
		self._http2inpriorityframesrate = 0
		self._http2inrststreamframes = 0
		self._http2inrststreamframesrate = 0
		self._http2insettingframes = 0
		self._http2insettingframesrate = 0
		self._http2inpushpromiseframes = 0
		self._http2inpushpromiseframesrate = 0
		self._http2inpingframes = 0
		self._http2inpingframesrate = 0
		self._http2ingoawayframes = 0
		self._http2ingoawayframesrate = 0
		self._http2inwindowupdateframes = 0
		self._http2inwindowupdateframesrate = 0
		self._http2incontinuationframes = 0
		self._http2incontinuationframesrate = 0
		self._http2frametoobig = 0
		self._http2frametoobigrate = 0
		self._http2pingflood = 0
		self._http2pingfloodrate = 0
		self._http2errsetflood = 0
		self._http2errsetfloodrate = 0
		self._http2errresfraflood = 0
		self._http2errresfrafloodrate = 0
		self._http2errempfraflood = 0
		self._http2errempfrafloodrate = 0

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
	def http2errresfrafloodrate(self) :
		r"""Rate (/s) counter for http2errresfraflood.
		"""
		try :
			return self._http2errresfrafloodrate
		except Exception as e:
			raise e

	@property
	def http2requpgrate(self) :
		r"""Rate (/s) counter for http2requpg.
		"""
		try :
			return self._http2requpgrate
		except Exception as e:
			raise e

	@property
	def http2dataframesrcvdrate(self) :
		r"""Rate (/s) counter for http2dataframesrcvd.
		"""
		try :
			return self._http2dataframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2inpriorityframesrate(self) :
		r"""Rate (/s) counter for http2inpriorityframes.
		"""
		try :
			return self._http2inpriorityframesrate
		except Exception as e:
			raise e

	@property
	def http2serverdirectrate(self) :
		r"""Rate (/s) counter for http2serverdirect.
		"""
		try :
			return self._http2serverdirectrate
		except Exception as e:
			raise e

	@property
	def http2priorityframessent(self) :
		r"""Number of HTTP/2 PRIORITY frames sent.
		"""
		try :
			return self._http2priorityframessent
		except Exception as e:
			raise e

	@property
	def http2headerframessent(self) :
		r"""Number of HTTP/2 HEADER frames sent.
		"""
		try :
			return self._http2headerframessent
		except Exception as e:
			raise e

	@property
	def http2serverupgradefailedrate(self) :
		r"""Rate (/s) counter for http2serverupgradefailed.
		"""
		try :
			return self._http2serverupgradefailedrate
		except Exception as e:
			raise e

	@property
	def http2inheaderframes(self) :
		r"""Number of HTTP/2 HEADER frames.
		"""
		try :
			return self._http2inheaderframes
		except Exception as e:
			raise e

	@property
	def http2pushpromframesrcvdrate(self) :
		r"""Rate (/s) counter for http2pushpromframesrcvd.
		"""
		try :
			return self._http2pushpromframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2responsesrate(self) :
		r"""Rate (/s) counter for http2responses.
		"""
		try :
			return self._http2responsesrate
		except Exception as e:
			raise e

	@property
	def http2inpriorityframes(self) :
		r"""Number of HTTP/2 PRIORITY frames.
		"""
		try :
			return self._http2inpriorityframes
		except Exception as e:
			raise e

	@property
	def http2serverdirectfailedrate(self) :
		r"""Rate (/s) counter for http2serverdirectfailed.
		"""
		try :
			return self._http2serverdirectfailedrate
		except Exception as e:
			raise e

	@property
	def http2serverdirectfailed(self) :
		r"""Number of HTTP/2 server direct failed.
		"""
		try :
			return self._http2serverdirectfailed
		except Exception as e:
			raise e

	@property
	def http2goawayframesrcvd(self) :
		r"""Number of HTTP/2 GOAWAY frames received.
		"""
		try :
			return self._http2goawayframesrcvd
		except Exception as e:
			raise e

	@property
	def http2dataframessent(self) :
		r"""Number of HTTP/2 DATA frames sent.
		"""
		try :
			return self._http2dataframessent
		except Exception as e:
			raise e

	@property
	def http2continuationframesrcvd(self) :
		r"""Number of HTTP/2 CONTINUATION frames received.
		"""
		try :
			return self._http2continuationframesrcvd
		except Exception as e:
			raise e

	@property
	def http2rststreamframessent(self) :
		r"""Number of HTTP/2 RST_STREAM frames sent.
		"""
		try :
			return self._http2rststreamframessent
		except Exception as e:
			raise e

	@property
	def http2rststreamframesrcvd(self) :
		r"""Number of HTTP/2 RST_STREAM frames received.
		"""
		try :
			return self._http2rststreamframesrcvd
		except Exception as e:
			raise e

	@property
	def http2inwindowupdateframesrate(self) :
		r"""Rate (/s) counter for http2inwindowupdateframes.
		"""
		try :
			return self._http2inwindowupdateframesrate
		except Exception as e:
			raise e

	@property
	def http2windowupdateframessent(self) :
		r"""Number of HTTP/2 WINDOW_UPDATE frames sent.
		"""
		try :
			return self._http2windowupdateframessent
		except Exception as e:
			raise e

	@property
	def http2headerframesrcvdrate(self) :
		r"""Rate (/s) counter for http2headerframesrcvd.
		"""
		try :
			return self._http2headerframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2pingframessent(self) :
		r"""Number of HTTP/2 PING frames sent.
		"""
		try :
			return self._http2pingframessent
		except Exception as e:
			raise e

	@property
	def http2requests(self) :
		r"""Total number of http2 requests.
		"""
		try :
			return self._http2requests
		except Exception as e:
			raise e

	@property
	def http2errsetfloodrate(self) :
		r"""Rate (/s) counter for http2errsetflood.
		"""
		try :
			return self._http2errsetfloodrate
		except Exception as e:
			raise e

	@property
	def http2inpingframesrate(self) :
		r"""Rate (/s) counter for http2inpingframes.
		"""
		try :
			return self._http2inpingframesrate
		except Exception as e:
			raise e

	@property
	def http2requestsrate(self) :
		r"""Rate (/s) counter for http2requests.
		"""
		try :
			return self._http2requestsrate
		except Exception as e:
			raise e

	@property
	def http2inpingframes(self) :
		r"""Number of HTTP/2 PING frames.
		"""
		try :
			return self._http2inpingframes
		except Exception as e:
			raise e

	@property
	def http2priorityframessentrate(self) :
		r"""Rate (/s) counter for http2priorityframessent.
		"""
		try :
			return self._http2priorityframessentrate
		except Exception as e:
			raise e

	@property
	def http2settingframesrcvd(self) :
		r"""Number of HTTP/2 SETTINGS frames received.
		"""
		try :
			return self._http2settingframesrcvd
		except Exception as e:
			raise e

	@property
	def http2windowupdateframessentrate(self) :
		r"""Rate (/s) counter for http2windowupdateframessent.
		"""
		try :
			return self._http2windowupdateframessentrate
		except Exception as e:
			raise e

	@property
	def http2nomatcipherrate(self) :
		r"""Rate (/s) counter for http2nomatcipher.
		"""
		try :
			return self._http2nomatcipherrate
		except Exception as e:
			raise e

	@property
	def http2headerframessentrate(self) :
		r"""Rate (/s) counter for http2headerframessent.
		"""
		try :
			return self._http2headerframessentrate
		except Exception as e:
			raise e

	@property
	def http2serverupgradefailed(self) :
		r"""Number of HTTP/2 server upgrade failed.
		"""
		try :
			return self._http2serverupgradefailed
		except Exception as e:
			raise e

	@property
	def http2indataframes(self) :
		r"""Number of HTTP/2 DATA frames.
		"""
		try :
			return self._http2indataframes
		except Exception as e:
			raise e

	@property
	def http2errsetflood(self) :
		r"""HTTP/2 number of settings frames received on connection is above rate limit.
		"""
		try :
			return self._http2errsetflood
		except Exception as e:
			raise e

	@property
	def http2frametoobig(self) :
		r"""Number of HTTP/2 frames received carrying a frame length greater than SETTINGS_MAX_FRAME_SIZE sent by NetScale .
		"""
		try :
			return self._http2frametoobig
		except Exception as e:
			raise e

	@property
	def http2priorityframesrcvd(self) :
		r"""Total number of http2 priority frames received.
		"""
		try :
			return self._http2priorityframesrcvd
		except Exception as e:
			raise e

	@property
	def http2direct(self) :
		r"""Total number of http2 direct connections established.
		"""
		try :
			return self._http2direct
		except Exception as e:
			raise e

	@property
	def http2incontinuationframes(self) :
		r"""Number of HTTP/2 CONTINUATION frames.
		"""
		try :
			return self._http2incontinuationframes
		except Exception as e:
			raise e

	@property
	def http2inpushpromiseframesrate(self) :
		r"""Rate (/s) counter for http2inpushpromiseframes.
		"""
		try :
			return self._http2inpushpromiseframesrate
		except Exception as e:
			raise e

	@property
	def http2pingframesrcvdrate(self) :
		r"""Rate (/s) counter for http2pingframesrcvd.
		"""
		try :
			return self._http2pingframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2pushpromiseframessent(self) :
		r"""Number of HTTP/2 PUSH_PROMISE frames sent.
		"""
		try :
			return self._http2pushpromiseframessent
		except Exception as e:
			raise e

	@property
	def http2ingoawayframesrate(self) :
		r"""Rate (/s) counter for http2ingoawayframes.
		"""
		try :
			return self._http2ingoawayframesrate
		except Exception as e:
			raise e

	@property
	def http2totgrpcfailure(self) :
		r"""Total number of gRPC failures.
		"""
		try :
			return self._http2totgrpcfailure
		except Exception as e:
			raise e

	@property
	def http2dataframesrcvd(self) :
		r"""Number of HTTP/2 DATA frames received.
		"""
		try :
			return self._http2dataframesrcvd
		except Exception as e:
			raise e

	@property
	def http2insettingframes(self) :
		r"""Number of HTTP/2 SETTINGS frames.
		"""
		try :
			return self._http2insettingframes
		except Exception as e:
			raise e

	@property
	def http2nomatcipher(self) :
		r"""Total number of cipher mismatch failures.
		"""
		try :
			return self._http2nomatcipher
		except Exception as e:
			raise e

	@property
	def http2inwindowupdateframes(self) :
		r"""Number of HTTP/2 WINDOW_UPDATE frames.
		"""
		try :
			return self._http2inwindowupdateframes
		except Exception as e:
			raise e

	@property
	def http2priorityframesrcvdrate(self) :
		r"""Rate (/s) counter for http2priorityframesrcvd.
		"""
		try :
			return self._http2priorityframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2winupdateframesrcvd(self) :
		r"""Number of HTTP/2 WINDOW_UPDATE frames received.
		"""
		try :
			return self._http2winupdateframesrcvd
		except Exception as e:
			raise e

	@property
	def http2altsvcframessent(self) :
		r"""Number of HTTP/2 ALTSVC frames sent.
		"""
		try :
			return self._http2altsvcframessent
		except Exception as e:
			raise e

	@property
	def http2pingframessentrate(self) :
		r"""Rate (/s) counter for http2pingframessent.
		"""
		try :
			return self._http2pingframessentrate
		except Exception as e:
			raise e

	@property
	def http2totgrpcresponse(self) :
		r"""Total number of gRPC responses.
		"""
		try :
			return self._http2totgrpcresponse
		except Exception as e:
			raise e

	@property
	def http2goawayframesrcvdrate(self) :
		r"""Rate (/s) counter for http2goawayframesrcvd.
		"""
		try :
			return self._http2goawayframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2continuationframesrcvdrate(self) :
		r"""Rate (/s) counter for http2continuationframesrcvd.
		"""
		try :
			return self._http2continuationframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2pingfloodrate(self) :
		r"""Rate (/s) counter for http2pingflood.
		"""
		try :
			return self._http2pingfloodrate
		except Exception as e:
			raise e

	@property
	def http2rststreamframesrcvdrate(self) :
		r"""Rate (/s) counter for http2rststreamframesrcvd.
		"""
		try :
			return self._http2rststreamframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2inheaderframesrate(self) :
		r"""Rate (/s) counter for http2inheaderframes.
		"""
		try :
			return self._http2inheaderframesrate
		except Exception as e:
			raise e

	@property
	def http2pushpromiseframessentrate(self) :
		r"""Rate (/s) counter for http2pushpromiseframessent.
		"""
		try :
			return self._http2pushpromiseframessentrate
		except Exception as e:
			raise e

	@property
	def http2totgrpcrequest(self) :
		r"""Total number of gRPC requests.
		"""
		try :
			return self._http2totgrpcrequest
		except Exception as e:
			raise e

	@property
	def http2responses(self) :
		r"""Total number of http2 responses.
		"""
		try :
			return self._http2responses
		except Exception as e:
			raise e

	@property
	def http2directrate(self) :
		r"""Rate (/s) counter for http2direct.
		"""
		try :
			return self._http2directrate
		except Exception as e:
			raise e

	@property
	def http2serverdirect(self) :
		r"""Number of HTTP/2 server direct.
		"""
		try :
			return self._http2serverdirect
		except Exception as e:
			raise e

	@property
	def http2pingflood(self) :
		r"""HTTP/2 number of ping frames received on connection is above rate limit.
		"""
		try :
			return self._http2pingflood
		except Exception as e:
			raise e

	@property
	def http2grpcfailurerate(self) :
		r"""Rate (/s) counter for http2totgrpcfailure.
		"""
		try :
			return self._http2grpcfailurerate
		except Exception as e:
			raise e

	@property
	def http2continuationframessentrate(self) :
		r"""Rate (/s) counter for http2continuationframessent.
		"""
		try :
			return self._http2continuationframessentrate
		except Exception as e:
			raise e

	@property
	def http2pushpromframesrcvd(self) :
		r"""Number of HTTP/2 PUSH_PROMISE frames received.
		"""
		try :
			return self._http2pushpromframesrcvd
		except Exception as e:
			raise e

	@property
	def http2altsvcframessentrate(self) :
		r"""Rate (/s) counter for http2altsvcframessent.
		"""
		try :
			return self._http2altsvcframessentrate
		except Exception as e:
			raise e

	@property
	def http2errresfraflood(self) :
		r"""HTTP/2 number of reset frames received on connection is above rate limit.
		"""
		try :
			return self._http2errresfraflood
		except Exception as e:
			raise e

	@property
	def http2grpcsuccessrate(self) :
		r"""Rate (/s) counter for http2totgrpcsuccess.
		"""
		try :
			return self._http2grpcsuccessrate
		except Exception as e:
			raise e

	@property
	def http2goawayframessentrate(self) :
		r"""Rate (/s) counter for http2goawayframessent.
		"""
		try :
			return self._http2goawayframessentrate
		except Exception as e:
			raise e

	@property
	def http2headerframesrcvd(self) :
		r"""Total number of http2 header frames received.
		"""
		try :
			return self._http2headerframesrcvd
		except Exception as e:
			raise e

	@property
	def http2grpcresponserate(self) :
		r"""Rate (/s) counter for http2totgrpcresponse.
		"""
		try :
			return self._http2grpcresponserate
		except Exception as e:
			raise e

	@property
	def http2totgrpcsuccess(self) :
		r"""Total number of gRPC success.
		"""
		try :
			return self._http2totgrpcsuccess
		except Exception as e:
			raise e

	@property
	def http2inrststreamframes(self) :
		r"""Number of HTTP/2 RST_STREAM frames.
		"""
		try :
			return self._http2inrststreamframes
		except Exception as e:
			raise e

	@property
	def http2rststreamframessentrate(self) :
		r"""Rate (/s) counter for http2rststreamframessent.
		"""
		try :
			return self._http2rststreamframessentrate
		except Exception as e:
			raise e

	@property
	def http2incontinuationframesrate(self) :
		r"""Rate (/s) counter for http2incontinuationframes.
		"""
		try :
			return self._http2incontinuationframesrate
		except Exception as e:
			raise e

	@property
	def http2requestupgradefailedrate(self) :
		r"""Rate (/s) counter for http2requestupgradefailed.
		"""
		try :
			return self._http2requestupgradefailedrate
		except Exception as e:
			raise e

	@property
	def http2errempfraflood(self) :
		r"""HTTP/2 number of empty frames received on connection is above rate limit.
		"""
		try :
			return self._http2errempfraflood
		except Exception as e:
			raise e

	@property
	def http2continuationframessent(self) :
		r"""Number of HTTP/2 CONTINUATION frames sent.
		"""
		try :
			return self._http2continuationframessent
		except Exception as e:
			raise e

	@property
	def http2inpushpromiseframes(self) :
		r"""Number of HTTP/2 PUSH_PROMISE frames.
		"""
		try :
			return self._http2inpushpromiseframes
		except Exception as e:
			raise e

	@property
	def http2requestupgradefailed(self) :
		r"""Number of HTTP/2 request upgrade failed.
		"""
		try :
			return self._http2requestupgradefailed
		except Exception as e:
			raise e

	@property
	def http2dataframessentrate(self) :
		r"""Rate (/s) counter for http2dataframessent.
		"""
		try :
			return self._http2dataframessentrate
		except Exception as e:
			raise e

	@property
	def http2settingframesrcvdrate(self) :
		r"""Rate (/s) counter for http2settingframesrcvd.
		"""
		try :
			return self._http2settingframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2winupdateframesrcvdrate(self) :
		r"""Rate (/s) counter for http2winupdateframesrcvd.
		"""
		try :
			return self._http2winupdateframesrcvdrate
		except Exception as e:
			raise e

	@property
	def http2indataframesrate(self) :
		r"""Rate (/s) counter for http2indataframes.
		"""
		try :
			return self._http2indataframesrate
		except Exception as e:
			raise e

	@property
	def http2errempfrafloodrate(self) :
		r"""Rate (/s) counter for http2errempfraflood.
		"""
		try :
			return self._http2errempfrafloodrate
		except Exception as e:
			raise e

	@property
	def http2goawayframessent(self) :
		r"""Number of HTTP/2 GOAWAY frames sent.
		"""
		try :
			return self._http2goawayframessent
		except Exception as e:
			raise e

	@property
	def http2requpg(self) :
		r"""Total number of connections upgraded to HTTP2.
		"""
		try :
			return self._http2requpg
		except Exception as e:
			raise e

	@property
	def http2settingframessent(self) :
		r"""Number of HTTP/2 SETTINGS frames sent.
		"""
		try :
			return self._http2settingframessent
		except Exception as e:
			raise e

	@property
	def http2pingframesrcvd(self) :
		r"""Number of HTTP/2 PING frames received.
		"""
		try :
			return self._http2pingframesrcvd
		except Exception as e:
			raise e

	@property
	def http2insettingframesrate(self) :
		r"""Rate (/s) counter for http2insettingframes.
		"""
		try :
			return self._http2insettingframesrate
		except Exception as e:
			raise e

	@property
	def http2ingoawayframes(self) :
		r"""Number of HTTP/2 GOAWAY frames.
		"""
		try :
			return self._http2ingoawayframes
		except Exception as e:
			raise e

	@property
	def http2settingframessentrate(self) :
		r"""Rate (/s) counter for http2settingframessent.
		"""
		try :
			return self._http2settingframessentrate
		except Exception as e:
			raise e

	@property
	def http2frametoobigrate(self) :
		r"""Rate (/s) counter for http2frametoobig.
		"""
		try :
			return self._http2frametoobigrate
		except Exception as e:
			raise e

	@property
	def http2inrststreamframesrate(self) :
		r"""Rate (/s) counter for http2inrststreamframes.
		"""
		try :
			return self._http2inrststreamframesrate
		except Exception as e:
			raise e

	@property
	def http2grpcrequestrate(self) :
		r"""Rate (/s) counter for http2totgrpcrequest.
		"""
		try :
			return self._http2grpcrequestrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolhttp2_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolhttp2
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
		r""" Use this API to fetch the statistics of all protocolhttp2_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolhttp2_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolhttp2_response(base_response) :
	def __init__(self, length=1) :
		self.protocolhttp2 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolhttp2 = [protocolhttp2_stats() for _ in range(length)]

