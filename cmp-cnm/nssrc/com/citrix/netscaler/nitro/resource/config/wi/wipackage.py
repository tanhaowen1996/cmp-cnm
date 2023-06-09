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

class wipackage(base_resource) :
	""" Configuration for Web Interface resource. """
	def __init__(self) :
		self._jre = None
		self._wi = None
		self._maxsites = None

	@property
	def jre(self) :
		r"""Complete path to the JRE tar file.
		You can use OpenJDK7 package for FreeBSD 8.x/amd64.The Java package can be downloaded from http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/amd64/8.4-RELEASE/packages/java/openjdk-7.17.02_2.tbz.<br/>Default value: "file://tmp/diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz"<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._jre
		except Exception as e:
			raise e

	@jre.setter
	def jre(self, jre) :
		r"""Complete path to the JRE tar file.
		You can use OpenJDK7 package for FreeBSD 8.x/amd64.The Java package can be downloaded from http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/amd64/amd64/8.4-RELEASE/packages/java/openjdk-7.17.02_2.tbz.<br/>Default value: "file://tmp/diablo-jdk-freebsd6.amd64.1.6.0.07.02.tbz"<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._jre = jre
		except Exception as e:
			raise e

	@property
	def wi(self) :
		r"""Complete path to the Web Interface tar file for installing the Web Interface on the Citrix ADC. This file includes Apache Tomcat Web server. The file name has the following format: nswi-<version number>.tgz (for example, nswi-1.5.tgz).<br/>Default value: "http://citrix.com/downloads/nswi-1.7.tgz"<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._wi
		except Exception as e:
			raise e

	@wi.setter
	def wi(self, wi) :
		r"""Complete path to the Web Interface tar file for installing the Web Interface on the Citrix ADC. This file includes Apache Tomcat Web server. The file name has the following format: nswi-<version number>.tgz (for example, nswi-1.5.tgz).<br/>Default value: "http://citrix.com/downloads/nswi-1.7.tgz"<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._wi = wi
		except Exception as e:
			raise e

	@property
	def maxsites(self) :
		r"""Maximum number of Web Interface sites that can be created on the Citrix ADC; changes the amount of RAM reserved for Web Interface usage; changing its value results in restart of Tomcat server and invalidates any existing Web Interface sessions.<br/>Possible values = 3, 25, 50, 100, 200, 500.
		"""
		try :
			return self._maxsites
		except Exception as e:
			raise e

	@maxsites.setter
	def maxsites(self, maxsites) :
		r"""Maximum number of Web Interface sites that can be created on the Citrix ADC; changes the amount of RAM reserved for Web Interface usage; changing its value results in restart of Tomcat server and invalidates any existing Web Interface sessions.<br/>Possible values = 3, 25, 50, 100, 200, 500
		"""
		try :
			self._maxsites = maxsites
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(wipackage_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.wipackage
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
	def Install(cls, client, resource) :
		r""" Use this API to Install wipackage.
		"""
		try :
			if type(resource) is not list :
				Installresource = wipackage()
				Installresource.jre = resource.jre
				Installresource.wi = resource.wi
				Installresource.maxsites = resource.maxsites
				return Installresource.perform_operation(client,"Install")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the wipackage resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = wipackage()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Maxsites:
		_3 = "3"
		_25 = "25"
		_50 = "50"
		_100 = "100"
		_200 = "200"
		_500 = "500"

class wipackage_response(base_response) :
	def __init__(self, length=1) :
		self.wipackage = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.wipackage = [wipackage() for _ in range(length)]

