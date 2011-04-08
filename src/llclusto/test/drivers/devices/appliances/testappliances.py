import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.appliance import LindenGSA, LindenF58900, LindenF51600, LindenIsilon

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
        f5 = LindenF58900()
        self.assertEquals(f5.type, 'appliance')

class LindenF51600Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_f5(self):
        """
        """
        f5 = LindenF51600()
        self.assertEquals(f5.type, 'appliance')

class LindenIsilonTests(testbase.ClustoTestBase):
    """ 
    """
    def test_isilon(self):
        """

        """
        isilon = LindenIsilon()
        self.assertEquals(isilon.type, 'appliance')





