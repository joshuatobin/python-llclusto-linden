import clusto
from clusto.drivers import *

class HostnameMixin:
    """Provides hostname functionality.

    Hostnames are stored on a per-port basis, and multiple hostnames can be
    associated with a port.  This mixin expects to find a _primary_port
    attribute which tells it what port is the default for get_hostname() and
    set_hostname().
    """

    # default to the first ethernet port
    _primary_port = "nic-eth-1"

    def set_hostname(hostname, port_type=None, port_number=None):
        """Set the primary hostname for a port.  The primary hostname for a
        port is the name that the IP address associated with the interface
        resolves to.

        For example: if a host has two ethernet ports, eth0 and eth1, and
        eth0's IP is 216.82.5.62, then the primary hostname for eth0 is
        web40.lindenlab.com.  This host also has the IP 10.3.3.54
        (int.web40.lindenlab.com) on eth0:1, but this hostname is not the
        primary hostname for the interface.  This is somewhat arbitrary.

        Ultimately, the host considers its "hostname" to be this primary
        hostname for the primary port.

        To set the hostname for a different port, pass the port in the port.
        arguments.
        """

        

    def set_alias(hostname, port_type=None, port_num=None):
        """Set a secondary hostname for a port.  This can be the hostname
        for an aliased interface (e.g. eth0:1) or a DNS alias (CNAME record).
        """


    def get_hostname(port_type=None, port_num=None):
        """Gets the primary hostname for a given port.
        """

    def get_aliases(port_type=None, port_num=None):
        """Gets all aliases for a given port.
        """

    def get_all_hostnames(port_type=None, port_num=None):
        """Gets all names this host may be referred to as (primary and alias
        hostnames for all ports).
        """
