import clusto
from llclusto.drivers.base import LindenEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.networkswitches import BasicNetworkSwitch

class LindenRouter(LindenEquipment, LindenHostnameMixin, BasicNetworkSwitch):
    """                                                                                                                              
    LindenRouter Driver.                                                                                                             
    """

    _clusto_type = "router"
    _driver_name = "lindenrouter"

    _properties = {'model':None,
                   'manufacturer': None}

    _portmeta = {'pwr-nema-5' : {'numports':4},
                 'nic-eth' : {'numports':24}}
