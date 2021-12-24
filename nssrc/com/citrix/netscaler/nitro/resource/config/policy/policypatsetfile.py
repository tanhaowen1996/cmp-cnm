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

class policypatsetfile(base_resource) :
	""" Configuration for patset file resource. """
	def __init__(self) :
		self._src = None
		self._name = None
		self._overwrite = None
		self._delimiter = None
		self._charset = None
		self._comment = None
		self._imported = None
		self._totalpatterns = None
		self._boundpatterns = None
		self._patsetname = None
		self._bindstatuscode = None
		self._bindstatus = None
		self.___count = None

	@property
	def src(self) :
		r"""URL in protocol, host, path, and file name format from where the patset file will be imported. If file is already present, then it can be imported using local keyword (import patsetfile local:filename patsetfile1)
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		r"""URL in protocol, host, path, and file name format from where the patset file will be imported. If file is already present, then it can be imported using local keyword (import patsetfile local:filename patsetfile1)
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name to assign to the imported patset file. Unique name of the pattern set. Not case sensitive. Must begin with an ASCII letter or underscore (_) character and must contain only alphanumeric and underscore characters.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name to assign to the imported patset file. Unique name of the pattern set. Not case sensitive. Must begin with an ASCII letter or underscore (_) character and must contain only alphanumeric and underscore characters.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def overwrite(self) :
		r"""Overwrites the existing file.
		"""
		try :
			return self._overwrite
		except Exception as e:
			raise e

	@overwrite.setter
	def overwrite(self, overwrite) :
		r"""Overwrites the existing file.
		"""
		try :
			self._overwrite = overwrite
		except Exception as e:
			raise e

	@property
	def delimiter(self) :
		r"""patset file patterns delimiter.<br/>Default value: 10.
		"""
		try :
			return self._delimiter
		except Exception as e:
			raise e

	@delimiter.setter
	def delimiter(self, delimiter) :
		r"""patset file patterns delimiter.<br/>Default value: 10
		"""
		try :
			self._delimiter = delimiter
		except Exception as e:
			raise e

	@property
	def charset(self) :
		r"""Character set associated with the characters in the string.<br/>Possible values = ASCII, UTF_8.
		"""
		try :
			return self._charset
		except Exception as e:
			raise e

	@charset.setter
	def charset(self, charset) :
		r"""Character set associated with the characters in the string.<br/>Possible values = ASCII, UTF_8
		"""
		try :
			self._charset = charset
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments to preserve information about this patsetfile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments to preserve information about this patsetfile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def imported(self) :
		r"""When set, display only shows all imported patsetfiles.<br/>Default value: 0.
		"""
		try :
			return self._imported
		except Exception as e:
			raise e

	@imported.setter
	def imported(self, imported) :
		r"""When set, display only shows all imported patsetfiles.<br/>Default value: 0
		"""
		try :
			self._imported = imported
		except Exception as e:
			raise e

	@property
	def totalpatterns(self) :
		r"""Total number of patterns in the patset file.
		"""
		try :
			return self._totalpatterns
		except Exception as e:
			raise e

	@property
	def boundpatterns(self) :
		r"""Total number of patterns bound to a patset.
		"""
		try :
			return self._boundpatterns
		except Exception as e:
			raise e

	@property
	def patsetname(self) :
		r"""The patset with which the patsetfile is associated.
		"""
		try :
			return self._patsetname
		except Exception as e:
			raise e

	@property
	def bindstatuscode(self) :
		r"""The status code of pattern bindings to patset.
		"""
		try :
			return self._bindstatuscode
		except Exception as e:
			raise e

	@property
	def bindstatus(self) :
		r"""The status of pattern bindings to patset.
		"""
		try :
			return self._bindstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(policypatsetfile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.policypatsetfile
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
	def Import(cls, client, resource) :
		r""" Use this API to Import policypatsetfile.
		"""
		try :
			if type(resource) is not list :
				Importresource = policypatsetfile()
				Importresource.src = resource.src
				Importresource.name = resource.name
				Importresource.overwrite = resource.overwrite
				Importresource.delimiter = resource.delimiter
				Importresource.charset = resource.charset
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ policypatsetfile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].src = resource[i].src
						Importresources[i].name = resource[i].name
						Importresources[i].overwrite = resource[i].overwrite
						Importresources[i].delimiter = resource[i].delimiter
						Importresources[i].charset = resource[i].charset
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = policypatsetfile()
		addresource.name = resource.name
		addresource.comment = resource.comment
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add policypatsetfile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ policypatsetfile() for _ in range(len(resource))]
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
		deleteresource = policypatsetfile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete policypatsetfile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = policypatsetfile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ policypatsetfile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ policypatsetfile() for _ in range(len(resource))]
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
		changeresource = policypatsetfile()
		changeresource.name = resource.name
		return changeresource

	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change policypatsetfile.
		"""
		try :
			if type(resource) is not list :
				changeresource = cls.filter_update_parameters(resource)
				return changeresource.perform_operation(client,"update")
			else :
				if (resource and len(resource) > 0) :
					changeresources = [ policypatsetfile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						changeresources[i] = cls.filter_change_parameters(resource[i])
				result = cls.perform_operation_bulk_request(client, changeresources,"update")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the policypatsetfile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = policypatsetfile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = policypatsetfile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [policypatsetfile() for _ in range(len(name))]
						obj = [policypatsetfile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = policypatsetfile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the policypatsetfile resources that are configured on netscaler.
	# This uses policypatsetfile_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = policypatsetfile()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of policypatsetfile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policypatsetfile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the policypatsetfile resources configured on NetScaler.
		"""
		try :
			obj = policypatsetfile()
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
		r""" Use this API to count filtered the set of policypatsetfile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = policypatsetfile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Charset:
		ASCII = "ASCII"
		UTF_8 = "UTF_8"

class policypatsetfile_response(base_response) :
	def __init__(self, length=1) :
		self.policypatsetfile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.policypatsetfile = [policypatsetfile() for _ in range(length)]

