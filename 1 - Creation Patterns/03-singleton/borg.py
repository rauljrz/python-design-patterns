"""
Example the concrete class singleton
"""


class Borg:
    """ The Borg design pattern """
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dictionary
