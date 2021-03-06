import clusto
from database import LindenDatabase
from serverclass import ServerClass
from llclusto.drivers import LindenIPMIMixin


class Orca(LindenDatabase):
    """ LindenOrca """
    _driver_name = "orcaserver"
    _server_class_name = "Orca"
    rack_units = 3


class Orca2009(LindenDatabase, LindenIPMIMixin):
    """ LindenOrca2009 """
    _driver_name = "orca2009server"
    _server_class_name = "Orca 2009"
    rack_units = 4
