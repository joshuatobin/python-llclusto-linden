import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenEquipment, LindenHostnameMixin, LindenIPMIMixin
from clusto.drivers import PortMixin
from clusto.exceptions import ConnectionException

class TestIPMI(LindenEquipment, LindenIPMIMixin, PortMixin):
    _clusto_type = "testipmi"
    _driver_name = "testipmidriver"

class LindenIPMITests(testbase.ClustoTestBase):
    """ Test linden hostname framework. """

    def testIPMICreation(self):
        d1 = TestIPMI()
        d1.set_ipmi_info("mgmt.lindenlab.com")
        
        d1_ipmi = d1.get_ipmi_info()
        self.assertEquals(d1_ipmi, "mgmt.lindenlab.com")
        
        d1.set_ipmi_info("mgmt2.lindenlab.com")
        d1_ipmi = d1.get_ipmi_info()
        self.assertEquals(d1_ipmi, "mgmt2.lindenlab.com")
        

    def testIPMIDeletion(self):
        d1 = TestIPMI()
        d1.set_ipmi_info("mgmt.lindenlab.com")
        d1.del_ipmi_info()
        
        d1_ipmi = d1.get_ipmi_info()
        self.assertEquals(d1_ipmi, None)
        
