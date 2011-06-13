import clusto
from llclusto.drivers.devices.powerstrips import LindenPDU
from llclusto.drivers.base import LindenEquipment, LindenRackableEquipment
from llclusto.drivers.common import LogMixin
from clusto.drivers.locations.racks import BasicRack

class LindenRack(BasicRack, LogMixin):
    """
    LindenRack driver.
    """
    _clusto_type="rack"
    _driver_name="lindenrack"
    
    _properties = {'minu':1, 'maxu':45, 'pdu_mounts':4}

    def get_attached_pdus(self):
        """
        Returns a list of PDUs attached to a rack.
        """

        return self.attr_values(key="_contains", subkey="pdu")

    def attach_pdu(self, pdu):
        """
        Attach a PDU to a rack.
        """
        # change to lindenpdu
        if not isinstance(pdu, LindenPDU):
            raise TypeError("%s does not appear to be of valid PDU type." % pdu)

        attached_pdus = self.get_attached_pdus()
        
        if len(attached_pdus) >= self.pdu_mounts:
            raise Exception("You can only add up to %d PDUs in a rack. "
                            "This rack already contains %d PDUs..." % (self.pdu_mounts, len(attached_pdus)))
        
        if pdu in attached_pdus:
            raise Exception("%s already exists in rack: %s..." % (pdu, self.entity.name))
        else:
            self.add_attr("_contains", pdu, number=True, subkey="pdu")
        
    def detach_pdu(self, pdu):
        """
        Detach a PDU from a rack.
        """
        
        attached_pdus = self.get_attached_pdus()
        
        if pdu not in attached_pdus:
            raise Exception("%s not found attached to %s." % (pdu, self.name))
        else:
            self.del_attrs("_contains", value=pdu, subkey="pdu")


### Subclassing _ensure_compatible_device from basicrack.py. BasicRack is limited in that it only allows
### inserting devices of class Device. Hardcoding Lindenrackableequipment.

    def _ensure_compatible_device(self, device):
        if not isinstance(device, LindenRackableEquipment):
            raise TypeError("You can only add Linden Rackable Devices to a rack.  %s is a"
                            " %s" % (device.name, str(device.__class__)))
