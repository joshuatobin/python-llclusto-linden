from lindenserver import LindenServer
from llclusto.drivers import LindenEquipment
from llclusto.exceptions import LLClustoError

class ChassisFullError(LLClustoError):
    pass
    

class Class7Chassis(LindenEquipment):
    """Class 7 Servers are blade servers, with 4 fitting in each 2U chassis. 
    Each Class 7 Chassis fits four Class 7 Servers, but we don't currently
    keep track of which of the four slots each server is in.  It doesn't
    particularly matter; when we need to direct remote hands to a specific
    blade, we just give them the MAC address, which is labelled on the 
    front of the blade.
    """

    _driver_name = "class7chassis"
    _clusto_type = "serverchassis"

    # Hardcoding _num_slots into the class rather than making it a property.  
    # There's never going to be a Class 7 Chassis that has any different number
    # of slots.

    _num_slots = 4

    rack_units = 2

    _properties = {'serial_number': None,
                   'asset_tag': None}

    _portmeta = {'pwr-nema-5': {'numports': 2},
                }

    def insert(self, server):
        """Add a Class7Server to this chassis."""

        if not isinstance(server, Class7Server):
            raise TypeError("Only Class 7 Servers may be inserted into a Class 7 Chassis.")

        if len(self.contents(clusto_types=["server"])) >= self._num_slots:
            raise ChassisFullError("Cannot insert host: chassis is full.")

        super(Class7Chassis, self).insert(server)

    @classmethod
    def get_chassis(cls, server):
        """ Find the chassis in which the given server resides.
        """

        # Partially cribbed from clusto's basicrack.
        chassis = set(server.parents(clusto_types=[cls]))

        assert len(chassis) <= 1

        if len(chassis) == 0:
            return None
        else:
            return chassis.pop()

class Class7Server(LindenServer):
    """A Class 7 Server is a blade that fits in a Class 7 Chassis, 4 per 
    chassis.  Power comes from the chassis, so this driver has no power port
    listed.
    """

    _driver_name = "class7server"

    _server_class_name = "Class 7"

    _portmeta = {'nic-eth': {'numports': 2},
                }
