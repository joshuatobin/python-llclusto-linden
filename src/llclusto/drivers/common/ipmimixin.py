import clusto
from clusto.drivers import *

class LindenIPMIMixin():
    """ Provides IPMI functionality.
    
    The IPMI interface will be associated with a single port on 
    the host. The port can be shared with an existing interface(ie eth0),
    specified by _ipmi_port_type and _ipmi_port_num.
    """
    
    # IPMI shares its interface with the first ethernet port. 
    _ipmi_port_type = 'nic-eth'
    _ipmi_port_num = 1

    def set_ipmi_info(self, ipmi_hostname):
        """ Set the ipmi hostname associated with the ipmi interface"""
        if not isinstance(ipmi_hostname, basestring):
            raise TypeError("The IPMI hostname must be a string") 
        self.set_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname", ipmi_hostname)
    
    def get_ipmi_info(self):
        """ Get the hostname for the ipmi interface"""
        return self.get_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname")

    def del_ipmi_info(self):
        """ Delete the ipmi_hostname"""
        self.del_port_attr(self._ipmi_port_type, self._ipmi_port_num, "ipmi_hostname")

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
