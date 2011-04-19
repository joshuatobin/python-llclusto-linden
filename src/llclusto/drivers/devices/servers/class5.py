import clusto
from lindenserver import LindenServer
from serverclass import ServerClass

class Class5Server(LindenServer):
    """Driver for basic Class 5 Servers, and also acts as a superclass for all
    of the fun Class 5 variants we seem to have accreted.
    """

    _driver_name = "class5server"

    _server_class_name = "Class 5"

class Class5bServer(Class5Server):
    """
    """
    
    _driver_name = "class5bserver"
    
    _server_class_name = "Class 5b"
    
class Class5DellF1C(Class5Server):
    """
    """
    
    _driver_name = "class5dellf1cserver"
    
    _server_class_name = "Class 5 Dell F1C"

class Class5DellPowerEdge860(Class5Server):
    """
    """
    
    _driver_name = "class5dellpoweredge860"
    
    _server_class_name = "Class 5 Dell PowerEdge 860"


