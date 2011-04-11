import clusto
from clusto.drivers import Driver

class PGIImage(Driver):
    """
    """

    _driver_name = "pgi_image"
    _clusto_type = "pgi_image"


    def get_image_associations(self):
        """Returns a list of hosts this PGI image is associated with. 
        """
        pass        

    def get_systemimager_stored_on(self):
        """Returns a list of PGI systemimagers this image is stored on.
        """
        pass


        

        
            
