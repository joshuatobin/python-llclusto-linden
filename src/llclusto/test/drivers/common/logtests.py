import llclusto
from llclusto.test import testbase
from llclusto.drivers import LindenEquipment, LogMixin, LogEventType
import datetime 

class TestLog(LindenEquipment, LogMixin):
    _clusto_type = "testlog"
    _driver_name = "testlogdriver"

class LogTests(testbase.ClustoTestBase):

    def data(self):
        self.log_event_type = LogEventType("test event")
        self.host = TestLog()
        self.log_event = self.host.add_log_event(user="test",
                                    event_type=self.log_event_type,
                                    timestamp=datetime.datetime.utcnow(),
                                    description="test description",
                                    test_param = "test")

    def test_get_log_event(self):
        self.assertEquals(self.host.get_log_events(), [self.log_event])
        
