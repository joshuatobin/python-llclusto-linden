import llclusto
from llclusto.test import testbase

from llclusto.drivers import Class6Server, ServerClass


class Class6Tests(testbase.ClustoTestBase):
    def data(self):
        class6 = ServerClass("Class 6", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=500)

    def test_class6(self):
        server = Class6Server("test1.lindenlab.com")

        self.assertEquals(server.server_class.name, "Class 6")
