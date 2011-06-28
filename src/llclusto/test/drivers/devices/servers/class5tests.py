import llclusto
from llclusto.test import testbase
from llclusto.drivers import Class5Server, ServerClass


class Class5Tests(testbase.ClustoTestBase):
    def data(self):
        llclusto.drivers.HostState('up')
        class5 = ServerClass("Class 5", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=138)


    def test_class5(self):
        server = Class5Server("test1.lindenlab.com")

        self.assertEquals(server.server_class.name, "Class 5")
