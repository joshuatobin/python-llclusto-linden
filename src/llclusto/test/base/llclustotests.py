import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenEquipment, LindenHostnameMixin
from clusto.drivers import PortMixin
from clusto.exceptions import ConnectionException

class TestLLClusto(LindenEquipment, LindenHostnameMixin, PortMixin):
    _clusto_type = "testllclusto"
    _driver_name = "testllclustodriver"

class LLClustoTests(testbase.ClustoTestBase):
    """ Test llclusto. """

    def testGetByHostname(self):
        d1 = TestLLClusto()
        d1.hostname = 'foo'

        s1 = llclusto.get_by_hostname('foo')

        self.assertEqual(len(s1), 1)
        self.assertEqual(s1[0], d1)
