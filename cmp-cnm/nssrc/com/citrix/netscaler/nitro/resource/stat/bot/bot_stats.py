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

class bot_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._botrequests = 0
		self._botrequestsrate = 0
		self._botreqbytes = 0
		self._botreqbytesrate = 0
		self._botresponses = 0
		self._botresponsesrate = 0
		self._botresbytes = 0
		self._botresbytesrate = 0
		self._bottotallog = 0
		self._botlograte = 0
		self._bottotaldrop = 0
		self._botdroprate = 0
		self._bottotalredirect = 0
		self._botredirectrate = 0
		self._bottotalreset = 0
		self._botresetrate = 0
		self._botvioldevicefingerprint = 0
		self._botvioldevicefingerprintrate = 0
		self._botvioldevicefingerprintlog = 0
		self._botvioldevicefingerprintlograte = 0
		self._botvioldevicefingerprintdrop = 0
		self._botvioldevicefingerprintdroprate = 0
		self._botvioldevicefingerprintredirect = 0
		self._botvioldevicefingerprintredirectrate = 0
		self._botvioldevicefingerprintcaptcha = 0
		self._botvioldevicefingerprintcaptcharate = 0
		self._botvioldevicefingerprintreset = 0
		self._botvioldevicefingerprintresetrate = 0
		self._botviolipreputation = 0
		self._botviolipreputationrate = 0
		self._botviolipreputationlog = 0
		self._botviolipreputationlograte = 0
		self._botviolipreputationdrop = 0
		self._botviolipreputationdroprate = 0
		self._botviolipreputationredirect = 0
		self._botviolipreputationredirectrate = 0
		self._botviolipreputationcaptcha = 0
		self._botviolipreputationcaptcharate = 0
		self._botviolipreputationreset = 0
		self._botviolipreputationresetrate = 0
		self._botviolwhitelist = 0
		self._botviolwhitelistrate = 0
		self._botviolwhitelistlog = 0
		self._botviolwhitelistlograte = 0
		self._botviolblacklist = 0
		self._botviolblacklistrate = 0
		self._botviolblacklistlog = 0
		self._botviolblacklistlograte = 0
		self._botviolblacklistdrop = 0
		self._botviolblacklistdroprate = 0
		self._botviolblacklistreset = 0
		self._botviolblacklistresetrate = 0
		self._botviolblacklistredirect = 0
		self._botviolblacklistredirectrate = 0
		self._botviolratelimit = 0
		self._botviolratelimitrate = 0
		self._botviolratelimitlog = 0
		self._botviolratelimitlograte = 0
		self._botviolratelimitdrop = 0
		self._botviolratelimitdroprate = 0
		self._botviolratelimitredirect = 0
		self._botviolratelimitredirectrate = 0
		self._botviolratelimitreset = 0
		self._botviolratelimitresetrate = 0
		self._botviolstaticsignature = 0
		self._botviolstaticsignaturerate = 0
		self._botviolstaticsignaturelog = 0
		self._botviolstaticsignaturelograte = 0
		self._botviolstaticsignaturedrop = 0
		self._botviolstaticsignaturedroprate = 0
		self._botviolstaticsignatureredirect = 0
		self._botviolstaticsignatureredirectrate = 0
		self._botviolstaticsignaturereset = 0
		self._botviolstaticsignatureresetrate = 0
		self._botvioltps = 0
		self._botvioltpsrate = 0
		self._botvioltpslog = 0
		self._botvioltpslograte = 0
		self._botvioltpsdrop = 0
		self._botvioltpsdroprate = 0
		self._botvioltpsredirect = 0
		self._botvioltpsredirectrate = 0
		self._botvioltpsreset = 0
		self._botvioltpsresetrate = 0
		self._botvioltpscaptcha = 0
		self._botvioltpscaptcharate = 0
		self._botviolcaptcha = 0
		self._botviolcaptcharate = 0
		self._botviolcaptchalog = 0
		self._botviolcaptchalograte = 0
		self._botviolcaptchadrop = 0
		self._botviolcaptchadroprate = 0
		self._botviolcaptcharedirect = 0
		self._botviolcaptcharedirectrate = 0
		self._botviolcaptchareset = 0
		self._botviolcaptcharesetrate = 0
		self._botvioltrap = 0
		self._botvioltraprate = 0
		self._botvioltraplog = 0
		self._botvioltraplograte = 0
		self._botvioltrapdrop = 0
		self._botvioltrapdroprate = 0
		self._botvioltrapredirect = 0
		self._botvioltrapredirectrate = 0
		self._botvioltrapreset = 0
		self._botvioltrapresetrate = 0

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
	def botviolipreputationlograte(self) :
		r"""Rate (/s) counter for botviolipreputationlog.
		"""
		try :
			return self._botviolipreputationlograte
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturereset(self) :
		r"""Number of static signature violations requests reset by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolstaticsignaturereset
		except Exception as e:
			raise e

	@property
	def botvioltps(self) :
		r"""Number of tps violations seen by the Bot Management.
		"""
		try :
			return self._botvioltps
		except Exception as e:
			raise e

	@property
	def botvioltraplog(self) :
		r"""Number of trap violations logged by the Bot Management.
		"""
		try :
			return self._botvioltraplog
		except Exception as e:
			raise e

	@property
	def botviolipreputation(self) :
		r"""Number of ip reputation violations seen by the Bot Management.
		"""
		try :
			return self._botviolipreputation
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirectrate(self) :
		r"""Rate (/s) counter for botviolblacklistredirect.
		"""
		try :
			return self._botviolblacklistredirectrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturedroprate(self) :
		r"""Rate (/s) counter for botviolstaticsignaturedrop.
		"""
		try :
			return self._botviolstaticsignaturedroprate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlog(self) :
		r"""Number of white list violations logged by the Bot Management.
		"""
		try :
			return self._botviolwhitelistlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintrate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprint.
		"""
		try :
			return self._botvioldevicefingerprintrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirectrate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintredirect.
		"""
		try :
			return self._botvioldevicefingerprintredirectrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitlograte(self) :
		r"""Rate (/s) counter for botviolratelimitlog.
		"""
		try :
			return self._botviolratelimitlograte
		except Exception as e:
			raise e

	@property
	def botvioltrapredirectrate(self) :
		r"""Rate (/s) counter for botvioltrapredirect.
		"""
		try :
			return self._botvioltrapredirectrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitdroprate(self) :
		r"""Rate (/s) counter for botviolratelimitdrop.
		"""
		try :
			return self._botviolratelimitdroprate
		except Exception as e:
			raise e

	@property
	def botvioltpsrate(self) :
		r"""Rate (/s) counter for botvioltps.
		"""
		try :
			return self._botvioltpsrate
		except Exception as e:
			raise e

	@property
	def botviolblacklistlograte(self) :
		r"""Rate (/s) counter for botviolblacklistlog.
		"""
		try :
			return self._botviolblacklistlograte
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirect(self) :
		r"""Number of black list violations redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolblacklistredirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintcaptcha(self) :
		r"""Number of device fingerprint violations requests for which CAPTCHA challenge was sent.
		"""
		try :
			return self._botvioldevicefingerprintcaptcha
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelog(self) :
		r"""Number of static signature violations logged by the Bot Management.
		"""
		try :
			return self._botviolstaticsignaturelog
		except Exception as e:
			raise e

	@property
	def botvioltpscaptcharate(self) :
		r"""Rate (/s) counter for botvioltpscaptcha.
		"""
		try :
			return self._botvioltpscaptcharate
		except Exception as e:
			raise e

	@property
	def botviolcaptchadroprate(self) :
		r"""Rate (/s) counter for botviolcaptchadrop.
		"""
		try :
			return self._botviolcaptchadroprate
		except Exception as e:
			raise e

	@property
	def botresponsesrate(self) :
		r"""Rate (/s) counter for botresponses.
		"""
		try :
			return self._botresponsesrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirectrate(self) :
		r"""Rate (/s) counter for botviolstaticsignatureredirect.
		"""
		try :
			return self._botviolstaticsignatureredirectrate
		except Exception as e:
			raise e

	@property
	def botviolcaptcharedirectrate(self) :
		r"""Rate (/s) counter for botviolcaptcharedirect.
		"""
		try :
			return self._botviolcaptcharedirectrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintcaptcharate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintcaptcha.
		"""
		try :
			return self._botvioldevicefingerprintcaptcharate
		except Exception as e:
			raise e

	@property
	def botviolipreputationdroprate(self) :
		r"""Rate (/s) counter for botviolipreputationdrop.
		"""
		try :
			return self._botviolipreputationdroprate
		except Exception as e:
			raise e

	@property
	def botresbytesrate(self) :
		r"""Rate (/s) counter for botresbytes.
		"""
		try :
			return self._botresbytesrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitrate(self) :
		r"""Rate (/s) counter for botviolratelimit.
		"""
		try :
			return self._botviolratelimitrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationlog(self) :
		r"""Number of ip reputation violations logged by the Bot Management.
		"""
		try :
			return self._botviolipreputationlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdrop(self) :
		r"""Number of device fingerprint violations dropped by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprintdrop
		except Exception as e:
			raise e

	@property
	def botreqbytes(self) :
		r"""Number of bytes transfered for requests.
		"""
		try :
			return self._botreqbytes
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelograte(self) :
		r"""Rate (/s) counter for botviolstaticsignaturelog.
		"""
		try :
			return self._botviolstaticsignaturelograte
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturerate(self) :
		r"""Rate (/s) counter for botviolstaticsignature.
		"""
		try :
			return self._botviolstaticsignaturerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationcaptcharate(self) :
		r"""Rate (/s) counter for botviolipreputationcaptcha.
		"""
		try :
			return self._botviolipreputationcaptcharate
		except Exception as e:
			raise e

	@property
	def botviolcaptchareset(self) :
		r"""Number of Captcha challenge failures reset by the Bot Management.
		"""
		try :
			return self._botviolcaptchareset
		except Exception as e:
			raise e

	@property
	def botviolipreputationreset(self) :
		r"""Number of ip reputation violations reset by the Bot Management.
		"""
		try :
			return self._botviolipreputationreset
		except Exception as e:
			raise e

	@property
	def botviolratelimitdrop(self) :
		r"""Number of rate limiting violations dropped by the Bot Management.
		"""
		try :
			return self._botviolratelimitdrop
		except Exception as e:
			raise e

	@property
	def botvioltpslograte(self) :
		r"""Rate (/s) counter for botvioltpslog.
		"""
		try :
			return self._botvioltpslograte
		except Exception as e:
			raise e

	@property
	def botvioltpsresetrate(self) :
		r"""Rate (/s) counter for botvioltpsreset.
		"""
		try :
			return self._botvioltpsresetrate
		except Exception as e:
			raise e

	@property
	def botrequests(self) :
		r"""HTTP/HTTPS requests sent to your protected web servers via the Bot Management.
		"""
		try :
			return self._botrequests
		except Exception as e:
			raise e

	@property
	def botviolblacklistrate(self) :
		r"""Rate (/s) counter for botviolblacklist.
		"""
		try :
			return self._botviolblacklistrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirectrate(self) :
		r"""Rate (/s) counter for botviolipreputationredirect.
		"""
		try :
			return self._botviolipreputationredirectrate
		except Exception as e:
			raise e

	@property
	def botvioltraplograte(self) :
		r"""Rate (/s) counter for botvioltraplog.
		"""
		try :
			return self._botvioltraplograte
		except Exception as e:
			raise e

	@property
	def botviolcaptcharedirect(self) :
		r"""Number of Captcha challenge failures redirected by the Bot Management.
		"""
		try :
			return self._botviolcaptcharedirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdroprate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintdrop.
		"""
		try :
			return self._botvioldevicefingerprintdroprate
		except Exception as e:
			raise e

	@property
	def botlograte(self) :
		r"""Rate (/s) counter for bottotallog.
		"""
		try :
			return self._botlograte
		except Exception as e:
			raise e

	@property
	def botvioltrapredirect(self) :
		r"""Number of trap violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botvioltrapredirect
		except Exception as e:
			raise e

	@property
	def botvioltpsdrop(self) :
		r"""Number of tps violations dropped by the Bot Management.
		"""
		try :
			return self._botvioltpsdrop
		except Exception as e:
			raise e

	@property
	def botvioltrapreset(self) :
		r"""Number of trap violations reset by the Bot Management.
		"""
		try :
			return self._botvioltrapreset
		except Exception as e:
			raise e

	@property
	def botviolratelimit(self) :
		r"""Number of rate limiting violations seen by the Bot Management.
		"""
		try :
			return self._botviolratelimit
		except Exception as e:
			raise e

	@property
	def botviolblacklistdroprate(self) :
		r"""Rate (/s) counter for botviolblacklistdrop.
		"""
		try :
			return self._botviolblacklistdroprate
		except Exception as e:
			raise e

	@property
	def botviolcaptchadrop(self) :
		r"""Number of Captcha challenge failures dropped by the Bot Management.
		"""
		try :
			return self._botviolcaptchadrop
		except Exception as e:
			raise e

	@property
	def botviolipreputationrate(self) :
		r"""Rate (/s) counter for botviolipreputation.
		"""
		try :
			return self._botviolipreputationrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirect(self) :
		r"""Number of static signature violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolstaticsignatureredirect
		except Exception as e:
			raise e

	@property
	def botvioltpsreset(self) :
		r"""Number of tps violations reset by the Bot Management.
		"""
		try :
			return self._botvioltpsreset
		except Exception as e:
			raise e

	@property
	def botvioltpsredirect(self) :
		r"""Number of tps violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botvioltpsredirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintlograte(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintlog.
		"""
		try :
			return self._botvioldevicefingerprintlograte
		except Exception as e:
			raise e

	@property
	def botresponses(self) :
		r"""HTTP/HTTPS responses sent by your protected web servers via the Bot Management.
		"""
		try :
			return self._botresponses
		except Exception as e:
			raise e

	@property
	def botvioltpsredirectrate(self) :
		r"""Rate (/s) counter for botvioltpsredirect.
		"""
		try :
			return self._botvioltpsredirectrate
		except Exception as e:
			raise e

	@property
	def botviolcaptchalograte(self) :
		r"""Rate (/s) counter for botviolcaptchalog.
		"""
		try :
			return self._botviolcaptchalograte
		except Exception as e:
			raise e

	@property
	def botvioltrapdrop(self) :
		r"""Number of trap violations dropped by the Bot Management.
		"""
		try :
			return self._botvioltrapdrop
		except Exception as e:
			raise e

	@property
	def botviolblacklistreset(self) :
		r"""Number of black list violations reset by the Bot Management.
		"""
		try :
			return self._botviolblacklistreset
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirectrate(self) :
		r"""Rate (/s) counter for botviolratelimitredirect.
		"""
		try :
			return self._botviolratelimitredirectrate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlograte(self) :
		r"""Rate (/s) counter for botviolwhitelistlog.
		"""
		try :
			return self._botviolwhitelistlograte
		except Exception as e:
			raise e

	@property
	def botvioltpsdroprate(self) :
		r"""Rate (/s) counter for botvioltpsdrop.
		"""
		try :
			return self._botvioltpsdroprate
		except Exception as e:
			raise e

	@property
	def botviolblacklistdrop(self) :
		r"""Number of black list violations dropped by the Bot Management.
		"""
		try :
			return self._botviolblacklistdrop
		except Exception as e:
			raise e

	@property
	def botviolcaptcha(self) :
		r"""Number of Captcha challenge failures seen by the Bot Management.
		"""
		try :
			return self._botviolcaptcha
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirect(self) :
		r"""Number of ip reputation violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolipreputationredirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintreset(self) :
		r"""Number of device fingerprint violations reset by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprintreset
		except Exception as e:
			raise e

	@property
	def botvioltpscaptcha(self) :
		r"""Number of TPS violations requests for which CAPTCHA challenge was sent.
		"""
		try :
			return self._botvioltpscaptcha
		except Exception as e:
			raise e

	@property
	def botviolipreputationdrop(self) :
		r"""Number of ip reputation violations dropped by the Bot Management.
		"""
		try :
			return self._botviolipreputationdrop
		except Exception as e:
			raise e

	@property
	def botresetrate(self) :
		r"""Rate (/s) counter for bottotalreset.
		"""
		try :
			return self._botresetrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignature(self) :
		r"""Number of static signature violations seen by the Bot Management.
		"""
		try :
			return self._botviolstaticsignature
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturedrop(self) :
		r"""Number of static signature violations dropped by the Bot Management.
		"""
		try :
			return self._botviolstaticsignaturedrop
		except Exception as e:
			raise e

	@property
	def bottotalredirect(self) :
		r"""Total number of redirects by the bot management.
		"""
		try :
			return self._bottotalredirect
		except Exception as e:
			raise e

	@property
	def bottotalreset(self) :
		r"""Total number of resets by the bot management.
		"""
		try :
			return self._bottotalreset
		except Exception as e:
			raise e

	@property
	def botviolratelimitreset(self) :
		r"""Number of rate limiting violations reset by the Bot Management.
		"""
		try :
			return self._botviolratelimitreset
		except Exception as e:
			raise e

	@property
	def botvioltrap(self) :
		r"""Number of trap violations seen by the Bot Management.
		"""
		try :
			return self._botvioltrap
		except Exception as e:
			raise e

	@property
	def botreqbytesrate(self) :
		r"""Rate (/s) counter for botreqbytes.
		"""
		try :
			return self._botreqbytesrate
		except Exception as e:
			raise e

	@property
	def botresbytes(self) :
		r"""Number of bytes transfered for responses.
		"""
		try :
			return self._botresbytes
		except Exception as e:
			raise e

	@property
	def botviolcaptcharate(self) :
		r"""Rate (/s) counter for botviolcaptcha.
		"""
		try :
			return self._botviolcaptcharate
		except Exception as e:
			raise e

	@property
	def botdroprate(self) :
		r"""Rate (/s) counter for bottotaldrop.
		"""
		try :
			return self._botdroprate
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirect(self) :
		r"""Number of rate limiting violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolratelimitredirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintresetrate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintreset.
		"""
		try :
			return self._botvioldevicefingerprintresetrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitlog(self) :
		r"""Number of rate limiting violations logged by the Bot Management.
		"""
		try :
			return self._botviolratelimitlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintlog(self) :
		r"""Number of device fingerprint violations logged by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprintlog
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureresetrate(self) :
		r"""Rate (/s) counter for botviolstaticsignaturereset.
		"""
		try :
			return self._botviolstaticsignatureresetrate
		except Exception as e:
			raise e

	@property
	def botvioltrapresetrate(self) :
		r"""Rate (/s) counter for botvioltrapreset.
		"""
		try :
			return self._botvioltrapresetrate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistrate(self) :
		r"""Rate (/s) counter for botviolwhitelist.
		"""
		try :
			return self._botviolwhitelistrate
		except Exception as e:
			raise e

	@property
	def botviolwhitelist(self) :
		r"""Number of white list violations seen by the Bot Management.
		"""
		try :
			return self._botviolwhitelist
		except Exception as e:
			raise e

	@property
	def botredirectrate(self) :
		r"""Rate (/s) counter for bottotalredirect.
		"""
		try :
			return self._botredirectrate
		except Exception as e:
			raise e

	@property
	def botviolblacklistlog(self) :
		r"""Number of black list violations logged by the Bot Management.
		"""
		try :
			return self._botviolblacklistlog
		except Exception as e:
			raise e

	@property
	def botvioltpslog(self) :
		r"""Number of tps violations logged by the Bot Management.
		"""
		try :
			return self._botvioltpslog
		except Exception as e:
			raise e

	@property
	def botviolblacklist(self) :
		r"""Number of black list violations seen by the Bot Management.
		"""
		try :
			return self._botviolblacklist
		except Exception as e:
			raise e

	@property
	def botrequestsrate(self) :
		r"""Rate (/s) counter for botrequests.
		"""
		try :
			return self._botrequestsrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationresetrate(self) :
		r"""Rate (/s) counter for botviolipreputationreset.
		"""
		try :
			return self._botviolipreputationresetrate
		except Exception as e:
			raise e

	@property
	def botviolcaptcharesetrate(self) :
		r"""Rate (/s) counter for botviolcaptchareset.
		"""
		try :
			return self._botviolcaptcharesetrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationcaptcha(self) :
		r"""Number of ip reputation violations requests for which CAPTCHA challenge was sent.
		"""
		try :
			return self._botviolipreputationcaptcha
		except Exception as e:
			raise e

	@property
	def botvioltrapdroprate(self) :
		r"""Rate (/s) counter for botvioltrapdrop.
		"""
		try :
			return self._botvioltrapdroprate
		except Exception as e:
			raise e

	@property
	def botviolcaptchalog(self) :
		r"""Number of Captcha challenge failures logged by the Bot Management.
		"""
		try :
			return self._botviolcaptchalog
		except Exception as e:
			raise e

	@property
	def botvioltraprate(self) :
		r"""Rate (/s) counter for botvioltrap.
		"""
		try :
			return self._botvioltraprate
		except Exception as e:
			raise e

	@property
	def bottotallog(self) :
		r"""Total number of logs by the bot management.
		"""
		try :
			return self._bottotallog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprint(self) :
		r"""Number of device fingerprint violations seen by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprint
		except Exception as e:
			raise e

	@property
	def bottotaldrop(self) :
		r"""Total number of drops by the bot management.
		"""
		try :
			return self._bottotaldrop
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirect(self) :
		r"""Number of device fingerprint violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botvioldevicefingerprintredirect
		except Exception as e:
			raise e

	@property
	def botviolblacklistresetrate(self) :
		r"""Rate (/s) counter for botviolblacklistreset.
		"""
		try :
			return self._botviolblacklistresetrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitresetrate(self) :
		r"""Rate (/s) counter for botviolratelimitreset.
		"""
		try :
			return self._botviolratelimitresetrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bot_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bot
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
		r""" Use this API to fetch the statistics of all bot_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = bot_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class bot_response(base_response) :
	def __init__(self, length=1) :
		self.bot = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bot = [bot_stats() for _ in range(length)]

