import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenDatabase, \
                             LindenDatabase2008, \
                             LindenDatabase2009, \
                             LindenDatabase2009SSD, \
                             ServerClass


class LindenDatabaseTests(testbase.ClustoTestBase):
    def data(self):
        lindendb = ServerClass("db", num_cpus=2, cores_per_cpu=4, ram_size=32768, disk_size=536)
        lindendb2008 = ServerClass("db2008", num_cpus=2, cores_per_cpu=4, ram_size=65536, disk_size=403)
        lindendb2009 = ServerClass("db2009", num_cpus=2, cores_per_cpu=4, ram_size=49152, disk_size=1238)
        lindendb2009ssd = ServerClass("db2009ssd", num_cpus=2, cores_per_cpu=4, ram_size=98304, disk_size=536)

    def testLindenDatabase(self):
        server = LindenDatabase("lindendb.lindenlab.com")
        self.assertEquals(server.server_class.name, "db")

    def testLindenDatabase2008(self):
        server = LindenDatabase2008("lindendb2008.lindenlab.com")
        self.assertEquals(server.server_class.name, "db2008")

    def testLindenDatabase2009(self):
        server = LindenDatabase2009("lindendb2009.lindenlab.com")
        self.assertEquals(server.server_class.name, "db2009")

    def testLindenDatabase2009SSD(self):
        server = LindenDatabase2009SSD("lindendb2009ssd.lindenlab.com")
        self.assertEquals(server.server_class.name, "db2009ssd")
