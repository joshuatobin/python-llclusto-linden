import clusto
from clusto.driver import *


class LindenServer(LindenEquipment, BasicServer):
    """
    LindenServer driver.
    """
    _clusto_type = "server"
    _driver_name = "basicserver"


class Class5Server(LindenServer):
    """
    """

    _clusto_type = "server"
    _driver_name = "class5server"


class Class7Chassis(LindenServer):
    """
    """
    pass



class Class7Server(LindenServer, HostnameMixin):
    """
    """

     _properties = {"server_class": None}
 
     def __init__(self, mac):
        class7 = clusto.get_by_name("Class 7")
        self.server_class = class7

    

