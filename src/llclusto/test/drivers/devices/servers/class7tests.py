import llclusto
from llclusto.test import testbase

from llclusto.drivers import ServerClass, Class7Chassis, Class7Server, ChassisFullError, Class5Server


class Class7Tests(testbase.ClustoTestBase):
    def data(self):
        class5 = ServerClass("Class 5", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=138)
        class7 = ServerClass("Class 7", num_cpus=2, cores_per_cpu=4, ram_size=24576, disk_size=150)

    def test_insert(self):
        chassis = Class7Chassis()

        server1 = Class7Server("class7-test1.lindenlab.com")
        server2 = Class7Server("class7-test2.lindenlab.com")
        server3 = Class7Server("class7-test3.lindenlab.com")
        server4 = Class7Server("class7-test4.lindenlab.com")
        server5 = Class7Server("class7-test5.lindenlab.com")
        server6 = Class7Server("class5-test1.lindenlab.com")

        self.assertRaises(TypeError, chassis.insert, server6) # Should not be able to insert Class5Server into Class7Chassis

