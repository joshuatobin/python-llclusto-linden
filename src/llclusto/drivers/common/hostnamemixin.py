import clusto
from clusto.drivers import *

class LindenHostnameMixin(object):
    """Provides hostname functionality.

    Hostnames are stored on a per-port basis, and multiple hostnames can be
    associated with a port.  This mixin expects to find a _primary_port
    attribute which tells it what port is the default for get_hostname() and
    set_hostname().
    """

    # default to the first ethernet port
    _primary_port_type = "nic-eth"
    _primary_port_num = 1

    def _resolve_port(self, port_type, port_num):
        if port_type is None:
            port_type = self._primary_port_type
            port_num = self._primary_port_num

        num = self._ensure_portnum(port_type, port_num)

        return (port_type, num)

    def set_hostname(self, hostname, port_type=None, port_num=None):
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
        
        port, num = self._resolve_port(port_type, port_num)

        self.set_port_attr(port, num, "hostname", hostname)

    def del_hostname(self, port_type=None, port_num=None):
        """Delete the primary hostname for a port.  Defaults to the primary 
        port."""

        port, num = self._resolve_port(port_type, port_num)

        self.del_port_attr(port, num, "hostname")

    def add_hostname_alias(self, hostname, port_type=None, port_num=None):
        """Set a secondary hostname for a port.  This can be the hostname
        for an aliased interface (e.g. eth0:1) or a DNS alias (CNAME record).
        """

        port, num = self._resolve_port(port_type, port_num)

        existing = self.attrs(key=self._port_key(port), number=num, subkey="hostname-alias", value=hostname)

        if len(existing) > 0:
            raise ValueError("%s already has the hostname %s on %s-%d" % (self.entity.name, hostname, port, num))

        self.add_port_attr(port, num, "hostname-alias", hostname)

    def del_hostname_alias(self, hostname, port_type=None, port_num=None):
        """Remove a secondary hostname for a port."""

        port, num = self._resolve_port(port_type, port_num)

        self.del_port_attr(port, num, "hostname-alias", hostname)

    def get_hostname(self, port_type=None, port_num=None):
        """Gets the primary hostname for a given port.
        """

        port, num = self._resolve_port(port_type, port_num)

        return self.get_port_attr(port, num, "hostname")

    def get_hostname_aliases(self, port_type=None, port_num=None):
        """Gets all aliases for a given port.
        """

        port, num = self._resolve_port(port_type, port_num)

        attrs = self.attrs(key=self._port_key(port), number=num, subkey="hostname-alias")

        return [attr.value for attr in attrs]

    def get_all_hostnames(self):
        """Gets all names this host may be referred to as (primary and alias
        hostnames for all ports).
        """

        hostnames = []

        for port_type in self._portmeta.keys():
            for num in xrange(1, self._portmeta[port_type]['numports'] + 1):
                hostname = self.get_hostname(port_type, num)

                if hostname is not None:
                    hostnames.append(hostname)

                hostnames.extend(self.get_hostname_aliases(port_type, num))

        return hostnames


    hostname = property(get_hostname, set_hostname, del_hostname)
