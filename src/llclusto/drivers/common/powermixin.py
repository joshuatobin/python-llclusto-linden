import clusto
import llclusto
import time
from clusto.drivers import *
from llclusto.exceptions import LLClustoError

class MissingPowerManagementInfo(LLClustoError):
    pass

class LindenPowerMixin():
    """
    """
    def get_power_management_info(self):
        """
        """
        pdu_connections = []
        port_info = self.port_info
        try:
            if self.has_ipmi():
                return [{'ipmi': self.ipmi[0]}]
            elif 'pwr-nema-5' in port_info:
                for port_num in port_info['pwr-nema-5']:
                    if port_info['pwr-nema-5'][port_num]['connection']:
                        pdu_connections.append({'pdu': port_info['pwr-nema-5'][port_num]['connection'],
                                                'port': port_info['pwr-nema-5'][port_num]['otherportnum']})
                return pdu_connections
            else:
                return pdu_connections
        except (KeyError, AttributeError, IndexError):
            pdu_connections = []

    def power_on(self):
        """
        """
        if self.has_ipmi():
            return self.ipmi_power_on()
        
        power_mgmt_info = self.get_power_management_info()
        
        if not power_mgmt_info:
            raise MissingPowerManagementInfo("Could not find any power management information...")
        
        for pdu in power_mgmt_info:
                pdu['pdu'].power_on_port(pdu['port'])
        
        return "Powered on..."

    def power_off(self):
        """
        """
        if self.has_ipmi():
            return self.ipmi_power_off()
        
        power_mgmt_info = self.get_power_management_info()
        
        if not power_mgmt_info:
            raise MissingPowerManagementInfo("Could not find any power management information...")
        
        for pdu in power_mgmt_info:
                pdu['pdu'].power_off_port(pdu['port'])
        
        return "Powered off..."
    
    def power_cycle(self):
        """
        """
        if self.has_ipmi():
            return self.ipmi_power_cycle()
        
        power_mgmt_info = self.get_power_management_info()
        
        if not power_mgmt_info:
            raise MissingPowerManagementInfo("Could not find any power management information...")

        # If a device has two pdus its best to power them off, then back on rather than just power cycling...
        for pdu in power_mgmt_info:
                pdu['pdu'].power_off_port(pdu['port'])

        time.sleep(3)
        for pdu in power_mgmt_info:
                pdu['pdu'].power_on_port(pdu['port'])

        return "Power cycled..."
