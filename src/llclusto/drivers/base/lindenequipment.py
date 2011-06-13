import clusto
from clusto.drivers import *
from llclusto.drivers.common import LogMixin

class LindenEquipment(Driver, LogMixin):

    _driver_name="lindenequipment"
    _clusto_type="device"
    
    def __init__(self, *args, **kwargs):
        try:
            name_manager = clusto.get_by_name("LindenEquipment_name_manager")
        except LookupError:
            name_manager = SimpleNameManager("LindenEquipment_name_manager", basename="LL", digits=10)

        try:
            clusto.begin_transaction()

            name, num = name_manager.allocator()

            super(LindenEquipment, self).__init__(name, *args, **kwargs)

            name_manager.allocate(self, name)

            clusto.commit()
        except:
            clusto.rollback_transaction()
            raise

    def __repr__(self):
        if hasattr(self, "get_hostname"):
            return "%s(hostname=%s, name=%s, type=%s, driver=%s)" % (self.__class__.__name__,
                                                                     self.get_hostname(),
                                                                     self.entity.name,
                                                                     self.entity.type,
                                                                     self.entity.driver)
        else:
            return super(LindenEquipment, self).__repr__()
