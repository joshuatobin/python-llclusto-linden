import clusto
from lindenserver import LindenServer
from serverclass import ServerClass

class LindenOrca(LindenServer):
    """ LindenOrca """

    _driver_name = "lindenorca"
    _server_class_name = "orca"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 3


class LindenOrca2009(LindenServer):
    """ LindenOrca2009 """

    _driver_name = "lindenorca2009"
    _server_class_name = "orca2009"
    _portmeta = {'pwr-nema-5': {'numports':2},
                 'nic-eth': {'numports':2},
                 }
    rack_units = 4


