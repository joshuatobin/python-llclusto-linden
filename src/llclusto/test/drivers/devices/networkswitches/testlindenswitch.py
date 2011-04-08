import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.devices.networkswitches import LindenSwitch, HP2810_48G, JuniperEX4200

class LindenSwitchTests(testbase.ClustoTestBase):
    """ 
    """
    def test_lindenswitch(self):
        """
        """
        switch = LindenSwitch()
        self.assertEquals(switch.type, 'networkswitch')

class HP2810_48GTests(testbase.ClustoTestBase):
    """ 
    """
    def test_hp2810(self):
        """
        """
        switch = HP2810_48G()
        self.assertEquals(switch.type, 'networkswitch')

class JuniperEX4200Tests(testbase.ClustoTestBase):
    """ 
    """
    def test_juniperex4200(self):
        """

        """
        switch = JuniperEX4200()
        self.assertEquals(switch.type, 'networkswitch')





