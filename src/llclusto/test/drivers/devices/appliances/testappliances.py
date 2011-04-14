import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.appliance import GSA, F5_8900, F5_1600, Isilon

class GSATests(testbase.ClustoTestBase):
    """ 
    """
    def test_gsa(self):
        """
        """
        gsa = GSA()
        self.assertEquals(gsa.type, 'appliance')

class F58900Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_f5(self):
        """
        """
        f5 = F5_8900()
        self.assertEquals(f5.type, 'appliance')

class F51600Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_f5(self):
        """
        """
        f5 = F5_1600()
        self.assertEquals(f5.type, 'appliance')

class IsilonTests(testbase.ClustoTestBase):
    """ 
    """
    def test_isilon(self):
        """

        """
        isilon = Isilon()
        self.assertEquals(isilon.type, 'appliance')





