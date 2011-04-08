import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.powerstrips import LindenPDU

class LindenSwitchTests(testbase.ClustoTestBase):
    """ 
    """
    def test_lindenpdu(self):
        """
        """
        pdu = LindenPDU()
        self.assertEquals(pdu.type, 'pdu')







