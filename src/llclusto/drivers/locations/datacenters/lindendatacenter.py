import clusto
from clusto.drivers.locations.datacenters import BasicDatacenter
from llclusto.drivers.common import LogMixin

class LindenDatacenter(BasicDatacenter, LogMixin):
    """
    LindenDatacenter driver.
    """

    _clusto_type="datacenter"
    _driver_name="lindendatacenter"

    _properties = {'address': None, 'phone': None, 'billing_address': None, 'shipping_address': None, \
                   'notes': None, 'website': None, 'email': None, 'remote_hands_email': None }

    def __init__(self, name, address, phone, remote_hands_email, **kwargs):
        super(LindenDatacenter, self).__init__(name, address=address, phone=phone,\
                                               remote_hands_email=remote_hands_email, **kwargs)


                   
