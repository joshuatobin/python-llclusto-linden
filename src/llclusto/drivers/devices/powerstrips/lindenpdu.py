
from llclusto.drivers.base import LindenEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.common import PortMixin

class LindenPDU(LindenEquipment, LindenHostnameMixin, PortMixin):
    """
    Linden PowerStrip 
    """

    _clusto_type = "pdu"
    _driver_name = "lindenpdu"

    _portmeta = { 'pwr-nema-5' : { 'numports':24, },
                  'nic-eth' : { 'numports':1, },
                  'console-serial' : { 'numports':1, },
                  }





        


