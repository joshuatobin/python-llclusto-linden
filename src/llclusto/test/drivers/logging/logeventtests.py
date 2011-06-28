import clusto
import llclusto
import datetime
from llclusto.test import testbase
from llclusto.drivers import LogEventType, LogEvent, LindenServer, ServerClass

class ClassLServer(LindenServer):
    _driver_name = "classlserver"
    _server_class_name = "Class L Server"


class LogEventTests(testbase.ClustoTestBase):


    def data(self):
        llclusto.drivers.HostState('up')
        LogEventType("test event")
        ServerClass("Class L Server", num_cpus=3, cores_per_cpu=3, ram_size=19, disk_size=230)
        self.host = ClassLServer("hostx")
        

    def test_log_event_creation(self):
        l = LogEvent(source_entity = self.host, 
                     user="test", 
                     event_type=clusto.get_by_name("test event"), 
                     timestamp=datetime.datetime.utcnow(), 
                     description="test description",
                     test_param = "test")
        self.assertEquals(l.source_entity, self.host)
        self.assertEquals(l.user, "test")
        self.assertEquals(l.event_type, clusto.get_by_name("test event"))
        self.assertEquals(type(l.timestamp), datetime.datetime)
        self.assertEquals(l.description, "test description")
        self.assertEquals(l.test_param, "test")
        self.assertRaises(TypeError, LogEvent)


    def test_source_entity(self):
        host2 = ClassLServer("host2")
        self.assertRaises(TypeError,
                          LogEvent,
                          source_entity=123,
                          user="test",
                          event_type=clusto.get_by_name("test event"),
                          timestamp=datetime.datetime.utcnow(),
                          description="test description",
                          test_param = "test")
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        self.assertRaises(TypeError, l.set_source_entity, 123)
        l.source_entity = host2
        self.assertEquals(l.source_entity, host2)
        self.assertEquals(l.attrs(key="source_entiry"), self.host.references(key="source_entity"))


    def test_user(self):
        self.assertRaises(TypeError,
                          LogEvent,
                          source_entity=self.host,
                          user=123,
                          event_type=clusto.get_by_name("test event"),
                          timestamp=datetime.datetime.utcnow(),
                          description="test description",
                          test_param = "test")
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        self.assertRaises(TypeError, l.set_user, 123)
        l.user = "test2"
        self.assertEquals(l.user, "test2")


    def test_event_type(self):
        self.assertRaises(TypeError,
                          LogEvent,
                          source_entity=self.host,
                          user="test",
                          event_type="test event",
                          timestamp=datetime.datetime.utcnow(),
                          description="test description",
                          test_param = "test")
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        self.assertRaises(TypeError, l.set_event_type, "test event")
        l.event_type = LogEventType("test2 event")
        self.assertEquals(l.event_type, clusto.get_by_name("test2 event"))


    def test_timestamp(self):
        self.assertRaises(TypeError,
                          LogEvent,
                          source_entity=self.host,
                          user="test",
                          event_type=clusto.get_by_name("test event"),
                          timestamp="12:00",
                          description="test description",
                          test_param = "test")
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        self.assertRaises(TypeError, l.set_timestamp, "12:00")
        cur_time = datetime.datetime.utcnow()
        l.timestamp = cur_time
        self.assertEquals(l.timestamp, cur_time)


    def test_description(self):
        self.assertRaises(TypeError,
                          LogEvent,
                          source_entity=self.host,
                          user="test",
                          event_type=clusto.get_by_name("test event"),
                          timestamp=datetime.datetime.utcnow(),
                          description=123,
                          test_param = "test")
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        self.assertRaises(TypeError, l.description, 123)
        l.description = "test description2"
        self.assertEquals(l.description, "test description2")


    def test_optional_param(self):
        l = LogEvent(source_entity = self.host,
                     user="test",
                     event_type=clusto.get_by_name("test event"),
                     timestamp=datetime.datetime.utcnow(),
                     description="test description",
                     test_param = "test")
        l.test_param = "test2"
        self.assertEquals(l.test_param, "test2")
        self.assertEquals(l.attr_value(key="test_param" ,subkey = "_extra"), "test2")


    def test_get_log_events(self):
        date1 = datetime.datetime(1901, 1, 1, 1, 1, 1, 1)
        date2 = datetime.datetime(2010, 1, 1, 1, 1, 1, 1)
        date3 = datetime.datetime(2000, 1, 1, 1, 1, 1, 1)
        host2 = ClassLServer("host2")
        event_type2 = LogEventType("test2 event")

        log1 = LogEvent(source_entity = self.host,
                        user="test1",
                        event_type=clusto.get_by_name("test event"),
                        timestamp=date1,
                        description="test description",
                        test_param = "test2")
        log2 = LogEvent(source_entity = self.host,
                        user="test2",
                        event_type=event_type2,
                        timestamp=date2,
                        description="test description",
                        test_param = "test2")        
        log3 = LogEvent(source_entity = host2,
                        user="test1",
                        event_type=clusto.get_by_name("test event"),
                        timestamp=date3,
                        description="test description",
                        test_param = "test3")

        self.assertEquals(sorted(LogEvent.get_log_events(user="test1")), sorted([log1, log3]))
        self.assertEquals(sorted(LogEvent.get_log_events(event_type=event_type2)), [log2])
        self.assertEquals(sorted(LogEvent.get_log_events(source_entity=self.host)), sorted([log1, log2]))
        self.assertEquals(sorted(LogEvent.get_log_events(start_timestamp=datetime.datetime(1902, 1, 1, 1, 1, 1, 1))), sorted([log2, log3]))
        self.assertEquals(sorted(LogEvent.get_log_events(end_timestamp=datetime.datetime(2012, 1, 1, 1, 1, 1, 1))), sorted([log1, log2, log3]))
        self.assertEquals(sorted(LogEvent.get_log_events(start_timestamp=datetime.datetime(2000, 1, 1, 1, 1, 1, 1),
                                                         end_timestamp=datetime.datetime(2011, 1, 1, 1, 1, 1, 1))), sorted([log2, log3]))
        self.assertEquals(sorted(LogEvent.get_log_events(start_timestamp=datetime.datetime(1902, 1, 1, 1, 1, 1, 1),
                                                         end_timestamp=datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                                                         user="test1")), [log3])
        self.assertEquals(sorted(LogEvent.get_log_events(start_timestamp=datetime.datetime(2001, 1, 1, 1, 1, 1, 1),
                                                         end_timestamp=datetime.datetime(2011, 1, 1, 1, 1, 1, 1),
                                                         event_type=event_type2)), [log2])
        self.assertEquals(sorted(LogEvent.get_log_events(event_type=clusto.get_by_name("test event"), user="test1", 
                                                         source_entity=self.host)), sorted([log1]))

