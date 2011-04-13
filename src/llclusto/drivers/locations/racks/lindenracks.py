import clusto
from llclusto.drivers.devices.powerstrips import LindenPDU
from llclusto.drivers.base import LindenEquipment, LindenRackableEquipment
from clusto.drivers.locations.racks import BasicRack

class LindenRack(LindenEquipment, BasicRack):
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

###
### The inserter method was cargo-culted from basicrack.py in the clusto source. 
### The upstream version of BasicRack.insert() only allows inserts for classes of Device. 
###
    def insert(self, device, rackU):
        """Insert a given device into the given rackU."""

        if not isinstance(device, LindenRackableEquipment):
            raise TypeError("You can only add Rackable Equipment to a rack.  %s is a"
                            " %s" % (device.name, str(device.__class__)))

        rackU = self._ensure_rack_u(rackU)

        rau = self.get_rack_and_u(device)

        if rau != None:
            raise Exception("%s is already in rack %s"
                            % (device.name, rau['rack'].name))

        if hasattr(device, 'rack_units') and (len(rackU) != device.rack_units):
            raise TypeError("%s is a %dU device, cannot insert it in %dU"
                            % (device.name, units, len(rackU)))

        for U in rackU:
            dev = self.get_device_in(U)
            if dev:
                raise TypeError("%s is already in RU %d" % (dev.name, U))

        for U in rackU:
            self.add_attr("_contains", device, number=U, subkey='ru')



    

