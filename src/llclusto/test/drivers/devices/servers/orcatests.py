import llclusto
from llclusto.test import testbase
from llclusto.drivers import Orca, Orca2009, ServerClass

class OrcaTests(testbase.ClustoTestBase):
    def data(self):
        llclusto.drivers.HostState('up')
        orca = ServerClass("Orca", num_cpus=2, cores_per_cpu=4, ram_size=16384, disk_size=5500)
        orca2009 = ServerClass("Orca 2009", num_cpus=2, cores_per_cpu=4, ram_size=24576, disk_size=9000)

    def testOrca(self):
        server = Orca("orca.lindenlab.com")
        self.assertEquals(server.server_class.name, "Orca")

    def testOrca2009(self):
        server = Orca2009("orca2009.lindenlab.com")
        self.assertEquals(server.server_class.name, "Orca 2009")
