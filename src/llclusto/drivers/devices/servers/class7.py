from lindenserver import LindenServer, LindenServerChassis
from llclusto.drivers import LindenRackableEquipment
from llclusto.drivers import LindenIPMIMixin
from llclusto.exceptions import LLClustoError
from clusto.drivers import PortMixin

class ChassisFullError(LLClustoError):
    pass
    

class Class7Chassis(LindenServerChassis):
    """Class 7 Servers are blade servers, with 4 fitting in each 2U chassis. 
    Each Class 7 Chassis fits four Class 7 Servers, but we don't currently
    keep track of which of the four slots each server is in.  It doesn't
    particularly matter; when we need to direct remote hands to a specific
    blade, we just give them the MAC address, which is labelled on the 
    front of the blade.
    """

    _driver_name = "class7chassis"
    _clusto_type = "serverchassis"

    _properties = {'serial_number': None,
                   'asset_tag': None}

    _portmeta = {'pwr-nema-5': {'numports': 2},
                }

    def insert(self, server):
        """Add a Class7Server to this chassis."""

        if not isinstance(server, Class7Server):
            raise TypeError("Only Class 7 Servers may be inserted into a Class 7 Chassis.")

        super(Class7Chassis, self).insert(server)


class Class7Server(LindenServer, LindenIPMIMixin):
    """A Class 7 Server is a blade that fits in a Class 7 Chassis, 4 per 
    chassis.  Power comes from the chassis, so this driver has no power port
    listed.
    """

    _driver_name = "class7server"

    _server_class_name = "Class 7"

    _portmeta = {'nic-eth': {'numports': 2},
                }
