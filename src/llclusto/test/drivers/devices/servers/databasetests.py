import llclusto
from llclusto.test import testbase
from llclusto.drivers import DatabaseX, \
                             Database2008, \
                             Database2009, \
                             Database2009SSD, \
                             ServerClass

class DatabaseTests(testbase.ClustoTestBase):

    def data(self):
        dbx = ServerClass("DB X", num_cpus=2, cores_per_cpu=4, ram_size=32768, disk_size=536)
        db2008 = ServerClass("DB 2008", num_cpus=2, cores_per_cpu=4, ram_size=65536, disk_size=403)
        db2009 = ServerClass("DB 2009", num_cpus=2, cores_per_cpu=4, ram_size=49152, disk_size=1238)
        db2009ssd = ServerClass("DB 2009 SSD", num_cpus=2, cores_per_cpu=4, ram_size=98304, disk_size=536)

    def testDatabase(self):
        server = DatabaseX("dbx.lindenlab.com")
        self.assertEquals(server.server_class.name, "DB X")

    def testDatabase2008(self):
        server = Database2008("db2008.lindenlab.com")
        self.assertEquals(server.server_class.name, "DB 2008")

    def testDatabase2009(self):
        server = Database2009("db2009.lindenlab.com")
        self.assertEquals(server.server_class.name, "DB 2009")

    def testDatabase2009SSD(self):
        server = Database2009SSD("db2009ssd.lindenlab.com")
        self.assertEquals(server.server_class.name, "DB 2009 SSD")
