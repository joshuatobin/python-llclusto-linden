import clusto
import llclusto
from llclusto.test import testbase
from llclusto.drivers import Class5Server, ServerClass
from llclusto.drivers.devices.servers import PGIImage

class LindenPGITests(testbase.ClustoTestBase):
    """ 
    """

    def test_get_image_association(self):
        """
        Test for get_image_association() fucntion.
        """
        class5 = ServerClass("Class 5", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=138)

        server0 = Class5Server("pgi0.lindenlab.com")
        server1 = Class5Server("pgi1.lindenlab.com")

        image0 = PGIImage("pgi-image0")
        image1 = PGIImage("pgi-image1")


        self.assertEquals(image0.type, 'pgi_image')
        self.assertEquals(image1.type, 'pgi_image')

        self.assertEquals(server0.pgi_image, None)
        self.assertEquals(server1.pgi_image, None)
        
        server0.pgi_image = image0
        server1.pgi_image = image1
        self.assertEquals(server0.pgi_image.name, 'pgi-image0')
        self.assertEquals(server1.pgi_image.name, 'pgi-image1')

        self.assertEquals(type(image0.get_image_associations()), list)

        self.assertEquals(image0.get_image_associations(), [server0])
                            
        self.assertEquals(image1.get_image_associations(), [server1])

        server1.pgi_image = image0
        self.assertEquals(image0.get_image_associations(), [server0, server1])
        
        self.assertEquals(image1.get_image_associations(), [])

        server0.pgi_image = image1
        server1.pgi_image = image0
        self.assertEquals(server0.pgi_image.name, 'pgi-image1')
        self.assertEquals(server1.pgi_image.name, 'pgi-image0')

        
    def test_get_si_server_image_stored_on(self):
        """
        Tests for the get_si_server_image_stored_on() function.
        """

        class5 = ServerClass("Class 5", num_cpus=1, cores_per_cpu=4, ram_size=4096, disk_size=138)
        server3 = Class5Server("pgi3.lindenlab.com")
        server4 = Class5Server("pgi4.lindenlab.com")

        image3 = PGIImage("pgi-image3")
        image4 = PGIImage("pgi-image4")


        self.assertEquals(server3.get_stored_pgi_images(), [])
        self.assertEquals(server4.get_stored_pgi_images(), [])

        server3.add_stored_pgi_image(image3)
        self.assertEquals(server3.get_stored_pgi_images(), [image3])
        self.assertEquals(image3.get_si_server_image_stored_on(), [server3])

        server3.add_stored_pgi_image(image4)
        self.assertEquals(server3.get_stored_pgi_images(), [image3, image4])


        server4.add_stored_pgi_image(image3)
        self.assertEquals(image3.get_si_server_image_stored_on(), [server3, server4])

        server3.delete_stored_pgi_image(image3)
        self.assertEquals(image3.get_si_server_image_stored_on(), [server4])

        

