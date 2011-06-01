from llclusto.drivers.base import LindenEquipment
from llclusto.drivers.common import LindenHostnameMixin
from clusto.drivers.devices.common import PortMixin
from llclusto.exceptions import LLClustoError
import netsnmp

class PduHostnameError(LLClustoError):
    pass

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


    _properties = {"serial_number": None,
                   "asset_tag": None,
                   }

    def power_on_port(self, port):
        """
        Issues a power_on via SNMPSET to a specified PORT.
        """
        if not self.hostname:
            raise PduHostnameError("A hostname does not exist for %s in Jinx..." % self.entity)

        port_oid = '318.1.1.4.4.2.1.3.%s' % port 
        oid = netsnmp.Varbind('.1.3.6.1.4.1', port_oid, '1', 'INTEGER')
        netsnmp.snmpset(oid, Version = 1, DestHost=self.hostname, Community='private')
        return "port: %s powered on..." % port 

    def power_off_port(self, port):
        """
        Issues a power_off via SNMPSET to a specified PORT.
        """
        if not self.hostname:
            raise PduHostnameError("A hostname does not exist for %s in Jinx..." % self.entity)

        port_oid = '318.1.1.4.4.2.1.3.%s' % port 
        oid = netsnmp.Varbind('.1.3.6.1.4.1', port_oid, '2', 'INTEGER')
        netsnmp.snmpset(oid, Version = 1, DestHost=self.hostname, Community='private')
        return "port: %s powered off..." % port 

    def power_cycle_port(self, port):
        """
        Issues a power_cycle via SNMPSET to a specified PORT.
        """
        if not self.hostname:
            raise PduHostnameError("A hostname does not exist for %s in Jinx..." % self.entity)

        port_oid = '318.1.1.4.4.2.1.3.%s' % port 
        oid = netsnmp.Varbind('.1.3.6.1.4.1', port_oid, '3', 'INTEGER')
        netsnmp.snmpset(oid, Version = 1, DestHost=self.hostname, Community='private')
        return "port: %s power cycled..." % port 

        


