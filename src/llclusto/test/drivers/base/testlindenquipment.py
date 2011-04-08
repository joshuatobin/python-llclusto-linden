import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.base import LindenEquipment

class LindenEquipmentTests(testbase.ClustoTestBase):
    """ 
    """
    def test_lindenequipment(self):
        """
        LindenEquipment test. 
        """

        thing = LindenEquipment()

        repr_output = 'LindenEquipment(name=%s, type=device, driver=lindenequipment)' % thing.name

        self.assertEquals(thing.__repr__(), repr_output)
        self.assertEquals(thing.driver, 'lindenequipment')
        self.assertEquals(thing.type, 'device')


        

