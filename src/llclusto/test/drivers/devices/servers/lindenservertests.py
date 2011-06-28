import llclusto
from llclusto.test import testbase

from llclusto.drivers import LindenServer, ServerClass, RevertPGIImageError, LindenIPMIMixin, PGIImage, HostState

class ClassXServer(LindenServer):
    """A subclass of LindenServer specifically here to let us test LindenServer.
    LindenServer itself is not designed to be instantiated.
    """

    _driver_name = "classxserver"

    _server_class_name = "Class X Server"

class ClassYServer(LindenServer, LindenIPMIMixin):
    """This Driver has class name "Class Y Server", but there won't be any 
    ServerClass entity named "Class Y Server".  Trying to instantiate a
    ClassYServer should result in an error because the server class does not
    exist.
    """

    _driver_name = "classyserver"

    _server_class_name = "Class Y Server"

class LindenServerTests(testbase.ClustoTestBase):
    def data(self):
        classX = ServerClass("Class X Server", num_cpus=3, cores_per_cpu=3, ram_size=19, disk_size=230)
    
    def test___init__(self):
        """LindenServer.__init__ should set the server's hostname and associate with the server class"""
        server = ClassXServer("test1.lindenlab.com")
        
        self.assertEquals(server.server_class.name, "Class X Server", "Server was not properly associated with its server class.")

        self.assertEquals(server.hostname, "test1.lindenlab.com", "Hostname was not properly set.")

        self.assertEquals(llclusto.get_by_hostname("test1.lindenlab.com"), [server], "Cannot find server by using llclusto.get_by_hostname()")

        # Test whether I'm able to create a server whose _server_class_name does not exist.
        self.assertRaises(LookupError, lambda: ClassYServer("test2.lindenlab.com"))

        self.assertEquals(llclusto.get_by_hostname("test2.lindenlab.com"), [], "When creation of a ClassYServer failed because there is no ServerClass named Class Y Server, the ClassYServer entity was still created (transaction should have been rolled back).")

    def test___getattr__(self):
        """LindenServer.__getattr__ should allow retrieving of properties from the server class"""

        server = ClassXServer("test1.lindenlab.com")

        self.assertEquals(server.num_cpus, 3, "Cannot access server class's num_cpus through server.num_cpus")
        
    def test___setattr__(self):
        """LindenServer.__setattr__ should prevent setting of properties stored in the server class"""

        server = ClassXServer("test1.lindenlab.com")

        def assign_num_cpus(server):
            server.num_cpus = 3

        # Test whether I'm able to set a server's number of CPUs without exception
        self.assertRaises(AttributeError, assign_num_cpus, server)

    def test_pgi_image(self):
        server = ClassXServer("test1.lindenlab.com")

        def assign_non_image(server):
            server.pgi_image = "notanimage"

        self.assertRaises(TypeError, assign_non_image, server) # Was able to assign something that is not a PGIImage to server.pgi_image

        image1 = PGIImage("image1")
        image2 = PGIImage("image2")

        server.pgi_image = image1

        self.assertEquals(server.pgi_image, image1)

        server.pgi_image = image2

        self.assertEquals(server.previous_pgi_image, image1, "When setting pgi_image, old image was not stored in previous_pgi_image")

    def test_previous_pgi_image(self):
        server = ClassXServer("test1.lindenlab.com")

        image1 = PGIImage("image1")

        def assign_previous_pgi_image(server):
            server.previous_pgi_image = image1

        self.assertRaises(AttributeError, assign_previous_pgi_image, server) # Should not be able to set read-only property previous_pgi_image

    def test_revert_pgi_image(self):
        server = ClassXServer("test1.lindenlab.com")

        image1 = PGIImage("image1")
        image2 = PGIImage("image2")

        server.pgi_image = image1

        self.assertRaises(RevertPGIImageError, lambda: server.revert_pgi_image()) # "Revert should fail when there was no previous associated image

        server.pgi_image = image2

        server.revert_pgi_image()

        self.assertEquals((server.pgi_image, server.previous_pgi_image), (image1, image2), "Revert did not properly swap current and previous image")

    def test_add_stored_pgi_image(self):
        server = ClassXServer("test1.lindenlab.com")

        server.add_stored_pgi_image("image1")

        self.assert_("image1" in server)

    def test_get_stored_pgi_images(self):
        server = ClassXServer("test1.lindenlab.com")

        image1 = PGIImage("image1")
        image2 = PGIImage("image2")

        server.add_stored_pgi_image(image1)

        self.assertEqual([image1], server.get_stored_pgi_images())

        server.add_stored_pgi_image(image2)

        self.assertEqual([image1, image2], server.get_stored_pgi_images())

    def test_delete_stored_pgi_image(self):
        server = ClassXServer("test1.lindenlab.com")

        image1 = PGIImage("image1")
        image2 = PGIImage("image2")

        server.add_stored_pgi_image(image1)

        self.assert_(image1 in server)

        server.delete_stored_pgi_image(image1)

        self.assert_(image1 not in server, "Deleting an image from a PGI systemimager did not actually remove the image.")

        self.assertRaises(LookupError, lambda: server.delete_stored_pgi_image(image1)) # Exception should be raised when attempting to delete an image not stored on a PGI systemimager

    def test_has_ipmi(self):
        server1 = ClassXServer("test1.lindenlab.com")
        classY = ServerClass("Class Y Server", num_cpus=3, cores_per_cpu=3, ram_size=19, disk_size=230)
        server2 = ClassYServer("test2.lindenlab.com")
        
        self.assertFalse(server1.has_ipmi(), "Server has ipmi configured when it should not.")
        server2.set_ipmi_info("mgmt.test2.lindenlab.com", "01:02:03:04:05:06")
        self.assertTrue(server2.has_ipmi(), "Server does not have ipmi configured when it should.")
    
    def test_state(self):
        server1 = ClassXServer("test1.lindenlab.com")
        server2 = ClassXServer("test2.lindenlab.com")
        
        state1 = HostState("state 1")
        state2 = HostState("state 2")
        
        server1.state = "state 1"
        
        self.assertEquals(server1.state, "state 1")
        self.assertEquals(state1.contents(), [server1])
        
        server2.state = "state 2"
        server1.state = "state 2"
        
        self.assertEquals(server1.state, "state 2")
        self.assertEquals(sorted(state2.contents()), sorted([server1, server2]))
        self.assertEquals(state1.contents(), [])

    def test_default_state(self):
        server1 = ClassXServer("test1.lindenlab.com")

        self.assertEquals(server1.state, "up")
