import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers.dns import DNSService, DNSRecord
class LindenDNSTests(testbase.ClustoTestBase):
    """
    Test Suite for DNS Records.
    """
    def test_dns_service_group(self):
        """
        Test for dns service groups
        """
        pool = DNSService("webservers")
        self.assertEquals(pool.driver, 'dnsservice')
        self.assertEquals(pool.type, 'pool')
        self.assertEquals(pool.name, 'webservers')


    def test_dns_record(self):
        """
        Test for dns records"
        """

        record = DNSRecord("hostname.lindenlab.com")
        self.assertEquals(record.name, "hostname.lindenlab.com")
        self.assertEquals(record.type, "dns_record")
        self.assertEquals(record.driver, "dns_record")
        self.assertEquals(record.comment, None)

        record.comment = "Shiny New Comment"
        self.assertEquals(record.comment, "Shiny New Comment")
        
        record.create_dns_service_group("bacula")

        bacula = clusto.get_by_name("bacula")
        self.assertEquals(bacula.type, "pool")

        record.set_dns_service_group("bacula")

        record.create_dns_service_group("loadbalancers")
        lb = clusto.get_by_name("loadbalancers")

        record.set_dns_service_group("loadbalancers")

        self.assertEquals(record.get_dns_service_groups(), [bacula, lb])

        record.unset_dns_service_group("bacula")

        self.assertEquals(record.get_dns_service_groups(), [lb])

