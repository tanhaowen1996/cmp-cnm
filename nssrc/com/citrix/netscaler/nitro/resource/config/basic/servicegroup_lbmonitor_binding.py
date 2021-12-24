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

class servicegroup_lbmonitor_binding(base_resource) :
	""" Binding class showing the lbmonitor that can be bound to servicegroup.
	"""
	def __init__(self) :
		self._monitor_name = None
		self._monweight = None
		self._monstate = None
		self._weight = None
		self._passive = None
		self._servicegroupname = None
		self._port = None
		self._customserverid = None
		self._serverid = None
		self._state = None
		self._hashid = None
		self._nameserver = None
		self._dbsttl = None
		self.___count = None

	@property
	def servicegroupname(self) :
		r"""Name of the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the service group.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number of the service. Each service must have a unique port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number of the service. Each service must have a unique port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def nameserver(self) :
		r"""Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use the global nameserver.
		"""
		try :
			return self._nameserver
		except Exception as e:
			raise e

	@nameserver.setter
	def nameserver(self, nameserver) :
		r"""Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use the global nameserver.
		"""
		try :
			self._nameserver = nameserver
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		r"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		r"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def serverid(self) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			return self._serverid
		except Exception as e:
			raise e

	@serverid.setter
	def serverid(self, serverid) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			self._serverid = serverid
		except Exception as e:
			raise e

	@property
	def customserverid(self) :
		r"""Unique service identifier. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None".
		"""
		try :
			return self._customserverid
		except Exception as e:
			raise e

	@customserverid.setter
	def customserverid(self, customserverid) :
		r"""Unique service identifier. Used when the persistency type for the virtual server is set to Custom Server ID.<br/>Default value: "None"
		"""
		try :
			self._customserverid = customserverid
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def monitor_name(self) :
		r"""Monitor name.
		"""
		try :
			return self._monitor_name
		except Exception as e:
			raise e

	@monitor_name.setter
	def monitor_name(self, monitor_name) :
		r"""Monitor name.
		"""
		try :
			self._monitor_name = monitor_name
		except Exception as e:
			raise e

	@property
	def dbsttl(self) :
		r"""Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0.
		"""
		try :
			return self._dbsttl
		except Exception as e:
			raise e

	@dbsttl.setter
	def dbsttl(self, dbsttl) :
		r"""Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0
		"""
		try :
			self._dbsttl = dbsttl
		except Exception as e:
			raise e

	@property
	def passive(self) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			return self._passive
		except Exception as e:
			raise e

	@passive.setter
	def passive(self, passive) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			self._passive = passive
		except Exception as e:
			raise e

	@property
	def monstate(self) :
		r"""Monitor state.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monstate
		except Exception as e:
			raise e

	@monstate.setter
	def monstate(self, monstate) :
		r"""Monitor state.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monstate = monstate
		except Exception as e:
			raise e

	@property
	def monweight(self) :
		r"""weight of the monitor that is bound to servicegroup.
		"""
		try :
			return self._monweight
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(servicegroup_lbmonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroup_lbmonitor_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = servicegroup_lbmonitor_binding()
		addresource.servicegroupname = resource.servicegroupname
		addresource.port = resource.port
		addresource.monitor_name = resource.monitor_name
		addresource.monstate = resource.monstate
		addresource.passive = resource.passive
		addresource.weight = resource.weight
		addresource.customserverid = resource.customserverid
		addresource.serverid = resource.serverid
		addresource.state = resource.state
		addresource.hashid = resource.hashid
		addresource.nameserver = resource.nameserver
		addresource.dbsttl = resource.dbsttl
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [servicegroup_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = servicegroup_lbmonitor_binding()
		deleteresource.servicegroupname = resource.servicegroupname
		deleteresource.port = resource.port
		deleteresource.monitor_name = resource.monitor_name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [servicegroup_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, servicegroupname="", option_="") :
		r""" Use this API to fetch servicegroup_lbmonitor_binding resources.
		"""
		try :
			if not servicegroupname :
				obj = servicegroup_lbmonitor_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = servicegroup_lbmonitor_binding()
				obj.servicegroupname = servicegroupname
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to fetch filtered set of servicegroup_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		r""" Use this API to count servicegroup_lbmonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to count the filtered set of servicegroup_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup_lbmonitor_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class servicegroup_lbmonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroup_lbmonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroup_lbmonitor_binding = [servicegroup_lbmonitor_binding() for _ in range(length)]

