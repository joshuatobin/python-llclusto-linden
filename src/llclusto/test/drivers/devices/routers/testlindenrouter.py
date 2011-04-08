import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.routers import LindenRouter

class LindenSwitchTests(testbase.ClustoTestBase):
    """ 
    """
    def test_lindenrouter(self):
        """
        """
        router = LindenRouter()
        self.assertEquals(router.type, 'router')






