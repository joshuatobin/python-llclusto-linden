from llclusto.drivers import LindenEquipment, LindenHostnameMixin
from clusto.drivers import PortMixin
from serverclass import ServerClass
from llclusto.exceptions import LLClustoError
import clusto
import llclusto

class RevertPGIImageError(LLClustoError):
    pass

class LindenServer(LindenEquipment, PortMixin, LindenHostnameMixin):
    """
    LindenServer driver.  Holds common functionality shared by all servers.

    Subclasses of this class will define a "Server Class", a term used at Linden
    Lab to refer to a group of servers all with the same specifications.  We
    represent each server class in Clusto as a single Entity of type ServerClass.
    The ServerClass entity will hold facts about the class such as number of
    CPUs, amount of RAM, etc.  Each LindenServer entity will hold a reference 
    to its ServerClass entity in the server_class property.

    Subclasses should provide a _server_class_name property that holds the name
    of the server class of which they are a member.  The ServerClass entity for
    a given server class must exist in the Clusto database before creating a
    server of that type.
    """

    _clusto_type = "server"
    _driver_name = "lindenserver"

    _portmeta = {'pwr-nema-5': {'numports': 1},
                 'nic-eth': {'numports': 2},
                }

    rack_units = 1

    _properties = {'server_class': None, 
                   "serial_number": None,
                   "asset_tag": None,
                   "_pgi_image": None,
                   "_previous_pgi_image": None,
                   }

    _server_class_name = "Unspecified Server Class"

    def __init__(self, hostname, **kwargs):
        """Create a new server.

        hostname: The hostname for this server.
        """

        try:
            clusto.begin_transaction()

            servers = llclusto.get_by_hostname(hostname)
            if len(servers) > 0:
                raise ValueError("One or more servers with hostname %s already exist: %s" % (hostname, servers))

            super(LindenServer, self).__init__(**kwargs)

            self.hostname = hostname
            self.server_class = ServerClass.get_server_class(self._server_class_name)

            clusto.commit()
        except:
            clusto.rollback_transaction()
            raise

    def __getattr__(self, name):
        """Allow access to facts about a server that are stored in the server 
        class, such as number of CPUs.  For example:

            >>> print server.num_cpus

        is equivalent to

            >>> print server.server_class.num_cpus
        """

        if name in ServerClass._properties:
            return getattr(self.server_class, name)
        else:
            return super(LindenServer, self).__getattr__(name)

    def __setattr__(self, name, value):
        """Prevent setting of facts stored in the server class, such as number
        of CPUs.
        """

        if name in ServerClass._properties:
            raise AttributeError("can't set attributes of server class")
        else:
            super(LindenServer, self).__setattr__(name, value)

    def _set_pgi_image(self, image):
        """ Setter method for the pgi_iamge property  

        Automatically keeps track of the previous associated PGI image.
        """

        try:
            clusto.begin_transaction()

            self._previous_pgi_image = self._pgi_image
            self._pgi_image = image

            clusto.commit()
        except:
            clusto.rollback_transaction()

    def _get_pgi_image(self):
        """ Getter method for the pgi_image property
        """

        return self._pgi_image

    def _get_previous_pgi_image(self):
        """ Getter method for the previous_pgi_image property
        """

        return self._previous_pgi_image

    pgi_image = property(_get_pgi_image, _set_pgi_image, doc=
                         """PGI image associated with this host.  

                            Assigning a new PGI image automatically stores the 
                            previous PGI image in this server as the
                            previous_pgi_image.""")
    previous_pgi_image = property(_get_previous_pgi_image, doc="""PGI image previously associated with this host.""")

    def revert_pgi_image(self):
        """ Revert this host to the previously assigned PGI image.
        
        Raises RevertPGIImageError if no image was previously associated with 
        this host.
        """

        if self.previous_pgi_image is None:
            raise RevertPGIImageError("Cannot revert PGI image, because no image was previously associated with this host.")

        self.pgi_image = self.previous_pgi_image

    def add_stored_pgi_image(self, image):
        """Add an image to this PGI systemimager host.

        Use this function to record the fact that an image is stored on this 
        PGI Systemimager host's disk.  This uses the "contains" relationship,
        so the image will show up in this server's contents if you call the 
        contents() method.
        """

        if image not in self:
            self.add_attr("_contains", image, subkey="pgi-image", number=True)

    def get_stored_pgi_images(self):
        """For PGI Systemimagers, lists all PGI images stored on this host.
        """

        return self.contents(subkey="pgi-image")

    def delete_stored_pgi_image(self, image):
        """Remove an image from this PGI Systemimager.

        Use this function to record the fact that an image is no longer stored
        on this PGI Systemiamger host's disk.
        """

        if image not in self:
            raise LookupError("image %s is not stored on this server" % image)
        else:
            self.del_attrs(key="_contains", value=image, subkey="pgi-image")

