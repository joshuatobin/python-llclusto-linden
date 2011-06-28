import llclusto
from llclusto.test import testbase

from llclusto.drivers import ServerClass, Class7Chassis, Class7Server, ChassisFullError, Class5Server


class Class7Tests(testbase.ClustoTestBase):
    def data(self):
        llclusto.drivers.HostState('up')
        class5 = ServerClass("Class 5", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=138)
        class7 = ServerClass("Class 7", num_cpus=2, cores_per_cpu=4, ram_size=24576, disk_size=150)

    def test_insert(self):
        chassis = Class7Chassis()

        server1 = Class7Server("class7-test1.lindenlab.com")
        server2 = Class7Server("class7-test2.lindenlab.com")
        server3 = Class7Server("class7-test3.lindenlab.com")
        server4 = Class7Server("class7-test4.lindenlab.com")
        server5 = Class7Server("class7-test5.lindenlab.com")
        server6 = Class5Server("class5-test1.lindenlab.com")

        self.assertRaises(TypeError, chassis.insert, server6) # Should not be able to insert Class5Server into Class7Chassis

        self.assert_(server1 not in chassis)
        self.assertEqual(Class7Chassis.get_chassis(server1), None)

        chassis.insert(server1)

        self.assert_(server1 in chassis)

        chassis.insert(server2)
        chassis.insert(server3)
        chassis.insert(server4)

        self.assertRaises(ChassisFullError, chassis.insert, server5)

        chassis.remove(server4)
        
        self.assert_(server4 not in chassis)

        chassis.insert(server5)
        
    def test_get_chassis(self):
        chassis1 = Class7Chassis()
        chassis2 = Class7Chassis()
                
        server1 = Class7Server("class7-test1.lindenlab.com")
        server2 = Class7Server("class7-test2.lindenlab.com")
        
        self.assertEqual(Class7Chassis.get_chassis(server1), None)
        self.assertEqual(Class7Chassis.get_chassis(server2), None)
        
        chassis1.insert(server1)
        chassis2.insert(server2)
        
        self.assertEqual(Class7Chassis.get_chassis(server1), chassis1)
        self.assertEqual(Class7Chassis.get_chassis(server2), chassis2)
