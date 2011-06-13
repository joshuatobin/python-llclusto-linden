import clusto
from clusto.drivers import *
from llclusto.drivers.logging import LogEvent
from datetime import datetime

class LogMixin(object):
    """Provides a simple wrapper around LogEvent.
    """

    def add_log_event(self, **kwargs):
        """Provides a wrapper to instantiate a new LogEvent. Sets 
        the source_entity to the driver creating the LogEvent.
        
        Keyword arguments:
        **kwargs -- a list of keyword arguments needed to instantiate a LogEvent
        """
        return LogEvent(source_entity=self, **kwargs)


    def get_log_events(self, **kwargs):
        """Provices a wrapper around the get_log_events classmethod in LogEvent

        Keyword arguments:
        **kwargs -- a list of keyword arguments to look up LogEvents
        """
        return LogEvent.get_log_events(source_entity=self, **kwargs)
