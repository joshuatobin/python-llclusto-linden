import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenOrca, LindenOrca2009, ServerClass

class LindenOrcaTests(testbase.ClustoTestBase):
    def data(self):
        lindenorca = ServerClass("orca", num_cpus=2, cores_per_cpu=4, ram_size=16384, disk_size=5500)
        lindenorca2009 = ServerClass("orca2009", num_cpus=2, cores_per_cpu=4, ram_size=24576, disk_size=9000)

    def testLindenOrca(self):
        server = LindenOrca("lindenorca.lindenlab.com")
        self.assertEquals(server.server_class.name, "orca")

    def testLindenOrca2009(self):
        server = LindenOrca2009("lindenorca2009.lindenlab.com")
        self.assertEquals(server.server_class.name, "orca2009")
