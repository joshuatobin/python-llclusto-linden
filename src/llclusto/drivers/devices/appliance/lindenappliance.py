import clusto
from llclusto.drivers.base import LindenEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.networkswitches import BasicNetworkSwitch

class LindenAppliance(LindenEquipment, LindenHostnameMixin, BasicNetworkSwitch):
    """                                                                                                                              
    LindenAppliance Driver.                                                                                                             
    """

    _clusto_type = "lindenappliance"
    _driver_name = "appliance"


class LindenIsilon(LindenAppliance):
    """
    """

    _clusto_type = "lindenisilon"
    _driver_name = "isilon"

    _properties = {'model':None,
                   'manufacturer': 'isilon'}

    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 'console-serial' : { 'numports':1, }
                 }


class LindenGSA():
    """
    """
    _driver_name = "GSA"
    _portmeta = {'pwr-nema-5': {'numports': 2},
                 'nic-eth': {'numports': 1},
                 'console-serial': {'numports': 1}}
    rack_units = 2


class LindenF5():
    pass



