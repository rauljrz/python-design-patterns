"""
Concrete Factory Dog
"""
from dog import Dog


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """ Returns a Dog object """
        return Dog()

    def get_food(self):
        """ Returns a Dog Food object """
        return "Dog Food!"
