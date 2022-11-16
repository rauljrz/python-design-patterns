"""
Example the concrete class singleton
"""
from borg import Borg


class Singleton(Borg):
    """ The singleton class """

    def __init__(self, **Kwargs):
        Borg.__init__(self)

        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_data.update(Kwargs)

    def __str__(self):
        # Return the attribute dictionary for printing
        return str(self._shared_data)
