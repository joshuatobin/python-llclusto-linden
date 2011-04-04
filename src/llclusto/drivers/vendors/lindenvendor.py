import clusto
from clusto.drivers import *

class LindenVendor(Driver):
    """
    """

    _driver_name = 'lindenvendor'
    _clusto_type = 'vendor'

    _properties = {'address': None, 'phone': None, 'fax': None, 'billing_address': None, 'shipping_address': None, \
                   'notes': None, 'website': None, 'email': None}

    def __init__(self, name, address, phone, **kwargs):
        super(LindenVendor, self).__init__(name, address=address, phone=phone, **kwargs)

        

    
