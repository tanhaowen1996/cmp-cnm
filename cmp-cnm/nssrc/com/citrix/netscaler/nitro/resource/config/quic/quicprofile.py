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

class quicprofile(base_resource) :
	""" Configuration for QUIC profile resource. """
	def __init__(self) :
		self._name = None
		self._ackdelayexponent = None
		self._activeconnectionidlimit = None
		self._activeconnectionmigration = None
		self._congestionctrlalgorithm = None
		self._initialmaxdata = None
		self._initialmaxstreamdatabidilocal = None
		self._initialmaxstreamdatabidiremote = None
		self._initialmaxstreamdatauni = None
		self._initialmaxstreamsbidi = None
		self._initialmaxstreamsuni = None
		self._maxackdelay = None
		self._maxidletimeout = None
		self._maxudpdatagramsperburst = None
		self._maxudppayloadsize = None
		self._newtokenvalidityperiod = None
		self._retrytokenvalidityperiod = None
		self._statelessaddressvalidation = None
		self._refcnt = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the QUIC profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the QUIC profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ackdelayexponent(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, indicating an exponent that the remote QUIC endpoint should use, to decode the ACK Delay field in QUIC ACK frames sent by the Citrix ADC.<br/>Default value: 3<br/>Maximum length =  20.
		"""
		try :
			return self._ackdelayexponent
		except Exception as e:
			raise e

	@ackdelayexponent.setter
	def ackdelayexponent(self, ackdelayexponent) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, indicating an exponent that the remote QUIC endpoint should use, to decode the ACK Delay field in QUIC ACK frames sent by the Citrix ADC.<br/>Default value: 3<br/>Maximum length =  20
		"""
		try :
			self._ackdelayexponent = ackdelayexponent
		except Exception as e:
			raise e

	@property
	def activeconnectionidlimit(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum number of QUIC connection IDs from the remote QUIC endpoint, that the Citrix ADC is willing to store.<br/>Default value: 3<br/>Minimum length =  2<br/>Maximum length =  8.
		"""
		try :
			return self._activeconnectionidlimit
		except Exception as e:
			raise e

	@activeconnectionidlimit.setter
	def activeconnectionidlimit(self, activeconnectionidlimit) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum number of QUIC connection IDs from the remote QUIC endpoint, that the Citrix ADC is willing to store.<br/>Default value: 3<br/>Minimum length =  2<br/>Maximum length =  8
		"""
		try :
			self._activeconnectionidlimit = activeconnectionidlimit
		except Exception as e:
			raise e

	@property
	def activeconnectionmigration(self) :
		r"""Specify whether the Citrix ADC should allow the remote QUIC endpoint to perform active QUIC connection migration.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._activeconnectionmigration
		except Exception as e:
			raise e

	@activeconnectionmigration.setter
	def activeconnectionmigration(self, activeconnectionmigration) :
		r"""Specify whether the Citrix ADC should allow the remote QUIC endpoint to perform active QUIC connection migration.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._activeconnectionmigration = activeconnectionmigration
		except Exception as e:
			raise e

	@property
	def congestionctrlalgorithm(self) :
		r"""Specify the congestion control algorithm to be used for QUIC connections. The default congestion control algorithm is CUBIC.<br/>Default value: Default<br/>Possible values = Default, NewReno, CUBIC, BBR.
		"""
		try :
			return self._congestionctrlalgorithm
		except Exception as e:
			raise e

	@congestionctrlalgorithm.setter
	def congestionctrlalgorithm(self, congestionctrlalgorithm) :
		r"""Specify the congestion control algorithm to be used for QUIC connections. The default congestion control algorithm is CUBIC.<br/>Default value: Default<br/>Possible values = Default, NewReno, CUBIC, BBR
		"""
		try :
			self._congestionctrlalgorithm = congestionctrlalgorithm
		except Exception as e:
			raise e

	@property
	def initialmaxdata(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial value, in bytes, for the maximum amount of data that can be sent on a QUIC connection.<br/>Default value: 1048576<br/>Minimum length =  8192<br/>Maximum length =  67108864.
		"""
		try :
			return self._initialmaxdata
		except Exception as e:
			raise e

	@initialmaxdata.setter
	def initialmaxdata(self, initialmaxdata) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial value, in bytes, for the maximum amount of data that can be sent on a QUIC connection.<br/>Default value: 1048576<br/>Minimum length =  8192<br/>Maximum length =  67108864
		"""
		try :
			self._initialmaxdata = initialmaxdata
		except Exception as e:
			raise e

	@property
	def initialmaxstreamdatabidilocal(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for bidirectional QUIC streams initiated by the Citrix ADC.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608.
		"""
		try :
			return self._initialmaxstreamdatabidilocal
		except Exception as e:
			raise e

	@initialmaxstreamdatabidilocal.setter
	def initialmaxstreamdatabidilocal(self, initialmaxstreamdatabidilocal) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for bidirectional QUIC streams initiated by the Citrix ADC.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608
		"""
		try :
			self._initialmaxstreamdatabidilocal = initialmaxstreamdatabidilocal
		except Exception as e:
			raise e

	@property
	def initialmaxstreamdatabidiremote(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for bidirectional QUIC streams initiated by the remote QUIC endpoint.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608.
		"""
		try :
			return self._initialmaxstreamdatabidiremote
		except Exception as e:
			raise e

	@initialmaxstreamdatabidiremote.setter
	def initialmaxstreamdatabidiremote(self, initialmaxstreamdatabidiremote) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for bidirectional QUIC streams initiated by the remote QUIC endpoint.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608
		"""
		try :
			self._initialmaxstreamdatabidiremote = initialmaxstreamdatabidiremote
		except Exception as e:
			raise e

	@property
	def initialmaxstreamdatauni(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for unidirectional streams initiated by the remote QUIC endpoint.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608.
		"""
		try :
			return self._initialmaxstreamdatauni
		except Exception as e:
			raise e

	@initialmaxstreamdatauni.setter
	def initialmaxstreamdatauni(self, initialmaxstreamdatauni) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial flow control limit, in bytes, for unidirectional streams initiated by the remote QUIC endpoint.<br/>Default value: 262144<br/>Minimum length =  8192<br/>Maximum length =  8388608
		"""
		try :
			self._initialmaxstreamdatauni = initialmaxstreamdatauni
		except Exception as e:
			raise e

	@property
	def initialmaxstreamsbidi(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial maximum number of bidirectional streams the remote QUIC endpoint may initiate.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  500.
		"""
		try :
			return self._initialmaxstreamsbidi
		except Exception as e:
			raise e

	@initialmaxstreamsbidi.setter
	def initialmaxstreamsbidi(self, initialmaxstreamsbidi) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial maximum number of bidirectional streams the remote QUIC endpoint may initiate.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  500
		"""
		try :
			self._initialmaxstreamsbidi = initialmaxstreamsbidi
		except Exception as e:
			raise e

	@property
	def initialmaxstreamsuni(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial maximum number of unidirectional streams the remote QUIC endpoint may initiate.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  500.
		"""
		try :
			return self._initialmaxstreamsuni
		except Exception as e:
			raise e

	@initialmaxstreamsuni.setter
	def initialmaxstreamsuni(self, initialmaxstreamsuni) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the initial maximum number of unidirectional streams the remote QUIC endpoint may initiate.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  500
		"""
		try :
			self._initialmaxstreamsuni = initialmaxstreamsuni
		except Exception as e:
			raise e

	@property
	def maxackdelay(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum amount of time, in milliseconds, by which the Citrix ADC will delay sending acknowledgments.<br/>Default value: 20<br/>Minimum length =  10<br/>Maximum length =  2000.
		"""
		try :
			return self._maxackdelay
		except Exception as e:
			raise e

	@maxackdelay.setter
	def maxackdelay(self, maxackdelay) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum amount of time, in milliseconds, by which the Citrix ADC will delay sending acknowledgments.<br/>Default value: 20<br/>Minimum length =  10<br/>Maximum length =  2000
		"""
		try :
			self._maxackdelay = maxackdelay
		except Exception as e:
			raise e

	@property
	def maxidletimeout(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum idle timeout, in seconds, for a QUIC connection. A QUIC connection will be silently discarded by the Citrix ADC if it remains idle for longer than the minimum of the idle timeout values advertised by the Citrix ADC and the remote QUIC endpoint, and three times the current Probe Timeout (PTO).<br/>Default value: 180<br/>Minimum length =  1<br/>Maximum length =  3600.
		"""
		try :
			return self._maxidletimeout
		except Exception as e:
			raise e

	@maxidletimeout.setter
	def maxidletimeout(self, maxidletimeout) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the maximum idle timeout, in seconds, for a QUIC connection. A QUIC connection will be silently discarded by the Citrix ADC if it remains idle for longer than the minimum of the idle timeout values advertised by the Citrix ADC and the remote QUIC endpoint, and three times the current Probe Timeout (PTO).<br/>Default value: 180<br/>Minimum length =  1<br/>Maximum length =  3600
		"""
		try :
			self._maxidletimeout = maxidletimeout
		except Exception as e:
			raise e

	@property
	def maxudpdatagramsperburst(self) :
		r"""An integer value, specifying the maximum number of UDP datagrams that can be transmitted by the Citrix ADC in a single transmission burst on a QUIC connection.<br/>Default value: 8<br/>Minimum length =  1<br/>Maximum length =  256.
		"""
		try :
			return self._maxudpdatagramsperburst
		except Exception as e:
			raise e

	@maxudpdatagramsperburst.setter
	def maxudpdatagramsperburst(self, maxudpdatagramsperburst) :
		r"""An integer value, specifying the maximum number of UDP datagrams that can be transmitted by the Citrix ADC in a single transmission burst on a QUIC connection.<br/>Default value: 8<br/>Minimum length =  1<br/>Maximum length =  256
		"""
		try :
			self._maxudpdatagramsperburst = maxudpdatagramsperburst
		except Exception as e:
			raise e

	@property
	def maxudppayloadsize(self) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the size of the largest UDP datagram payload, in bytes, that the Citrix ADC is willing to receive on a QUIC connection.<br/>Default value: 1472<br/>Minimum length =  1252<br/>Maximum length =  9188.
		"""
		try :
			return self._maxudppayloadsize
		except Exception as e:
			raise e

	@maxudppayloadsize.setter
	def maxudppayloadsize(self, maxudppayloadsize) :
		r"""An integer value advertised by the Citrix ADC to the remote QUIC endpoint, specifying the size of the largest UDP datagram payload, in bytes, that the Citrix ADC is willing to receive on a QUIC connection.<br/>Default value: 1472<br/>Minimum length =  1252<br/>Maximum length =  9188
		"""
		try :
			self._maxudppayloadsize = maxudppayloadsize
		except Exception as e:
			raise e

	@property
	def newtokenvalidityperiod(self) :
		r"""An integer value, specifying the validity period, in seconds, of address validation tokens issued through QUIC NEW_TOKEN frames sent by the Citrix ADC.<br/>Default value: 300<br/>Minimum length =  1<br/>Maximum length =  3600.
		"""
		try :
			return self._newtokenvalidityperiod
		except Exception as e:
			raise e

	@newtokenvalidityperiod.setter
	def newtokenvalidityperiod(self, newtokenvalidityperiod) :
		r"""An integer value, specifying the validity period, in seconds, of address validation tokens issued through QUIC NEW_TOKEN frames sent by the Citrix ADC.<br/>Default value: 300<br/>Minimum length =  1<br/>Maximum length =  3600
		"""
		try :
			self._newtokenvalidityperiod = newtokenvalidityperiod
		except Exception as e:
			raise e

	@property
	def retrytokenvalidityperiod(self) :
		r"""An integer value, specifying the validity period, in seconds, of address validation tokens issued through QUIC Retry packets sent by the Citrix ADC.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  120.
		"""
		try :
			return self._retrytokenvalidityperiod
		except Exception as e:
			raise e

	@retrytokenvalidityperiod.setter
	def retrytokenvalidityperiod(self, retrytokenvalidityperiod) :
		r"""An integer value, specifying the validity period, in seconds, of address validation tokens issued through QUIC Retry packets sent by the Citrix ADC.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  120
		"""
		try :
			self._retrytokenvalidityperiod = retrytokenvalidityperiod
		except Exception as e:
			raise e

	@property
	def statelessaddressvalidation(self) :
		r"""Specify whether the Citrix ADC should perform stateless address validation for QUIC clients, by sending tokens in QUIC Retry packets during QUIC connection establishment, and by sending tokens in QUIC NEW_TOKEN frames after QUIC connection establishment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._statelessaddressvalidation
		except Exception as e:
			raise e

	@statelessaddressvalidation.setter
	def statelessaddressvalidation(self, statelessaddressvalidation) :
		r"""Specify whether the Citrix ADC should perform stateless address validation for QUIC clients, by sending tokens in QUIC Retry packets during QUIC connection establishment, and by sending tokens in QUIC NEW_TOKEN frames after QUIC connection establishment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._statelessaddressvalidation = statelessaddressvalidation
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if the QUIC profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(quicprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.quicprofile
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
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = quicprofile()
		addresource.name = resource.name
		addresource.ackdelayexponent = resource.ackdelayexponent
		addresource.activeconnectionidlimit = resource.activeconnectionidlimit
		addresource.activeconnectionmigration = resource.activeconnectionmigration
		addresource.congestionctrlalgorithm = resource.congestionctrlalgorithm
		addresource.initialmaxdata = resource.initialmaxdata
		addresource.initialmaxstreamdatabidilocal = resource.initialmaxstreamdatabidilocal
		addresource.initialmaxstreamdatabidiremote = resource.initialmaxstreamdatabidiremote
		addresource.initialmaxstreamdatauni = resource.initialmaxstreamdatauni
		addresource.initialmaxstreamsbidi = resource.initialmaxstreamsbidi
		addresource.initialmaxstreamsuni = resource.initialmaxstreamsuni
		addresource.maxackdelay = resource.maxackdelay
		addresource.maxidletimeout = resource.maxidletimeout
		addresource.maxudpdatagramsperburst = resource.maxudpdatagramsperburst
		addresource.maxudppayloadsize = resource.maxudppayloadsize
		addresource.newtokenvalidityperiod = resource.newtokenvalidityperiod
		addresource.retrytokenvalidityperiod = resource.retrytokenvalidityperiod
		addresource.statelessaddressvalidation = resource.statelessaddressvalidation
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add quicprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ quicprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = quicprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete quicprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = quicprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ quicprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ quicprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = quicprofile()
		updateresource.name = resource.name
		updateresource.ackdelayexponent = resource.ackdelayexponent
		updateresource.activeconnectionidlimit = resource.activeconnectionidlimit
		updateresource.activeconnectionmigration = resource.activeconnectionmigration
		updateresource.congestionctrlalgorithm = resource.congestionctrlalgorithm
		updateresource.initialmaxdata = resource.initialmaxdata
		updateresource.initialmaxstreamdatabidilocal = resource.initialmaxstreamdatabidilocal
		updateresource.initialmaxstreamdatabidiremote = resource.initialmaxstreamdatabidiremote
		updateresource.initialmaxstreamdatauni = resource.initialmaxstreamdatauni
		updateresource.initialmaxstreamsbidi = resource.initialmaxstreamsbidi
		updateresource.initialmaxstreamsuni = resource.initialmaxstreamsuni
		updateresource.maxackdelay = resource.maxackdelay
		updateresource.maxidletimeout = resource.maxidletimeout
		updateresource.maxudpdatagramsperburst = resource.maxudpdatagramsperburst
		updateresource.maxudppayloadsize = resource.maxudppayloadsize
		updateresource.newtokenvalidityperiod = resource.newtokenvalidityperiod
		updateresource.retrytokenvalidityperiod = resource.retrytokenvalidityperiod
		updateresource.statelessaddressvalidation = resource.statelessaddressvalidation
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update quicprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ quicprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of quicprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = quicprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ quicprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ quicprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the quicprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = quicprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = quicprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [quicprofile() for _ in range(len(name))]
						obj = [quicprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = quicprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of quicprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = quicprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the quicprofile resources configured on NetScaler.
		"""
		try :
			obj = quicprofile()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of quicprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = quicprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
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

	class Activeconnectionmigration:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Statelessaddressvalidation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Congestionctrlalgorithm:
		Default = "Default"
		NewReno = "NewReno"
		CUBIC = "CUBIC"
		BBR = "BBR"

class quicprofile_response(base_response) :
	def __init__(self, length=1) :
		self.quicprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.quicprofile = [quicprofile() for _ in range(length)]

