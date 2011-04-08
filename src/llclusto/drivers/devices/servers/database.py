import clusto
from lindenserver import LindenServer
from serverclass import ServerClass

class LindenDatabase(LindenServer):
    """ LindenDatabase """

    _driver_name = "lindendatabase"
    _server_class_name = "db"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 2


class LindenDatabase2008(LindenServer):
    """ LindenDatabase 2008 """

    _driver_name = "lindendatabase2008"
    _server_class_name = "db2008"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 2


class LindenDatabase2009(LindenServer):
    """ LindenDatabase 2009 """

    _driver_name = "lindendatabase2009"
    _server_class_name = "db2009"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 4


class LindenDatabase2009SSD(LindenServer):
    """ LindenDatabase 2009 with Solid State Disks """

    _driver_name = "lindendatabase2009ssd"
    _server_class_name = "db2009ssd"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 4

