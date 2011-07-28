import clusto
from clusto.drivers import Driver, Pool

class InvalidDNSRecord(Exception):
    """
    Error class for Invalid DNS Record types.
    """
    pass

class InvalidDNSServiceGroup(Exception):
    """
    Error class for Invalid DNS Service Group.
    """
    pass

class DNSRecord(Driver):
    """Driver for DNS records.
    """
    _driver_name = "dns_record"
    _clusto_type = "dns_record"

    _properties = {'comment': None}

    def get_dns_service_groups(self):
        """Returns a list of DNS Service groups this host belongs to.
        """
        return self.parents(clusto_types=['pool'], clusto_drivers=['dnsservice'])

class DNSService(Pool):
    """ This class allows for DNSRecords to be placed into clusto pools for logical
    grouping of records.
    """

    _driver_name = "dnsservice"

    _properties = {'comment': None}

    
