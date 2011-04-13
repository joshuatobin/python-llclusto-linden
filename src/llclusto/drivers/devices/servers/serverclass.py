import clusto
from clusto.drivers import Driver

class ServerClass(Driver):
    """Represents an entire class of servers.

    A ServerClass entity will store common information about a class of 
    hardware, such as CPU speed, number of CPUs, number of disks, raid layout, 
    etc.

    We store this information in its own entity so that we have it in the 
    Clusto database, but we don't have to store each item as an Attribute
    for every host.  This also makes it easy to record new information about
    an entire class of servers without having to add an attribute to thousands
    of server entities.

    """

    _driver_name = "serverclass"
    _clusto_type = "serverclass"

    # In the future, we'll probably want to model disks in a more advanced way
    # to model RAID layouts.

    _properties = {'num_cpus': None,
                   'cores_per_cpu': None,
                   'cpu_speed': None,
                   'ram_size': None,
                   'disk_size': None,
                  }

    
    @classmethod
    def get_server_class(cls, server_class_name):
        """Retrieve the (Driver-wrapped) Entity representing the given server class.
        """

        try:
            server_class = clusto.get_by_name(server_class_name)
        except LookupError:
            raise LookupError("Server class %s not found." % server_class_name)

        if not isinstance(server_class, cls):
            raise TypeError("%s is not a server class." % server_class_name)

        return server_class
