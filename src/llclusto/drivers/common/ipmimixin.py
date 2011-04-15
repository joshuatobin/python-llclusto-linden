import clusto
from clusto.drivers import *
from llclusto.exceptions import LLClustoError

class IPMIHostnameError(LLClustoError):
    pass

class LindenIPMIMixin():
    """ Provides IPMI functionality.
    
    The IPMI interface will be associated with a single port on 
    the host. The port can be shared with an existing interface(ie eth0),
    specified by _ipmi_port_type and _ipmi_port_num.
    """
    
    # IPMI shares its interface with the first ethernet port. 
    _ipmi_port_type = 'nic-eth'
    _ipmi_port_num = 1

    def set_ipmi_info(self, ipmi_hostname, ipmi_mac):
        """ Set the ipmi hostname associated with the ipmi interface"""
        try:
            clusto.begin_transaction()

            if not isinstance(ipmi_hostname, basestring):
                raise TypeError("The IPMI hostname must be a string") 
            elif not ipmi_hostname.startswith("mgmt"):
                raise IPMIHostnameError("IPMI hostname must start with 'mgmt'")
            if not isinstance(ipmi_mac, basestring):
                raise TypeError("The IPMI mac address must be a string")

            self.set_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname", ipmi_hostname)
            self.set_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_mac", ipmi_mac)

            clusto.commit()
        except:
            clusto.rollback_transaction()
            raise
    
    def get_ipmi_info(self):
        """ Get the hostname and mac address as a tuple for the ipmi interface. """
        ipmi_hostname = self.get_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname")
        ipmi_mac = self.get_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_mac")
        if not ipmi_hostname and not ipmi_mac:
            return None
        else:
            return (ipmi_hostname, ipmi_mac)

    def del_ipmi_info(self):
        """ Delete the ipmi hostname and mac address attributes. """
        try:
            clusto.begin_transaction()

            self.del_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname")
            self.del_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_mac")

            clusto.commit()
        except:
            clusto.rollback_transaction()
            raise

    def ipmi_powercycle(self):
        """ """
        pass

    def ipmi_powerdown(self):
        """ """
        pass
    
    def ipmi_powerup(self):
        """ """
        pass
    
    def ipmi_pxeboot(self):
        """ """
        pass
    
    ipmi = property(get_ipmi_info, set_ipmi_info, del_ipmi_info)
