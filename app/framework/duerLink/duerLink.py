# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_duerLink', [dirname(__file__)])
        except ImportError:
            import _duerLink
            return _duerLink
        if fp is not None:
            try:
                _mod = imp.load_module('_duerLink', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _duerLink = swig_import_helper()
    del swig_import_helper
else:
    import _duerLink
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x



_duerLink.Duer_Link_Version_swigconstant(_duerLink)
Duer_Link_Version = _duerLink.Duer_Link_Version

_duerLink.ENetworkNone_swigconstant(_duerLink)
ENetworkNone = _duerLink.ENetworkNone

_duerLink.ENetworkConfigExited_swigconstant(_duerLink)
ENetworkConfigExited = _duerLink.ENetworkConfigExited

_duerLink.ENetworkConfigStarted_swigconstant(_duerLink)
ENetworkConfigStarted = _duerLink.ENetworkConfigStarted

_duerLink.ENetworkConfigIng_swigconstant(_duerLink)
ENetworkConfigIng = _duerLink.ENetworkConfigIng

_duerLink.ENetworkConfigRouteFailed_swigconstant(_duerLink)
ENetworkConfigRouteFailed = _duerLink.ENetworkConfigRouteFailed

_duerLink.ENetworkLinkSucceed_swigconstant(_duerLink)
ENetworkLinkSucceed = _duerLink.ENetworkLinkSucceed

_duerLink.ENetworkLinkFailed_swigconstant(_duerLink)
ENetworkLinkFailed = _duerLink.ENetworkLinkFailed

_duerLink.ENetworkRecoveryStart_swigconstant(_duerLink)
ENetworkRecoveryStart = _duerLink.ENetworkRecoveryStart

_duerLink.ENetworkRecoverySucceed_swigconstant(_duerLink)
ENetworkRecoverySucceed = _duerLink.ENetworkRecoverySucceed

_duerLink.ENetworkRecoveryFailed_swigconstant(_duerLink)
ENetworkRecoveryFailed = _duerLink.ENetworkRecoveryFailed

_duerLink.ERaspberryPi_swigconstant(_duerLink)
ERaspberryPi = _duerLink.ERaspberryPi

_duerLink.EMtk_swigconstant(_duerLink)
EMtk = _duerLink.EMtk

_duerLink.EHodor_swigconstant(_duerLink)
EHodor = _duerLink.EHodor

_duerLink.EOther_swigconstant(_duerLink)
EOther = _duerLink.EOther

_duerLink.ESoftAP_swigconstant(_duerLink)
ESoftAP = _duerLink.ESoftAP

_duerLink.EBle_swigconstant(_duerLink)
EBle = _duerLink.EBle

_duerLink.EAll_swigconstant(_duerLink)
EAll = _duerLink.EAll

_duerLink.EThird_Party_SuNing_swigconstant(_duerLink)
EThird_Party_SuNing = _duerLink.EThird_Party_SuNing

_duerLink.UNAVAILABLE_swigconstant(_duerLink)
UNAVAILABLE = _duerLink.UNAVAILABLE

_duerLink.AVAILABLE_swigconstant(_duerLink)
AVAILABLE = _duerLink.AVAILABLE

_duerLink.UNKNOW_swigconstant(_duerLink)
UNKNOW = _duerLink.UNKNOW

_duerLink.EDeviceAll_swigconstant(_duerLink)
EDeviceAll = _duerLink.EDeviceAll

_duerLink.EDeviceTV_swigconstant(_duerLink)
EDeviceTV = _duerLink.EDeviceTV

_duerLink.EDeviceSuningTV_swigconstant(_duerLink)
EDeviceSuningTV = _duerLink.EDeviceSuningTV

_duerLink.EDeviceHodor_swigconstant(_duerLink)
EDeviceHodor = _duerLink.EDeviceHodor

_duerLink.ENotFoundDevice_swigconstant(_duerLink)
ENotFoundDevice = _duerLink.ENotFoundDevice

_duerLink.EDeviceConnectionFailed_swigconstant(_duerLink)
EDeviceConnectionFailed = _duerLink.EDeviceConnectionFailed

_duerLink.EDeviceConnectionSuccess_swigconstant(_duerLink)
EDeviceConnectionSuccess = _duerLink.EDeviceConnectionSuccess

_duerLink.EDeviceDisconnectionFailed_swigconstant(_duerLink)
EDeviceDisconnectionFailed = _duerLink.EDeviceDisconnectionFailed

_duerLink.EDeviceDisconnectionSuccess_swigconstant(_duerLink)
EDeviceDisconnectionSuccess = _duerLink.EDeviceDisconnectionSuccess

_duerLink.EDeviceSendMsgFailed_swigconstant(_duerLink)
EDeviceSendMsgFailed = _duerLink.EDeviceSendMsgFailed

_duerLink.EDeviceSendMsgSuccess_swigconstant(_duerLink)
EDeviceSendMsgSuccess = _duerLink.EDeviceSendMsgSuccess
class NetworkConfigStatusObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NetworkConfigStatusObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NetworkConfigStatusObserver, name)
    __repr__ = _swig_repr

    def notify_network_config_status(self, notify_type):
        return _duerLink.NetworkConfigStatusObserver_notify_network_config_status(self, notify_type)

    def __init__(self):
        if self.__class__ == NetworkConfigStatusObserver:
            _self = None
        else:
            _self = self
        this = _duerLink.new_NetworkConfigStatusObserver(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _duerLink.delete_NetworkConfigStatusObserver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _duerLink.disown_NetworkConfigStatusObserver(self)
        return weakref_proxy(self)
NetworkConfigStatusObserver_swigregister = _duerLink.NetworkConfigStatusObserver_swigregister
NetworkConfigStatusObserver_swigregister(NetworkConfigStatusObserver)

class NetWorkPingStatusObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NetWorkPingStatusObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NetWorkPingStatusObserver, name)
    __repr__ = _swig_repr

    def network_status_changed(self, status):
        return _duerLink.NetWorkPingStatusObserver_network_status_changed(self, status)

    def __init__(self):
        if self.__class__ == NetWorkPingStatusObserver:
            _self = None
        else:
            _self = self
        this = _duerLink.new_NetWorkPingStatusObserver(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _duerLink.delete_NetWorkPingStatusObserver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _duerLink.disown_NetWorkPingStatusObserver(self)
        return weakref_proxy(self)
NetWorkPingStatusObserver_swigregister = _duerLink.NetWorkPingStatusObserver_swigregister
NetWorkPingStatusObserver_swigregister(NetWorkPingStatusObserver)

class NetworkDiscoverStatusObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NetworkDiscoverStatusObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NetworkDiscoverStatusObserver, name)
    __repr__ = _swig_repr

    def get_link_baiduid(self, baidu_id):
        return _duerLink.NetworkDiscoverStatusObserver_get_link_baiduid(self, baidu_id)

    def get_link_bduss(self, bduss):
        return _duerLink.NetworkDiscoverStatusObserver_get_link_bduss(self, bduss)

    def __init__(self):
        if self.__class__ == NetworkDiscoverStatusObserver:
            _self = None
        else:
            _self = self
        this = _duerLink.new_NetworkDiscoverStatusObserver(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _duerLink.delete_NetworkDiscoverStatusObserver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _duerLink.disown_NetworkDiscoverStatusObserver(self)
        return weakref_proxy(self)
NetworkDiscoverStatusObserver_swigregister = _duerLink.NetworkDiscoverStatusObserver_swigregister
NetworkDiscoverStatusObserver_swigregister(NetworkDiscoverStatusObserver)

class AccessTokenObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AccessTokenObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AccessTokenObserver, name)
    __repr__ = _swig_repr

    def access_token_status(self, status, info):
        return _duerLink.AccessTokenObserver_access_token_status(self, status, info)

    def __init__(self):
        if self.__class__ == AccessTokenObserver:
            _self = None
        else:
            _self = self
        this = _duerLink.new_AccessTokenObserver(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _duerLink.delete_AccessTokenObserver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _duerLink.disown_AccessTokenObserver(self)
        return weakref_proxy(self)
AccessTokenObserver_swigregister = _duerLink.AccessTokenObserver_swigregister
AccessTokenObserver_swigregister(AccessTokenObserver)

class DuerLinkReceivedDataObserver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DuerLinkReceivedDataObserver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DuerLinkReceivedDataObserver, name)
    __repr__ = _swig_repr

    def NotifyReceivedData(self, jsonPackageData, iSessionID=0):
        return _duerLink.DuerLinkReceivedDataObserver_NotifyReceivedData(self, jsonPackageData, iSessionID)

    def __init__(self):
        if self.__class__ == DuerLinkReceivedDataObserver:
            _self = None
        else:
            _self = self
        this = _duerLink.new_DuerLinkReceivedDataObserver(_self, )
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _duerLink.delete_DuerLinkReceivedDataObserver
    __del__ = lambda self: None
    def __disown__(self):
        self.this.disown()
        _duerLink.disown_DuerLinkReceivedDataObserver(self)
        return weakref_proxy(self)
