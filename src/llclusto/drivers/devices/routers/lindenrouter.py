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

