import clusto
from datetime import datetime

def get_by_hostname(hostname):
    """
    Lookup an entity by its hostname. Returns a list of all entities that have the hostname.
    """

    primary_hostname = clusto.get_entities(attrs=[{
                'subkey': 'hostname',
                'value' : hostname,
                }])

    hostname_alias = clusto.get_entities(attrs=[{
                'subkey': 'hostname-alias',
                'value' : hostname,
                }])

    return primary_hostname + hostname_alias
