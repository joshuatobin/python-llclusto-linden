import clusto
import datetime
from clusto.drivers import *
from logeventtype import LogEventType

class LogEvent(Driver):
    """ LogEvent an interface for log events. Every LogEvent contains a user,
    a source entity(the driver that triggered the event, the type of event, 
    the datetime formatted timestamp when the event occured and an optional 
    an description. Each of these variables will be stored in _properties.
    Any other arguments passed in will be stored as clusto attributes.     
    """
    _driver_name = 'logevent'
    _clusto_type = 'logevent'

    _properties = { 'user': None,
                    'source_entity': None,
                    'event_type': None,
                    'timestamp': None,
                    'description': None}

            
    def __init__(self, source_entity, user, event_type, timestamp, description=None, **kwargs):
        """Create a new LogEvent instance
        
        Keyword arguments:
        source_entity -- the source entity that is associated with the log event
        user -- the user that triggered the log event
        event_type -- the type of event that occured
        time_stamp -- the datetime when the log event occured
        description -- the string describing the event (default None)

        """
        try:
            name_manager = clusto.get_by_name("LogEvent_name_manager")
        except LookupError:
            name_manager = SimpleNameManager("LogEvent_name_manager", basename="Log", digits=10)

        try:
            clusto.begin_transaction()

            name, num = name_manager.allocator()
            
            super(LogEvent, self).__init__(name, event_type = event_type,
                                           source_entity =source_entity,
                                           timestamp = timestamp,
                                           user = user,
                                           description = description)

            name_manager.allocate(self, name)
            for key in kwargs:
                self.add_attr(key=key, value=kwargs[key])
            clusto.commit()
        except:
            clusto.rollback_transaction()
            raise


    def __getattr__(self, name):
        """Attribute look up, which will look in _properties,
        then the clusto attribute.
        
        Keyword arguments
        name -- the string containing the attribute name

        """
        try:
            return super(LogEvent, self).__getattr__(name)
        except AttributeError:
            value = self.attr_value(key=name)
            if not value:
                raise AttributeError("Attribute %s does not exist." % name)
            return value


    def __setattr__(self, name, value):
        """Sets the value of an attribute. If the attribute is not in
        _properties, write the value as a clusto attribute.
        
        Keyword arguments
        name -- the string containing the attribute name
        value -- the value of the attribute

        """
        # call property specific function
        if name == "user" :
            self.set_user(value)
        elif name == "event_type":
            self.set_event_type(value)
        elif name == "source_entity":
            self.set_source_entity(value)
        elif name == "timestamp":
            self.set_timestamp(value)
        elif name == "description":
            self.set_description(value)
        # some instance variables are not stored in clusto
        # call the driver's __setattr__ instead
        elif name in ('entity', '_clusto_type', '_driver_name'):
            super(LogEvent, self).__setattr__(name, value)
        # Otherwise store the value as an attribute in clusto
        else:
            self.set_attr(key=name, value=value)


    def set_source_entity(self, source_entity):
        """Sets the source_entity property
        
        Keyword arguments
        source_entity -- the new source_entity to associate with the LogEvent

        """
        if not isinstance(source_entity, Driver):
            raise TypeError("source_entity is a %s, and needs to inherit from Driver" % type(source_entity))
        super(LogEvent, self).__setattr__( "source_entity", source_entity)


    def set_user(self, user):
        """Sets the user property
        
        Keyword arguments
        user -- the new user associated with the LogEvent

        """
        if not isinstance(user, basestring):
            raise TypeError("user is a %s, and needs to be a string" % type(user))
        super(LogEvent, self).__setattr__( "user", user)


    def set_event_type(self, event_type):
        """Sets the event_type property

        Keyword arguments
        event_type -- the new event_type associated with the LogEvent

        """
        if not isinstance(event_type, LogEventType):
            raise TypeError("event_type is a %s, and needs to be a LogEventType" % type(event_type))
        super(LogEvent, self).__setattr__( "event_type", event_type)


    def set_timestamp(self, timestamp):
        """Sets the timestamp property
        
        Keyword arguments
        timestamp -- the new timestamp associated with the LogEvent
        """
        if not isinstance(timestamp, datetime.datetime):
            raise TypeError("timestamp is a %s, and needs to be a datetime" % type(timestamp))
        super(LogEvent, self).__setattr__("timestamp", timestamp)
    

    def set_description(self, description):
        """Sets the description property
        
        Keyword arguments
        description -- the new description associated with the LogEvent
        """
        if description and not isinstance(description, basestring):
            raise TypeError("description is a %s, and needs to be a string" % type(description))
        super(LogEvent, self).__setattr__( "description", description)


    @classmethod
    def get_log_events(self, source_entity=None, user=None, event_type=None, 
                       start_timestamp=None, end_timestamp=None):
        """Looks up the LogEvent instances based on the parameters passed in.
        
        Keyword arguments:
        source_entity -- the source entity that is associated with the log event
        user -- the user that triggered the log event
        event_type -- the type of event that occured
        start_timestamp -- the datetime signalling how far back to search
        end_timestamp -- the datetime signalling when to stop searching

        """

        # This may need more optimization
        sets = []

        if start_timestamp:
            if not end_timestamp:
                end_timestamp=datetime.datetime.utcnow()
            attrs = LogEvent.do_attr_query(start_timestamp=start_timestamp, end_timestamp=end_timestamp)
            sets.append(set([attr.entity for attr in attrs]))

        elif end_timestamp:
            attrs = LogEvent.do_attr_query(start_timestamp=datetime.datetime(1901, 1, 1, 1, 1, 1, 1),
                                           end_timestamp=end_timestamp)
            sets.append(set([attr.entity for attr in attrs]))

        if source_entity:
            attrs = LogEvent.do_attr_query(key="source_entity", value=source_entity)
            sets.append(set([attr.entity for attr in attrs]))
        
        if user:
            attrs = LogEvent.do_attr_query(key="user", value=user)
            sets.append(set([attr.entity for attr in attrs]))

        if event_type:
            attrs = LogEvent.do_attr_query(key="event_type", value=event_type)
            sets.append(set([attr.entity for attr in attrs]))

        if len(sets) < 1:
            return sets
        elif len(sets) == 1:
            return [Driver(entity) for entity in sets[0]]
        else:
            return [Driver(entity) for entity in set.intersection(*sets)]

