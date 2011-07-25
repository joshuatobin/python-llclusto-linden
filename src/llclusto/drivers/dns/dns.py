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

    def _get_service_group_instance(self, service_group):
        """
        """
        try:
            pool = clusto.get_by_name(service_group)
        except LookupError:
            raise InvalidDNSServiceGroup("DNS service group: %s does not exist." % service_group) 
        else:
            return pool

    def create_dns_service_group(self, service_group):
        """Creates a new clusto Pool for logical grouping of DNS records.
        """
        pool = DNSService(service_group)

    def get_dns_service_groups(self):
        """Returns a list of DNS Service groups this host belongs to.
        """
        return self.parents(clusto_types=['pool'], clusto_drivers=['dnsservice'])

    def set_dns_service_group(self, service_group):
        """Inserts a dns record into a dns service group for logical grouping of records.
        """

        pool = self._get_service_group_instance(service_group)
        pool.insert(self)

    def unset_dns_service_group(self, service_group):
        """Removes a dns record from a dns service group.
        """
        pool = self._get_service_group_instance(service_group)
        pool.remove(self)
        
class DNSService(Pool):
    """ This class allows for DNSRecords to be placed into clusto pools for logical
    grouping of records.
    """

    _driver_name = "dnsservice"


    
