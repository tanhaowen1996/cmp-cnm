
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use self file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
from base64 import b64encode
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.service.mas_context import MasContext
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.base.Json import Json
from nssrc.com.citrix.netscaler.nitro.resource.base.login import login
from nssrc.com.citrix.netscaler.nitro.resource.base.logout import logout
from nssrc.com.citrix.netscaler.nitro.resource.base.loginchallengeresponse import loginchallengeresponse
from nssrc.com.citrix.netscaler.nitro.resource.config.ha.hafailover import hafailover
from nssrc.com.citrix.netscaler.nitro.resource.config.ha.hasync import hasync
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsconfig import nsconfig
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.reboot import reboot
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsfeature import nsfeature
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsmode import nsmode

def env_var(env, default):
    return os.environ[env] if env in os.environ else default

class nitro_service(object):
    """ nitro_service is client interface through which Nitro operations are performed on resources.
    """
    _password = ""
    _username = ""
    _ipaddress = ""
    _version = ""
    _protocol = ""
    _sessionid=""
    _warning=""
    _timeout=0
    _onerror=""
    _format = ""
    _certvalidation = True
    _mascontext = ""
    _skipinvalidarg = False
    _idempotent = False
    _basic_auth = False

    def __init__(self, connect_context, protocol="http", payload_format=Json()):
        """ nitro_service class constructor specifying ip, format and protocol.

        @param connect_context Ipadress of the netscaler on which configuration is to be run. OR an instance of MasContext.
        @param format format wire language to be used. eg: Json,XML
        @param protocol Protocol.
        """
        if isinstance(connect_context, MasContext):
            self._mascontext = connect_context
        else:
            self._ipaddress = connect_context
        self._version = "v1"
        self._protocol = protocol
        self._format = payload_format
        if protocol.lower()!="http" and protocol.lower()!="https":
            raise nitro_exception("error: protocol value " + protocol + " is not supported")
        self._skipinvalidarg = False
        self._idempotent = False
        self._basic_auth = False

    def set_credential(self, username, password):
        """ sets the credentials for the netscaler.

        @param username Username of the netscaler
        @param password Password for the netscaler.
        """
        try:
            self._username = username
            self._password = password
        except Exception as e:
            raise e

    @property
    def connection_timeout(self):
        return float(env_var("NS_NITRO_CONNECTION_TIMEOUT", "5.0"))

    @property
    def read_timeout(self):
        return float(env_var("NS_NITRO_READ_TIMEOUT", "300.0"))

    @property
    def sessionid(self):
        """ Gets the sessionId.

        @return sessionId.
        """
        try:
            return self._sessionid
        except Exception as e:
            raise e

    @property
    def version(self):
        """ Gets the nitro version.

        @return Nitro version.
        """
        try:
            return self._version
        except Exception as e:
            raise e


    @property
    def ipaddress(self):
        """ Gets the Ipaddress of the netscaler.

        @return Ipadress.
        """
        try:
            return self._ipaddress
        except Exception as e:
            raise e


    @property
    def warning(self):
        """ Gets the warning status.

        @return warning status.
        """
        try:
            return self._warning
        except Exception as e:
            raise e


    @property
    def timeout(self):
        """ Gets the timeout.

        @return timeout.
        """
        try:
            return self._timeout
        except Exception as e:
            raise e


    @timeout.setter
    def timeout(self, timeout):
        """ sets the session inactivity timeout for the netscaler.

        @param timeout session timeout of the netscaler. Default is 30mins.
        """
        try:
            self._timeout = timeout
        except Exception as e:
            raise e


    @warning.setter
    def warning(self, warning):
        """ sets the flag for warning.

        @param warning set self to true for getting warnings in nitro response.
        """
        try:
            self._warning = warning
        except Exception as e:
            raise e


    def isLogin(self):
        """ Checks login status.

        @return true if logged-in or basic-auth is enabled else false.
        """
        try:
            if not self._sessionid and not self._mascontext and not self._basic_auth :
                return False
            return True
        except Exception as e:
            raise e


    @property
    def onerror(self):
        """ Gets the onerror status of the netscaler.

        @return onerror status.
        """
        try:
            if self._onerror is not None:
                return str(self._onerror)
            return ""
        except Exception as e:
            raise e


    @onerror.setter
    def onerror(self, val):
        """ Sets the onerror status of the netscaler.

        @set onerror self option is applicable for bulk requests.
        possible values: EXIT, CONTINUE, ROLLBACK.
        if set with EXIT: exists on the first encountered error.
        if set with CONTINUE: executes all the requests irrespective of individual response status.
        if set with ROLLBACK: rolls back the successful requests upon encountering an error.
        """
        try:
            self._onerror = val
        except Exception as e:
            raise e


    def login(self, username="", password="", timeout=""):
        """ Use self API to login into Netscaler.

        @param username Username
        @param password Password for the Netscaler.
        @param timeout timeout for netscaler session.Default is 1800secs

        @return status of the operation performed.

        @throws Exception nitro exception is thrown.
        """
        try:
            if username and password :
                self.set_credential(username, password)
            if timeout :
                    self.timeout = timeout
            _login = login(self._username, self._password, self._timeout)
            result = _login.perform_operation(self)
            if (result.errorcode == 0 or result.errorcode == 1034):
                self._sessionid = result.sessionid
            return result
        except Exception as e:
            raise e


    def loginchallengeresponse(self, response):
        """ Use self API to loginchallengeresponse into Netscaler with challenge response.

        @return status of the operation performed.

        @throws nitro_exception nitro exception is thrown.
        """
        try:
            logincr = loginchallengeresponse(response)
            result = logincr.perform_operation(self)
            if (result.errorcode == 0):
                self._sessionid = result.sessionid
            return result
        except Exception as e:
            raise e


    def reboot(self, warm):
        """ Use self API to reboot Netscaler.

        @param warm set self to true for warm reboot.

        @return status of the operation performed.
        """
        try:
            resource = reboot()
            resource.warm = warm
            result = resource.perform_operation(self)
            return result
        except Exception as e:
            raise e


    def forcehasync(self, force, save):
        """ Use self API to force the sync in secondary Netscaler.

        @param force set self to true for forcesync
        @param save set self to YES,if want to save the configuration after sync.

        @return status of the operation performed.
        """
        try:
            resource = hasync()
            resource.force = force
            resource.save = save
            option = options()
            option.action = "force"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e


    def forcehafailover(self, force):
        """ Use self API to invoke force failover in primary Netscaler.

        @param force set self to true if force failover is needed.

        @return status of the operation performed.
        """
        try:
            resource = hafailover()
            resource.force = force
            option = options()
            option.action = "force"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e


    def clear_config(self, force="", level=""):
        """ Use self API to clear configuration.

        @param force clear confirmation without prompting.
        @param level clear config according to the level. eg: basic, extended, full

        @return status of the operation performed.
        """
        try:
            if level and force :
                resource = nsconfig()
                if (force):
                    resource.force = force
                resource.level = level
                option = options()
                option.action = "clear"
                result = resource.perform_operation(self, "", option)
                return result
            elif force :
                return self.clear_config(force, "basic")
            else :
                return self.clear_config(True,"basic")
        except Exception as e:
            raise e



    def save_config(self):
        """ Use self API to save configuration on Netscaler.

        @return status of the operation performed.
        """
        try:
            resource = nsconfig()
            option = options()
            option.action = "save"
            result = resource.perform_operation(self, "", option)
            return result;
        except Exception as e:
            raise e


    def get_features(self):
        try:
            features = []
            prefix = "get_"

            methods = nsfeature.__dict__
            # Loop through the methods and find the ones that correspond to
            # feature names.
            for method in methods :
                if (method.startswith(prefix) and ( method !=("get_feature") and method !=("get_object_name") and method !=("get_nitro_response"))) :
                    feature_name = method[len(prefix):]
                    features.append(feature_name)
            return features
        except Exception as e:
            raise e


    def get_enabled_features(self):
        try:
            feature = nsfeature.get(self)
            enabled_features = feature[0].feature
            # Loop through the methods and find the ones that correspond to
            # feature names.
            return enabled_features
        except Exception as e:
            raise e


    def get_modes(self):
        try:
            modes = []
            prefix = "get_"

            methods = nsmode.__dict__
            # Loop through the methods and find the ones that correspond to
            # feature names.
            for method in methods :
                if (method.startswith(prefix) and ( method !=("get_mode") and method !=("get_object_name") and method !=("get_nitro_response"))) :
                    mode_name = method[len(prefix):]
                    modes.append(mode_name)
            return modes
        except Exception as e:
            raise e

    def get_enabled_modes(self):
        try:
            mode = nsmode.get(self)
            enabled_modes = mode[0].mode
            # Loop through the methods and find the ones that correspond to
            # feature names.
            return enabled_modes
        except Exception as e:
            raise e


    def enable_features(self, features):
        """ Use self API to enable the feature on Netscaler.

        @param features features to be enabled.

        @return status of the operation performed.

        @throws Exception Nitro exception.
        """
        try:
            resource = nsfeature()
            resource.feature = features
            option = options()
            option.action = "enable"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e

    def enable_modes(self, modes):
        """ Use self API to enable the mode on Netscaler.

        @param modes modes to be enabled.

        @return status of the operation performed.

        @throws Exception Nitro exception.
        """
        try:
            resource = nsmode()
            resource.mode = modes
            option = options()
            option.action = "enable"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e

    def disable_features(self, features):
        """ Use self API to disable the feature on Netscaler.

        @param features features to be disabled.

        @return status of the operation performed.

        @throws Exception Nitro exception.
        """
        try:
            resource = nsfeature()
            resource.feature = features
            option = options()
            option.action = "disable"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e

    def disable_modes(self, modes):
        """ Use self API to disable the mode on Netscaler.

        @param modes modes to be disabled.

        @return status of the operation performed.

        @throws Exception Nitro exception.
        """
        try:
            resource = nsmode()
            resource.mode = modes
            option = options()
            option.action = "disable"
            result = resource.perform_operation(self, "", option)
            return result
        except Exception as e:
            raise e



    def clear_session(self):
        """ Use self API to clear the current session when the session expires.
        This clears the session only at the client.
        Use logout() API in order to terminate the session.
        """
        try:
            self._sessionid = None
        except Exception as e:
            raise e


    def logout(self):
        """ Use self API to logout from current session.

        @return status of the operation performed.
        """
        try:
            result = None
            logout_ = logout()
            result = logout_.perform_operation(self)
            self._sessionid = None
            self._username = None
            self._password = None
            return result
        except Exception as e:
            raise e

    def get_basic_auth_str(self):
        """ Use this method to get basic authentication string to be sent in Authorization HTTP header

        @return basic auth string
        """
        return "Basic " + b64encode(b"{}:{}".format(self._username, self._password))

    @property
    def protocol(self):
        """ Gets the protocol.

        @return Returns the protocol.
        """
        try:
            return self._protocol
        except Exception as e:
            raise e


    @protocol.setter
    def protocol(self, protocol):
        """ Sets the protocol.

        @param protocol The protocol to be set.
        """
        try:
            if protocol or protocol.lower!="http" or protocol.lower!="https":
                raise nitro_exception("error: protocol value " + protocol + " is not supported")
            self._protocol = protocol
        except Exception as e:
            raise e


    @property
    def payload_formatter(self):
        """ Returns payload format.

        @return Returns json.
        """
        try:
            return self._format
        except Exception as e:
            raise e

    @property
    def certvalidation(self):
        """ Returns certificate validation flag status.

        @return Returns the json.
        """
        try:
            return self._certvalidation
        except Exception as e:
            raise e

    @certvalidation.setter
    def certvalidation(self, flag):
        """ Returns certificate validation flag status.

        @return Returns the json.
        """
        try:
            self._certvalidation = flag
        except Exception as e:
            raise e

    @property
    def mas_context(self):
        """ Returns mascontext """
        return self._mascontext

    @property
    def isMasContext(self):
        return self._mascontext

    @property
    def mas_ipaddress(self):
        try:
            return self._mascontext.mas_ip
        except:
            raise

    @property
    def mas_target_nsip(self):
        try:
            return self._mascontext.target_nsip
        except:
            raise

    @mas_target_nsip.setter
    def mas_target_nsip(self, target_nsip):
        """ Returns certificate validation flag status.
        @return Returns the json.
        """
        try:
            self._mascontext.target_nsip = target_nsip
        except:
            raise

    @property
    def mas_sessionid(self):
        try:
            return self._mascontext.sessionid
        except:
            raise

    @property
    def skipinvalidarg(self):
        """
            @return _skipinvalidarg
        """
        return self._skipinvalidarg

    @skipinvalidarg.setter
    def skipinvalidarg(self, skipinvalidarg):
        """ sets _skipinvalidarg field.

            @param skipinvalidarg
        """
        self._skipinvalidarg = skipinvalidarg

    @property
    def idempotent(self):
        """
        @return _idempotent
        """
        return self._idempotent

    @idempotent.setter
    def idempotent(self, idempotent):
        """ sets _idempotent field.
        @param idempotent
        """
        self._idempotent = idempotent

    @property
    def basic_auth(self):
        """
        @return _basic_auth
        """
        return self._basic_auth

    @basic_auth.setter
    def basic_auth(self, basic_auth):
        """ sets _basic_auth field.
        Set this varibale to True for SDK to use Basic Authentication mode when sending API requests to NetScaler.
        Not applicable when using the SDK against Citrix ADM in Proxy mode.
        @param idempotent
        """
        self._basic_auth = basic_auth