DuerLinkReceivedDataObserver_swigregister = _duerLink.DuerLinkReceivedDataObserver_swigregister
DuerLinkReceivedDataObserver_swigregister(DuerLinkReceivedDataObserver)

class DuerLinkWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DuerLinkWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DuerLinkWrapper, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["get_instance"] = lambda x: _duerLink.DuerLinkWrapper_get_instance
    if _newclass:
        get_instance = staticmethod(_duerLink.DuerLinkWrapper_get_instance)

    def release(self):
        return _duerLink.DuerLinkWrapper_release(self)

    def init_duer_link(self):
        return _duerLink.DuerLinkWrapper_init_duer_link(self)

    def start_network_recovery(self):
        return _duerLink.DuerLinkWrapper_start_network_recovery(self)

    def start_discover_and_bound(self, client_id):
        return _duerLink.DuerLinkWrapper_start_discover_and_bound(self, client_id)

    def send_dlp_msg_to_all_clients(self, sendBuffer):
        return _duerLink.DuerLinkWrapper_send_dlp_msg_to_all_clients(self, sendBuffer)

    def set_networkConfig_observer(self, config_listener):
        return _duerLink.DuerLinkWrapper_set_networkConfig_observer(self, config_listener)

    def set_discover_observer(self, deicover_listener):
        return _duerLink.DuerLinkWrapper_set_discover_observer(self, deicover_listener)

    def set_monitor_observer(self, ping_listener):
        return _duerLink.DuerLinkWrapper_set_monitor_observer(self, ping_listener)

    def set_dlp_data_observer(self, observer):
        return _duerLink.DuerLinkWrapper_set_dlp_data_observer(self, observer)

    def start_network_config(self):
        return _duerLink.DuerLinkWrapper_start_network_config(self)

    def stop_network_config(self):
        return _duerLink.DuerLinkWrapper_stop_network_config(self)

    def ble_client_connected(self):
        return _duerLink.DuerLinkWrapper_ble_client_connected(self)

    def ble_client_disconnected(self):
        return _duerLink.DuerLinkWrapper_ble_client_disconnected(self)

    def ble_recv_data(self, data, len):
        return _duerLink.DuerLinkWrapper_ble_recv_data(self, data, len)
    __swig_getmethods__["bluez_recv_data"] = lambda x: _duerLink.DuerLinkWrapper_bluez_recv_data
    if _newclass:
        bluez_recv_data = staticmethod(_duerLink.DuerLinkWrapper_bluez_recv_data)

    def start_loudspeaker_ctrl_devices_service(self, *args):
        return _duerLink.DuerLinkWrapper_start_loudspeaker_ctrl_devices_service(self, *args)

    def send_msg_to_devices_by_spec_type(self, msg_buf, device_type_value):
        return _duerLink.DuerLinkWrapper_send_msg_to_devices_by_spec_type(self, msg_buf, device_type_value)

    def disconnect_devices_connections_by_spe_type(self, device_type_value):
        return _duerLink.DuerLinkWrapper_disconnect_devices_connections_by_spe_type(self, device_type_value)
DuerLinkWrapper_swigregister = _duerLink.DuerLinkWrapper_swigregister
DuerLinkWrapper_swigregister(DuerLinkWrapper)

def DuerLinkWrapper_get_instance():
    return _duerLink.DuerLinkWrapper_get_instance()
DuerLinkWrapper_get_instance = _duerLink.DuerLinkWrapper_get_instance

def DuerLinkWrapper_bluez_recv_data(data, len):
    return _duerLink.DuerLinkWrapper_bluez_recv_data(data, len)
DuerLinkWrapper_bluez_recv_data = _duerLink.DuerLinkWrapper_bluez_recv_data

# This file is compatible with both classic and new-style classes.


