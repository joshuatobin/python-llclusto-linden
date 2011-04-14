import clusto
from llclusto.drivers.base import LindenRackableEquipment
from llclusto.drivers.common import LindenHostnameMixin


class LindenAppliance(LindenRackableEquipment, LindenHostnameMixin):
    """                                                                                                                              
    LindenAppliance Driver.                                                                                                             
    """

    _clusto_type = "appliance"
    _driver_name = "lindenappliance"

class Isilon(LindenAppliance):
    """
    """

    _driver_name = "isilon"

    _properties = {'model':None,
                   'manufacturer': None}

    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 'console-serial' : { 'numports':1, }
                 }

class GSA(LindenAppliance):
    """
    GSA Driver
    """

    _driver_name = "gsa"

    _properties = {'model':None,
                   'manufacturer': None}


    _portmeta = {'pwr-nema-5': {'numports': 2},
                 'nic-eth': {'numports': 1},
                 'console-serial': {'numports': 1}}
    rack_units = 2

class F5_8900(LindenAppliance):
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

class F5_1600(LindenAppliance):
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




