import clusto
from clusto.drivers import Driver

class PGIImage(Driver):
    """Driver for PGI Images.    
    """
    _driver_name = "pgi_image"
    _clusto_type = "pgi_image"

    def get_image_associations(self):
        """Returns a list of hosts this PGI image is associated with. 
        """
        return self.referencers(key='pgi_image')

    def get_si_servers_stored_on(self):
        """Returns a list of PGI systemimagers this image is stored on.
        """
        return self.parents(subkey="pgi-image")


        

        
            
