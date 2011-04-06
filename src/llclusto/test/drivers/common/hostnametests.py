import llclusto
from llclusto.test import testbase

from llclusto.drivers import LindenEquipment, LindenHostnameMixin
from clusto.drivers import Driver, PortMixin
from clusto.exceptions import ConnectionException

class TestHostname3Ports(LindenEquipment, LindenHostnameMixin, PortMixin):
    _clusto_type = "testhostname3ports"
    _driver_name = "testhostname3portsdriver"

    _primary_port_type = "nic-eth"
    _primary_port_num = 2

    _portmeta = {'pwr-nema-5': {'numports':1},
                 'nic-eth': {'numports':3},
                 'console-serial' : { 'numports':1, }
                 }

class TestHostname(LindenEquipment, LindenHostnameMixin, PortMixin):
    _clusto_type = "testhostname"
    _driver_name = "testhostnamedriver"


class LindenHostnameTests(testbase.ClustoTestBase):
    """ Test linden hostname framework. """
    
    def testHostnameCreation(self):
        d1 = TestHostname()
        d2 = TestHostname3Ports()
        
        d1.set_hostname('foo1-0', 'nic-eth', 1)
        d1_eth0 = d1.hostname
        d1_eth1 = d1.get_hostname('nic-eth', 2)

        d2.set_hostname('foo2-0', 'nic-eth', 1)
        d2.set_hostname('foo2-1', 'nic-eth', 2)
        d2.set_hostname('foo2-2', 'nic-eth', 3)

        d2_eth0 = d2.get_hostname('nic-eth', 1)
        d2_eth1 = d2.hostname
        d2_eth2 = d2.get_hostname('nic-eth', 3)

        self.assertEqual(d1_eth0, 'foo1-0')
        self.assertEqual(d1_eth1, None)
        self.assertEqual(d2_eth0, 'foo2-0')
        self.assertEqual(d2_eth1, 'foo2-1')
        self.assertEqual(d2_eth2, 'foo2-2')


    def testGetByHostname(self):
        d1 = TestHostname()
        d1.hostname = 'foo'

        s1 = llclusto.get_by_hostname('foo')

        self.assertEqual(len(s1), 1)

        self.assertEqual(s1[0].hostname, 'foo')


    def testDelHostname(self):
        d1 = TestHostname()
        d1.hostname = 'foo'

        del d1.hostname
        self.assertEqual(d1.hostname, None)


    def testHostnameAliasCreation(self):
        d1 = TestHostname()
        d2 = TestHostname3Ports()

        d1.hostname = 'foo1' 
        d1.add_hostname_alias('bar1-0')
        d2.add_hostname_alias('bar2-0', 'nic-eth', 1)
        d2.add_hostname_alias('bar2-1', 'nic-eth', 2)

        d1_eth0 = d1.get_hostname_aliases()
        d1_eth1 = d1.get_hostname_aliases('nic-eth', 2)

        d2_eth0 = d2.get_hostname_aliases('nic-eth', 1)
        d2_eth1 = d2.get_hostname_aliases()
        d2_eth2 = d2.get_hostname_aliases('nic-eth', 3)

        self.assertEquals(d1_eth0, ['bar1-0'])
        self.assertEquals(d2_eth0, ['bar2-0'])
        self.assertEquals(d2_eth1, ['bar2-1'])
        self.assertEquals(d2_eth2, [])
        
        d1.add_hostname_alias('newalias', 'nic-eth', 1)
        a1 = d1.get_hostname_aliases()
        self.assertEquals(a1, ['bar1-0','newalias'])


    def testDelHostnameAlias(self):
        d1 = TestHostname()

        d1.add_hostname_alias('bar1')
        d1_alias = d1.get_hostname_aliases()
        self.assertEquals(d1_alias, ['bar1'])

        d1.del_hostname_alias('bar1')
        d1_alias = d1.get_hostname_aliases()
        self.assertEquals(d1_alias, [])


    def testGetAllHostnames(self):
        d1 = TestHostname3Ports()
        
        d1.hostname = 'foo1'
        d1.add_hostname_alias('bar1', 'nic-eth', 2)
        d1.add_hostname_alias('barbar1', 'nic-eth', 3)
        
        d1_hostnames = d1.get_all_hostnames()
        self.assertEquals(d1_hostnames, ['foo1', 'bar1', 'barbar1'])
