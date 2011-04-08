from lindenserver import LindenServer
from llclusto.drivers import LindenEquipment
from llclusto.exceptions import LLClustoError


"""Class 7 hosts are blade servers, with 4 fitting in each 2U chassis."""

class ChassisFullError(LLClustoError):
    pass
    

class Class7Chassis(LindenEquipment):
    """Each Class 7 Chassis fits four Class 7 Servers, but we don't currently
    keep track of which of the four slots each server is in.  It doesn't
    particularly matter at the moment.
    """

    _driver_name = "class7chassis"
    _clusto_type = "serverchassis"

    # Hardcoding this into the class rather than making it a property.  There's
    # never going to be a Class 7 Chassis that has any different number of
    # slots.

    _num_slots = 4

    rack_units = 2

    _properties = {'serial_number': None,
                   'asset_tag': None}

    _portmeta = {'pwr-nema-5': {'numports': 2}
                }

    def insert(self, server):

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
    """
    """

    _driver_name = "class7server"

    _server_class_name = "Class 7"

    # TODO: declaring a port of type 'ipmi' here means it can't be connected
    # to a normal "nic-eth" switch.  We really need port compatibility.

    _portmeta = {'nic-eth': {'numports': 2},
                }
