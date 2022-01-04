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

class botprofile_stats(base_resource) :
	r""" Statistics for Bot profile resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._botrequestsperprofile = 0
		self._botrequestsperprofilerate = 0
		self._botreqbytesperprofile = 0
		self._botreqbytesperprofilerate = 0
		self._botresponsesperprofile = 0
		self._botresponsesperprofilerate = 0
		self._botresbytesperprofile = 0
		self._botresbytesperprofilerate = 0
		self._bottotallogprofile = 0
		self._botlogprofilerate = 0
		self._bottotaldropprofile = 0
		self._botdropprofilerate = 0
		self._bottotalredirectprofile = 0
		self._botredirectprofilerate = 0
		self._bottotalresetprofile = 0
		self._botresetprofilerate = 0
		self._botvioldevicefingerprintprofile = 0
		self._botvioldevicefingerprintprofilerate = 0
		self._botvioldevicefingerprintlogprofile = 0
		self._botvioldevicefingerprintlogprofilerate = 0
		self._botvioldevicefingerprintdropprofile = 0
		self._botvioldevicefingerprintdropprofilerate = 0
		self._botvioldevicefingerprintredirectprofile = 0
		self._botvioldevicefingerprintredirectprofilerate = 0
		self._botvioldevicefingerprintcaptchaprofile = 0
		self._botvioldevicefingerprintcaptchaprofilerate = 0
		self._botvioldevicefingerprintresetprofile = 0
		self._botvioldevicefingerprintresetprofilerate = 0
		self._botviolipreputationprofile = 0
		self._botviolipreputationprofilerate = 0
		self._botviolipreputationlogprofile = 0
		self._botviolipreputationlogprofilerate = 0
		self._botviolipreputationdropprofile = 0
		self._botviolipreputationdropprofilerate = 0
		self._botviolipreputationredirectprofile = 0
		self._botviolipreputationredirectprofilerate = 0
		self._botviolipreputationcaptchaprofile = 0
		self._botviolipreputationcaptchaprofilerate = 0
		self._botviolipreputationresetprofile = 0
		self._botviolipreputationresetprofilerate = 0
		self._botviolwhitelistprofile = 0
		self._botviolwhitelistprofilerate = 0
		self._botviolwhitelistlogprofile = 0
		self._botviolwhitelistlogprofilerate = 0
		self._botviolblacklistprofile = 0
		self._botviolblacklistprofilerate = 0
		self._botviolblacklistlogprofile = 0
		self._botviolblacklistlogprofilerate = 0
		self._botviolblacklistdropprofile = 0
		self._botviolblacklistdropprofilerate = 0
		self._botviolblacklistresetprofile = 0
		self._botviolblacklistresetprofilerate = 0
		self._botviolblacklistredirectprofile = 0
		self._botviolblacklistredirectprofilerate = 0
		self._botviolratelimitprofile = 0
		self._botviolratelimitprofilerate = 0
		self._botviolratelimitlogprofile = 0
		self._botviolratelimitlogprofilerate = 0
		self._botviolratelimitdropprofile = 0
		self._botviolratelimitdropprofilerate = 0
		self._botviolratelimitredirectprofile = 0
		self._botviolratelimitredirectprofilerate = 0
		self._botviolratelimitresetprofile = 0
		self._botviolratelimitresetprofilerate = 0
		self._botviolstaticsignatureprofile = 0
		self._botviolstaticsignatureprofilerate = 0
		self._botviolstaticsignaturelogprofile = 0
		self._botviolstaticsignaturelogprofilerate = 0
		self._botviolstaticsignaturedropprofile = 0
		self._botviolstaticsignaturedropprofilerate = 0
		self._botviolstaticsignatureredirectprofile = 0
		self._botviolstaticsignatureredirectprofilerate = 0
		self._botviolstaticsignatureresetprofile = 0
		self._botviolstaticsignatureresetprofilerate = 0
		self._botvioltpsprofile = 0
		self._botvioltpsprofilerate = 0
		self._botvioltpslogprofile = 0
		self._botvioltpslogprofilerate = 0
		self._botvioltpsdropprofile = 0
		self._botvioltpsdropprofilerate = 0
		self._botvioltpsredirectprofile = 0
		self._botvioltpsredirectprofilerate = 0
		self._botvioltpsresetprofile = 0
		self._botvioltpsresetprofilerate = 0
		self._botvioltpscaptchaprofile = 0
		self._botvioltpscaptchaprofilerate = 0
		self._botviolcaptchaprofile = 0
		self._botviolcaptchaprofilerate = 0
		self._botviolcaptchalogprofile = 0
		self._botviolcaptchalogprofilerate = 0
		self._botviolcaptchadropprofile = 0
		self._botviolcaptchadropprofilerate = 0
		self._botviolcaptcharedirectprofile = 0
		self._botviolcaptcharedirectprofilerate = 0
		self._botviolcaptcharesetprofile = 0
		self._botviolcaptcharesetprofilerate = 0
		self._botvioltrapprofile = 0
		self._botvioltrapprofilerate = 0
		self._botvioltraplogprofile = 0
		self._botvioltraplogprofilerate = 0
		self._botvioltrapdropprofile = 0
		self._botvioltrapdropprofilerate = 0
		self._botvioltrapredirectprofile = 0
		self._botvioltrapredirectprofilerate = 0
		self._botvioltrapresetprofile = 0
		self._botvioltrapresetprofilerate = 0

	@property
	def name(self) :
		r"""Name of the bot profile.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the bot profile.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

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
	def botvioldevicefingerprintlogprofile(self) :
		r"""Number of device fingerprint violations logged by the Bot profile.
		"""
		try :
			return self._botvioldevicefingerprintlogprofile
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirectprofile(self) :
		r"""Number of ip reputation violations requests redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botviolipreputationredirectprofile
		except Exception as e:
			raise e

	@property
	def botviolratelimitresetprofilerate(self) :
		r"""Rate (/s) counter for botviolratelimitresetprofile.
		"""
		try :
			return self._botviolratelimitresetprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturedropprofile(self) :
		r"""Number of static signatutre violations dropped by the Bot profile.
		"""
		try :
			return self._botviolstaticsignaturedropprofile
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureresetprofile(self) :
		r"""Number of static signatutre violations reset by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botviolstaticsignatureresetprofile
		except Exception as e:
			raise e

	@property
	def botviolratelimitlogprofilerate(self) :
		r"""Rate (/s) counter for botviolratelimitlogprofile.
		"""
		try :
			return self._botviolratelimitlogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationcaptchaprofile(self) :
		r"""Number of ip reputation violation requests for which CAPTCHA challenge was sent due to Bot profile.
		"""
		try :
			return self._botviolipreputationcaptchaprofile
		except Exception as e:
			raise e

	@property
	def botredirectprofilerate(self) :
		r"""Rate (/s) counter for bottotalredirectprofile.
		"""
		try :
			return self._botredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botviolratelimitlogprofile(self) :
		r"""Number of rate limiting violations logged by the Bot profile.
		"""
		try :
			return self._botviolratelimitlogprofile
		except Exception as e:
			raise e

	@property
	def botviolipreputationprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationprofile.
		"""
		try :
			return self._botviolipreputationprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdropprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintdropprofile.
		"""
		try :
			return self._botvioldevicefingerprintdropprofilerate
		except Exception as e:
			raise e

	@property
	def botviolblacklistresetprofile(self) :
		r"""Number of black list violations reset by the Bot profile.
		"""
		try :
			return self._botviolblacklistresetprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirectprofile(self) :
		r"""Number of black list violations redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botviolblacklistredirectprofile
		except Exception as e:
			raise e

	@property
	def botvioltraplogprofilerate(self) :
		r"""Rate (/s) counter for botvioltraplogprofile.
		"""
		try :
			return self._botvioltraplogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolratelimitprofile(self) :
		r"""Number of rate limiting violations seen by the Bot profile.
		"""
		try :
			return self._botviolratelimitprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistdropprofile(self) :
		r"""Number of black list violations dropped by the Bot profile.
		"""
		try :
			return self._botviolblacklistdropprofile
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirectprofilerate(self) :
		r"""Rate (/s) counter for botviolratelimitredirectprofile.
		"""
		try :
			return self._botviolratelimitredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botreqbytesperprofilerate(self) :
		r"""Rate (/s) counter for botreqbytesperprofile.
		"""
		try :
			return self._botreqbytesperprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltrapredirectprofilerate(self) :
		r"""Rate (/s) counter for botvioltrapredirectprofile.
		"""
		try :
			return self._botvioltrapredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationprofile(self) :
		r"""Number of ip reputation violations seen by the Bot profile.
		"""
		try :
			return self._botviolipreputationprofile
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelogprofilerate(self) :
		r"""Rate (/s) counter for botviolstaticsignaturelogprofile.
		"""
		try :
			return self._botviolstaticsignaturelogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelogprofile(self) :
		r"""Number of static signatutre violations logged by the Bot profile.
		"""
		try :
			return self._botviolstaticsignaturelogprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirectprofilerate(self) :
		r"""Rate (/s) counter for botviolblacklistredirectprofile.
		"""
		try :
			return self._botviolblacklistredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botresbytesperprofilerate(self) :
		r"""Rate (/s) counter for botresbytesperprofile.
		"""
		try :
			return self._botresbytesperprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirectprofile(self) :
		r"""Number of static signatutre violations redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botviolstaticsignatureredirectprofile
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureresetprofilerate(self) :
		r"""Rate (/s) counter for botviolstaticsignatureresetprofile.
		"""
		try :
			return self._botviolstaticsignatureresetprofilerate
		except Exception as e:
			raise e

	@property
	def botviolblacklistresetprofilerate(self) :
		r"""Rate (/s) counter for botviolblacklistresetprofile.
		"""
		try :
			return self._botviolblacklistresetprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirectprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationredirectprofile.
		"""
		try :
			return self._botviolipreputationredirectprofilerate
		except Exception as e:
			raise e

	@property
	def bottotaldropprofile(self) :
		r"""Total number of drops by the Bot profile.
		"""
		try :
			return self._bottotaldropprofile
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureprofilerate(self) :
		r"""Rate (/s) counter for botviolstaticsignatureprofile.
		"""
		try :
			return self._botviolstaticsignatureprofilerate
		except Exception as e:
			raise e

	@property
	def bottotallogprofile(self) :
		r"""Total number of logs by the Bot profile.
		"""
		try :
			return self._bottotallogprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptchadropprofilerate(self) :
		r"""Rate (/s) counter for botviolcaptchadropprofile.
		"""
		try :
			return self._botviolcaptchadropprofilerate
		except Exception as e:
			raise e

	@property
	def botviolratelimitdropprofilerate(self) :
		r"""Rate (/s) counter for botviolratelimitdropprofile.
		"""
		try :
			return self._botviolratelimitdropprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintprofile(self) :
		r"""Number of device fingerprint violations seen by the Bot profile.
		"""
		try :
			return self._botvioldevicefingerprintprofile
		except Exception as e:
			raise e

	@property
	def botviolipreputationresetprofile(self) :
		r"""Number of ip reputation violations reset by the Bot profile.
		"""
		try :
			return self._botviolipreputationresetprofile
		except Exception as e:
			raise e

	@property
	def botviolratelimitresetprofile(self) :
		r"""Number of rate limiting violations reset by the Bot profile.
		"""
		try :
			return self._botviolratelimitresetprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptchaprofile(self) :
		r"""Number of Captcha challenge failures seen by the Bot profile.
		"""
		try :
			return self._botviolcaptchaprofile
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintresetprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintresetprofile.
		"""
		try :
			return self._botvioldevicefingerprintresetprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltrapdropprofile(self) :
		r"""Number of trap violations dropped by the Bot profile.
		"""
		try :
			return self._botvioltrapdropprofile
		except Exception as e:
			raise e

	@property
	def botresbytesperprofile(self) :
		r"""Number of bytes transfered for responses.
		"""
		try :
			return self._botresbytesperprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptchalogprofile(self) :
		r"""Number of Captcha challenge failures logged by the Bot profile.
		"""
		try :
			return self._botviolcaptchalogprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistlogprofilerate(self) :
		r"""Rate (/s) counter for botviolblacklistlogprofile.
		"""
		try :
			return self._botviolblacklistlogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolcaptchadropprofile(self) :
		r"""Number of Captcha challenge failures dropped by the Bot profile.
		"""
		try :
			return self._botviolcaptchadropprofile
		except Exception as e:
			raise e

	@property
	def botvioltrapdropprofilerate(self) :
		r"""Rate (/s) counter for botvioltrapdropprofile.
		"""
		try :
			return self._botvioltrapdropprofilerate
		except Exception as e:
			raise e

	@property
	def botviolratelimitdropprofile(self) :
		r"""Number of rate limiting violations dropped by the Bot profile.
		"""
		try :
			return self._botviolratelimitdropprofile
		except Exception as e:
			raise e

	@property
	def botrequestsperprofile(self) :
		r"""HTTP/HTTPS requests sent to your protected web servers via the Bot profile.
		"""
		try :
			return self._botrequestsperprofile
		except Exception as e:
			raise e

	@property
	def botdropprofilerate(self) :
		r"""Rate (/s) counter for bottotaldropprofile.
		"""
		try :
			return self._botdropprofilerate
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirectprofile(self) :
		r"""Number of rate limiting violations requests redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botviolratelimitredirectprofile
		except Exception as e:
			raise e

	@property
	def botvioltpsdropprofile(self) :
		r"""Number of tps violations dropped by the Bot profile.
		"""
		try :
			return self._botvioltpsdropprofile
		except Exception as e:
			raise e

	@property
	def botlogprofilerate(self) :
		r"""Rate (/s) counter for bottotallogprofile.
		"""
		try :
			return self._botlogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolblacklistprofilerate(self) :
		r"""Rate (/s) counter for botviolblacklistprofile.
		"""
		try :
			return self._botviolblacklistprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturedropprofilerate(self) :
		r"""Rate (/s) counter for botviolstaticsignaturedropprofile.
		"""
		try :
			return self._botviolstaticsignaturedropprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpsprofile(self) :
		r"""Number of tps violations seen by the Bot profile.
		"""
		try :
			return self._botvioltpsprofile
		except Exception as e:
			raise e

	@property
	def botreqbytesperprofile(self) :
		r"""Number of bytes transfered for requests.
		"""
		try :
			return self._botreqbytesperprofile
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintprofile.
		"""
		try :
			return self._botvioldevicefingerprintprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirectprofilerate(self) :
		r"""Rate (/s) counter for botviolstaticsignatureredirectprofile.
		"""
		try :
			return self._botviolstaticsignatureredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirectprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintredirectprofile.
		"""
		try :
			return self._botvioldevicefingerprintredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationlogprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationlogprofile.
		"""
		try :
			return self._botviolipreputationlogprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirectprofile(self) :
		r"""Number of device fingerprint violations requests redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botvioldevicefingerprintredirectprofile
		except Exception as e:
			raise e

	@property
	def botvioltrapresetprofile(self) :
		r"""Number of trap violations reset by the Bot profile.
		"""
		try :
			return self._botvioltrapresetprofile
		except Exception as e:
			raise e

	@property
	def botviolwhitelistprofilerate(self) :
		r"""Rate (/s) counter for botviolwhitelistprofile.
		"""
		try :
			return self._botviolwhitelistprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpsresetprofile(self) :
		r"""Number of tps violations reset by the Bot profile.
		"""
		try :
			return self._botvioltpsresetprofile
		except Exception as e:
			raise e

	@property
	def botresponsesperprofilerate(self) :
		r"""Rate (/s) counter for botresponsesperprofile.
		"""
		try :
			return self._botresponsesperprofilerate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlogprofile(self) :
		r"""Number of white list violations logged by the Bot profile.
		"""
		try :
			return self._botviolwhitelistlogprofile
		except Exception as e:
			raise e

	@property
	def botviolipreputationlogprofile(self) :
		r"""Number of ip reputation violations logged by the Bot Profile.
		"""
		try :
			return self._botviolipreputationlogprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistlogprofile(self) :
		r"""Number of black list violations logged by the Bot profile.
		"""
		try :
			return self._botviolblacklistlogprofile
		except Exception as e:
			raise e

	@property
	def botrequestsperprofilerate(self) :
		r"""Rate (/s) counter for botrequestsperprofile.
		"""
		try :
			return self._botrequestsperprofilerate
		except Exception as e:
			raise e

	@property
	def botviolcaptcharedirectprofilerate(self) :
		r"""Rate (/s) counter for botviolcaptcharedirectprofile.
		"""
		try :
			return self._botviolcaptcharedirectprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationcaptchaprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationcaptchaprofile.
		"""
		try :
			return self._botviolipreputationcaptchaprofilerate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureprofile(self) :
		r"""Number of static signatutre violations seen by the Bot profile.
		"""
		try :
			return self._botviolstaticsignatureprofile
		except Exception as e:
			raise e

	@property
	def botvioltpscaptchaprofilerate(self) :
		r"""Rate (/s) counter for botvioltpscaptchaprofile.
		"""
		try :
			return self._botvioltpscaptchaprofilerate
		except Exception as e:
			raise e

	@property
	def botviolcaptchaprofilerate(self) :
		r"""Rate (/s) counter for botviolcaptchaprofile.
		"""
		try :
			return self._botviolcaptchaprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdropprofile(self) :
		r"""Number of device fingerprint violations dropped by the Bot profile.
		"""
		try :
			return self._botvioldevicefingerprintdropprofile
		except Exception as e:
			raise e

	@property
	def botviolblacklistprofile(self) :
		r"""Number of black list violations seen by the Bot profile.
		"""
		try :
			return self._botviolblacklistprofile
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintresetprofile(self) :
		r"""Number of device fingerprint violations reset by the Bot profile.
		"""
		try :
			return self._botvioldevicefingerprintresetprofile
		except Exception as e:
			raise e

	@property
	def botvioltraplogprofile(self) :
		r"""Number of trap violations logged by the Bot profile.
		"""
		try :
			return self._botvioltraplogprofile
		except Exception as e:
			raise e

	@property
	def botviolipreputationdropprofile(self) :
		r"""Number of ip reputation violations dropped by the Bot profile.
		"""
		try :
			return self._botviolipreputationdropprofile
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintcaptchaprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintcaptchaprofile.
		"""
		try :
			return self._botvioldevicefingerprintcaptchaprofilerate
		except Exception as e:
			raise e

	@property
	def botresponsesperprofile(self) :
		r"""HTTP/HTTPS responses sent by your protected web servers via the Bot profile.
		"""
		try :
			return self._botresponsesperprofile
		except Exception as e:
			raise e

	@property
	def botvioltrapredirectprofile(self) :
		r"""Number of trap violations requests redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botvioltrapredirectprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptchalogprofilerate(self) :
		r"""Rate (/s) counter for botviolcaptchalogprofile.
		"""
		try :
			return self._botviolcaptchalogprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpsredirectprofilerate(self) :
		r"""Rate (/s) counter for botvioltpsredirectprofile.
		"""
		try :
			return self._botvioltpsredirectprofilerate
		except Exception as e:
			raise e

	@property
	def botviolblacklistdropprofilerate(self) :
		r"""Rate (/s) counter for botviolblacklistdropprofile.
		"""
		try :
			return self._botviolblacklistdropprofilerate
		except Exception as e:
			raise e

	@property
	def bottotalresetprofile(self) :
		r"""Total number of resets by the Bot profile.
		"""
		try :
			return self._bottotalresetprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptcharesetprofilerate(self) :
		r"""Rate (/s) counter for botviolcaptcharesetprofile.
		"""
		try :
			return self._botviolcaptcharesetprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpslogprofilerate(self) :
		r"""Rate (/s) counter for botvioltpslogprofile.
		"""
		try :
			return self._botvioltpslogprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpsredirectprofile(self) :
		r"""Number of tps violations requests redirected by the Bot profile to a different Web page or web server.
		"""
		try :
			return self._botvioltpsredirectprofile
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintlogprofilerate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintlogprofile.
		"""
		try :
			return self._botvioldevicefingerprintlogprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationresetprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationresetprofile.
		"""
		try :
			return self._botviolipreputationresetprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpslogprofile(self) :
		r"""Number of tps violations logged by the Bot profile.
		"""
		try :
			return self._botvioltpslogprofile
		except Exception as e:
			raise e

	@property
	def bottotalredirectprofile(self) :
		r"""Total number of redirects by the Bot profile.
		"""
		try :
			return self._bottotalredirectprofile
		except Exception as e:
			raise e

	@property
	def botvioltpsdropprofilerate(self) :
		r"""Rate (/s) counter for botvioltpsdropprofile.
		"""
		try :
			return self._botvioltpsdropprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpsresetprofilerate(self) :
		r"""Rate (/s) counter for botvioltpsresetprofile.
		"""
		try :
			return self._botvioltpsresetprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltrapprofilerate(self) :
		r"""Rate (/s) counter for botvioltrapprofile.
		"""
		try :
			return self._botvioltrapprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltrapprofile(self) :
		r"""Number of trap violations seen by the Bot profile.
		"""
		try :
			return self._botvioltrapprofile
		except Exception as e:
			raise e

	@property
	def botviolcaptcharesetprofile(self) :
		r"""Number of Captcha challenge failures reset by the Bot profile.
		"""
		try :
			return self._botviolcaptcharesetprofile
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlogprofilerate(self) :
		r"""Rate (/s) counter for botviolwhitelistlogprofile.
		"""
		try :
			return self._botviolwhitelistlogprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltrapresetprofilerate(self) :
		r"""Rate (/s) counter for botvioltrapresetprofile.
		"""
		try :
			return self._botvioltrapresetprofilerate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintcaptchaprofile(self) :
		r"""Number of device fingerprint violation requests for which CAPTCHA challenge was sent due to Bot profile.
		"""
		try :
			return self._botvioldevicefingerprintcaptchaprofile
		except Exception as e:
			raise e

	@property
	def botresetprofilerate(self) :
		r"""Rate (/s) counter for bottotalresetprofile.
		"""
		try :
			return self._botresetprofilerate
		except Exception as e:
			raise e

	@property
	def botviolcaptcharedirectprofile(self) :
		r"""Number of Captcha challenge failures redirected by the Bot profile.
		"""
		try :
			return self._botviolcaptcharedirectprofile
		except Exception as e:
			raise e

	@property
	def botviolwhitelistprofile(self) :
		r"""Number of white list violations seen by the Bot profile.
		"""
		try :
			return self._botviolwhitelistprofile
		except Exception as e:
			raise e

	@property
	def botviolratelimitprofilerate(self) :
		r"""Rate (/s) counter for botviolratelimitprofile.
		"""
		try :
			return self._botviolratelimitprofilerate
		except Exception as e:
			raise e

	@property
	def botvioltpscaptchaprofile(self) :
		r"""Number of tps violation requests for which CAPTCHA challenge was sent due to Bot profile.
		"""
		try :
			return self._botvioltpscaptchaprofile
		except Exception as e:
			raise e

	@property
	def botvioltpsprofilerate(self) :
		r"""Rate (/s) counter for botvioltpsprofile.
		"""
		try :
			return self._botvioltpsprofilerate
		except Exception as e:
			raise e

	@property
	def botviolipreputationdropprofilerate(self) :
		r"""Rate (/s) counter for botviolipreputationdropprofile.
		"""
		try :
			return self._botviolipreputationdropprofilerate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botprofile_response, response, self.__class__.__name__.replace('_stats',''))
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all botprofile_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = botprofile_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class botprofile_response(base_response) :
	def __init__(self, length=1) :
		self.botprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botprofile = [botprofile_stats() for _ in range(length)]

