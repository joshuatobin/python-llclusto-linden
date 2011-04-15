import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenEquipment, LindenHostnameMixin, LindenIPMIMixin, IPMIHostnameError
from clusto.drivers import PortMixin
from clusto.exceptions import ConnectionException

class TestIPMI(LindenEquipment, LindenIPMIMixin, PortMixin):
    _clusto_type = "testipmi"
    _driver_name = "testipmidriver"

class LindenIPMITests(testbase.ClustoTestBase):
    """ Test linden hostname framework. """

    def testIPMICreation(self):
        d1 = TestIPMI()

        self.assertRaises(TypeError, d1.set_ipmi_info, 0, "01:02:03:04:05:06")
        self.assertRaises(TypeError, d1.set_ipmi_info, "mgmt.lindenlab.com", 1)
        self.assertRaises(IPMIHostnameError, d1.set_ipmi_info, "fizzle.lindenlab.com", "01:02:03:04:05:06")

        d1.set_ipmi_info("mgmt.lindenlab.com", "01:02:03:04:05:06")
        d1_ipmi = d1.get_ipmi_info()
        
        self.assertEquals(d1.get_ipmi_info(), ("mgmt.lindenlab.com", "01:02:03:04:05:06"))
        self.assertEquals(d1.ipmi, ("mgmt.lindenlab.com", "01:02:03:04:05:06"))

        d1.set_ipmi_info("mgmt2.lindenlab.com", "01:02:03:04:05:07")
        d1_ipmi = d1.get_ipmi_info()
        self.assertEquals(d1_ipmi, ("mgmt2.lindenlab.com", "01:02:03:04:05:07"))
        

    def testIPMIDeletion(self):
        d1 = TestIPMI()
        d1.set_ipmi_info("mgmt.lindenlab.com", "01:02:03:04:05:06")
        d1.del_ipmi_info()
        
        d1_ipmi = d1.get_ipmi_info()
        self.assertEquals(d1_ipmi, None)
        
