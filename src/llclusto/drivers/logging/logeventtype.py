import clusto
from clusto.drivers import Driver

class LogEventType(Driver):
    """A LogEventType entity stores a specific event type such as "power on".
    The LogEventType needs to be initialized before it can be used by LogMixin
    or LogEvent.
   
    """
    _driver_name="logeventtype"
    _clusto_type="logeventtype"

    _properties = {"description" : None}
