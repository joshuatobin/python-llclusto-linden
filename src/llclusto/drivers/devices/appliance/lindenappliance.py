import clusto
from llclusto.drivers.base import LindenEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.networkswitches import BasicNetworkSwitch

class LindenAppliance(LindenEquipment, LindenHostnameMixin, BasicNetworkSwitch):
    """                                                                                                                              
    LindenAppliance Driver.                                                                                                             
    """

    _clusto_type = "appliance"
    _driver_name = "lindenappliance"

class LindenIsilon(LindenAppliance):
    """
    """

    _driver_name = "lindenisilon"

    _properties = {'model':None,
                   'manufacturer': 'isilon'}

    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 'console-serial' : { 'numports':1, }
                 }

class LindenGSA(LindenAppliance):
    """
    LindenGSA Driver
    """

    _driver_name = "lindengsa"

    _properties = {'model':None,
                   'manufacturer': 'google'}

    _driver_name = "GSA"
    _portmeta = {'pwr-nema-5': {'numports': 2},
                 'nic-eth': {'numports': 1},
                 'console-serial': {'numports': 1}}
    rack_units = 2

class LindenF58900(LindenAppliance):
    """
    Big IP F5 Hardware Loadbalancer Driver.
    """

    _driver_name = "f5hwlb8900"

    _properties = {'model':None,
                   'manufacturer': 'F5'}

    _portmeta = {'pwr-nema-5': {'numports': 2},
                 'nic-eth': {'numports': 16},
                 'giga-fiber': {'numports': 8},
                 'console-serial': {'numports': 1}}

    rack_units = 2

class LindenF51600(LindenAppliance):
    """
    Big IP F5 Hardware Loadbalancer Driver.
    """

    _driver_name = "hwlb1600"

    _properties = {'model': '1600',
                   'manufacturer': 'F5'}

    _portmeta = {'pwr-nema-5': {'numports': 2},
                 'nic-eth': {'numports': 4},
                 'giga-fiber': {'numports': 2},
                 'console-serial': {'numports': 1}}

    rack_units = 1




