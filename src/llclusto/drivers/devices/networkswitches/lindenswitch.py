import clusto
from llclusto.drivers.base import LindenRackableEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.networkswitches import BasicNetworkSwitch

class LindenSwitch(LindenRackableEquipment, LindenHostnameMixin, BasicNetworkSwitch):
    """
    LindenSwitch Driver.
    """
    
    _clusto_type = "networkswitch"
    _driver_name = "lindennetworkswitch"

    _properties = {"serial_number": None,
                   "asset_tag": None,

                   }

class HP2650_48G(LindenSwitch):
    """
    HP 2650
    """

    _driver_name = 'hp2650_48G'

    _portmeta = {
        'pwr-nema-5': {'numports': 1},
        'console-serial': {'numports': 1},
        'nic-eth': {'numports': 48},
    }


class HP2810_48G(LindenSwitch):
    """
    44 autosensing 10/100/1000 ports 
    (IEEE 802.3 Type 10BASE-T, IEEE 802.3u Type 100BASE-TX, IEEE 802.3ab Type 1000BASE-T)

    Media Type: Auto-MDIX

    Duplex: 10BASE-T/100BASE-TX: half or full; 1000BASE-T: full only

    4 dual-personality ports

    each port can be used as either an RJ-45 10/100/1000 port or an open mini-GBIC slot (for use with mini-GBIC transceivers)

    We do not use the mini-gbic ports on any of our rack switches, therefore we'll have 48 ports available on each switch.

    """

    _driver_name = 'hp2810_48G'

    _portmeta = {
        'pwr-nema-5': {'numports': 1},
        'console-serial': {'numports': 1},
        'nic-eth': {'numports': 48},
        'nic-mini-gbic': {'numports': 4}, 
    }

class Juniper_EX4200(LindenSwitch):
    """
    Juniper EX4200-48P/48T
 
    These switches can be configured within a virtual chassis consisting of 10 switches
    """

    _driver_name = 'juniper-ex4200'
    
    _portmeta = {
        'pwr-nema-5': {'numports': 1},
        'console-serial': {'numports': 1},
        'nic-eth': {'numports': 48},
    }



    
