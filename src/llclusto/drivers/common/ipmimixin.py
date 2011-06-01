import clusto
from clusto.drivers import *
from llclusto.exceptions import LLClustoError
import commands
import time

IPMI_TOOL = '/usr/bin/ipmitool -I lanplus -H %s -U ADMIN -P ADMIN %s'

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

    def _run_ipmi_cmd(self, action):
        """ Run impitool and return the exit code and output via
        STDOUT.
        """
        cmd_out = commands.getstatusoutput(IPMI_TOOL % (self.ipmi[0], action))
        return cmd_out[0], cmd_out[1]

    def ipmi_power_on(self):
        """Attempts to turn ipmi enabled host on. It will
        then check the status, and return True if the power
        is on and False otherwise.
        """
        ret_val, result = self._run_ipmi_cmd('power on')

        if(ret_val == 0):
            #ipmi commands take a few moments to process
            time.sleep(5)
            msg = self.ipmi_power_status()
            if (msg == "Chassis Power is on"):
                return "Chassis powered on..."
            else:
                return "Error: %s" % msg
        else:
            return "Error: %s" % msg

    def ipmi_power_off(self):
        """Attempts to turn ipmi enabled host on. It will
        then check the status, and return True if the power
        is off and False otherwise.
        """
        ret_val, result =  self._run_ipmi_cmd('power off')

        if(ret_val == 0):
                #ipmi commands take a few moments to process
            time.sleep(5)
            msg = self.ipmi_power_status()
            if (msg == "Chassis Power is off"):
                return "Chassis Powered off..."
            else:
                return "Error: %s" % msg
        else:
            return "Error: %s" % msg

    def ipmi_power_cycle(self):
        """Performs and power cycle command via IPMI.
        This can potentially put the filesystem in a
        bad state, but since we are in the business of
        reusable hosts, power cycling fits our needs.
        After the power cycle we will wait for a
        sign of reboot(namely that the chassis is
        powered on). If after 30 seconds the chassis
        is still powered off, force a power on command.
        If that fails, give up and cry.
        """
        ret_val, result = self._run_ipmi_cmd('power cycle')

        if(ret_val == 0):
            #ipmi commands take a few moments to process
            time.sleep(5)
            if not self._wait_for_reboot():
                msg = self.ipmi_power_on()
                if not (msg == "Chassis powered on..."):
                    return "Unable to power cycle host..."
                return "Power cycle successful..."
            return "Power cycle successful..."
        else:
            return "Error: %s" % msg

    def ipmi_power_status(self):
        """Checks the power status of a ipmi enabled hosts
        and returns the status as a string
        """
        ret_val, result = self._run_ipmi_cmd('power status')        
        return result

    def _wait_for_reboot(self, wait_time=15):
        """ Waits for ipmi enabled host to be turned on. Accepts the
        ipmi hostname and the wait time in seconds(defaults to 15).
        Returns True if chassis is on before the wait time is up.
        Otherwise returns False meaning the chassis is still off.
        """
        #measured in seconds
        while (wait_time > 0):
            result = self.ipmi_power_status()
            if (result == "Chassis Power is on"):
                wait_time = 0
                ret_val = True
            else:
                time.sleep(5)
                wait_time -= 5
                ret_val = False
        return ret_val

    ipmi = property(get_ipmi_info, set_ipmi_info, del_ipmi_info)
