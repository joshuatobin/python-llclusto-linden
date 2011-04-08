import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.locations.racks import LindenRack
from llclusto.drivers.devices.powerstrips import LindenPDU

#class TestLindenRack(LindenRack):
#    """
#    """
#    _clusto_type="testrack"
#    _driver_name="testlindenrack"
#
#    _properties = {'minu':1, 'maxu':45, 'pdu_mounts':4}
#
#


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
#        rack = TestLindenRack("testrack.lindenlab.com")
        rack = LindenRack("testrack.lindenlab.com")
        
        self.assertEquals(pdu1.type, 'pdu')
        self.assertEquals(rack.type, 'rack')
        self.assertEquals(rack.get_attached_pdus(), [])
        
        rack.attach_pdu(pdu1)
        self.assertEquals(len(rack.contents()), 1)

        rack.attach_pdu(pdu2)
        self.assertEquals(len(rack.contents()), 2)

        rack.attach_pdu(pdu3)
        self.assertEquals(len(rack.contents()), 3)

        rack.attach_pdu(pdu4)
        self.assertEquals(len(rack.contents()), 4)

        self.assertEquals(len(rack.get_attached_pdus()), 4)

        rack.detach_pdu(pdu1)
        self.assertEquals(len(rack.contents()), 3)

        rack.detach_pdu(pdu2)
        self.assertEquals(len(rack.contents()), 2)

        rack.detach_pdu(pdu3)
        self.assertEquals(len(rack.contents()), 1)

        rack.detach_pdu(pdu4)
        self.assertEquals(rack.contents(), [])







