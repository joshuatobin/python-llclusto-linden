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
        


