import llclusto
from llclusto.test import testbase

from llclusto.drivers import ServerClass


class ServerClassTests(testbase.ClustoTestBase):
    def test_get_server_class(self):
        classX = ServerClass("Class X Server", num_cpus=1, cores_per_cpu=2, ram_size=3, disk_size=4)

        self.assertEquals(classX, ServerClass.get_server_class("Class X Server"))
