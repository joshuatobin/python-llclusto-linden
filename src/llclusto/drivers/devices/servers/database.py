import clusto
from lindenserver import LindenServer
from serverclass import ServerClass
from llclusto.drivers import LindenIPMIMixin


class LindenDatabase(LindenServer):
    """ Generic Linden Database """
    _driver_name = "lindendatabase"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }

class DBX(LindenDatabase):
    """ Database X """
    _driver_name = "dbxserver"
    _server_class_name = "DB X"
    rack_units = 2

class DB2008(LindenDatabase):
    """ Database 2008 """
    _driver_name = "db2008server"
    _server_class_name = "DB 2008"
    rack_units =2

class DB2009(LindenDatabase, LindenIPMIMixin):
    """ Database 2009 """
    _driver_name = "db2009server"
    _server_class_name = "DB 2009"
    rack_units = 4

class DB2009SSD(LindenDatabase, LindenIPMIMixin):
    """ Database 2009 with Solid State Disks """
    _driver_name = "db2009ssdserver"
    _server_class_name = "DB 2009 SSD"
    rack_units = 4

class DWDB(LindenDatabase):
    """ DWDB 2U """
    _driver_name = "dwdbserver"
    _server_class_name = "DWDB"
    rack_units = 2

class DWDB2008(LindenDatabase):
    """ DWDB 4U """
    _driver_name = "dwdb2008server"
    _server_class_name = "DWDB 2008"
    rack_units = 2

class DWDB2009(LindenDatabase, LindenIPMIMixin):
    """ DWDB 4U """
    _driver_name = "dwdb2009server"
    _server_class_name = "DWDB 2009"
    rack_units = 4


