import llclusto
from llclusto.test import testbase

from llclusto.drivers import ServerClass
from clusto.drivers import Driver

class ServerClassTests(testbase.ClustoTestBase):
    def test_get_server_class(self):
        self.assertRaises(LookupError, ServerClass.get_server_class, "Class X Server")

        classX = ServerClass("Class X Server", num_cpus=1, cores_per_cpu=2, ram_size=3, disk_size=4)

        self.assertEquals(classX, ServerClass.get_server_class("Class X Server"))

        thing = Driver("not a server class")

        self.assertRaises(TypeError, ServerClass.get_server_class, "not a server class")
