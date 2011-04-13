import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.appliance import LindenGSA, LindenF5_8900, LindenF5_1600, LindenIsilon

class LindenGSATests(testbase.ClustoTestBase):
    """ 
    """
    def test_gsa(self):
        """
        """
        gsa = LindenGSA()
        self.assertEquals(gsa.type, 'appliance')

class LindenF58900Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_f5(self):
        """
        """
        f5 = LindenF5_8900()
        self.assertEquals(f5.type, 'appliance')

class LindenF51600Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_f5(self):
        """
        """
        f5 = LindenF5_1600()
        self.assertEquals(f5.type, 'appliance')

class LindenIsilonTests(testbase.ClustoTestBase):
    """ 
    """
    def test_isilon(self):
        """

        """
        isilon = LindenIsilon()
        self.assertEquals(isilon.type, 'appliance')





