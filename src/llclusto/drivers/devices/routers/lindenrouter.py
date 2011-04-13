import clusto
from llclusto.drivers.base import LindenRackableEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.common import PortMixin, IPMixin
from clusto.drivers.devices.networkswitches import BasicNetworkSwitch


class LindenRouter(LindenRackableEquipment, LindenHostnameMixin, PortMixin, IPMixin):
    """                                                                                                                              
    LindenRouter Driver.                                                                                                             
    """
    _clusto_type = "router"
    _driver_name = "lindenrouter"

    _portmeta = {'pwr-nema-5' : {'numports':4},
                 'nic-eth' : {'numports':24}}

