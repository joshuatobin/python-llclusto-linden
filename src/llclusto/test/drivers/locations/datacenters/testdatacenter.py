import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.locations.datacenters import LindenDatacenter


class LindenDatacenterTests(testbase.ClustoTestBase):
    """ 
    """
    def test_datacenter(self):
        """
        LindenDatacenter tests.
        """

        dc1 = LindenDatacenter("linden test datacenter", "1234 Test DC WAY, Texas, Somewhere 12456", "415.900.0000", "datacenter@datacenter.com")
         
        self.assertEquals(dc1.type, 'datacenter')
        self.assertEquals(dc1.name, 'linden test datacenter')
        self.assertEquals(dc1.attr_value('remote_hands_email'), 'datacenter@datacenter.com')
        self.assertEquals(dc1.attr_value('address'), '1234 Test DC WAY, Texas, Somewhere 12456')
        self.assertEquals(dc1.attr_value('phone'), '415.900.0000')

        
