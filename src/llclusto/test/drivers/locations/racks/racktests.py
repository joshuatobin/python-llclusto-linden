import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.locations.racks import LindenRack
from llclusto.drivers.devices.powerstrips import LindenPDU

class LindenRackPDUTests(testbase.ClustoTestBase):
    """ 
    """
    def test_attach_and_remove_pdus(self):
        """
        Test to add and remove a pdu to a rack.
        """

        pdu1 = LindenPDU()
        pdu2 = LindenPDU()
        pdu3 = LindenPDU()
        pdu4 = LindenPDU()
        pdu5 = LindenPDU()
        rack = LindenRack("c3-03-31")
        non_linden_switch = clusto.drivers.networkswitches.Cisco2960("non-linden-switch")

        self.assertEquals(pdu1.type, 'pdu')
        self.assertEquals(rack.type, 'rack')
        self.assertEquals(rack.get_attached_pdus(), [])
        
        rack.attach_pdu(pdu1)
        self.assertEquals(len(rack.contents()), 1)

        rack.attach_pdu(pdu2)
        self.assertEquals(len(rack.contents()), 2)

        self.assertEquals(rack.get_attached_pdus(), [pdu1, pdu2])

        rack.attach_pdu(pdu3)
        self.assertEquals(len(rack.contents()), 3)
        
        self.assertEquals(rack.get_attached_pdus(), [pdu1, pdu2, pdu3])

        rack.attach_pdu(pdu4)
        self.assertEquals(len(rack.contents()), 4)

        self.assertEquals(rack.get_attached_pdus(), [pdu1, pdu2, pdu3, pdu4])

        self.assertEquals(len(rack.get_attached_pdus()), 4)

        # Raise an exception if more than 4 PDUs are added to a rack.
        self.assertRaises(Exception, lambda: rack.attach_pdu(pdu5)) 

        rack.detach_pdu(pdu1)
        self.assertEquals(len(rack.contents()), 3)

        self.assertEquals(rack.get_attached_pdus(), [pdu2, pdu3, pdu4])

        rack.detach_pdu(pdu2)
        self.assertEquals(len(rack.contents()), 2)

        self.assertEquals(rack.get_attached_pdus(), [pdu3, pdu4])

        rack.detach_pdu(pdu3)
        self.assertEquals(len(rack.contents()), 1)

        self.assertEquals(rack.get_attached_pdus(), [pdu4])

        rack.detach_pdu(pdu4)
        self.assertEquals(rack.contents(), [])

        # Raise an exception if a device not in LindenRackableEquipment is inserted
        self.assertRaises(Exception, lambda: rack.insert(non_linden_switch, 1))





