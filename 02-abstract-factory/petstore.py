"""
Concrete class of Pet Store
"""


class PetStore:
    """PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abastract Factory """
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the object
            retured by the Dog Factory.
        """
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is '{pet}!")
        print(f"Our pet say hello by '{pet.speak()}'")
        print(f"Its food is '{pet_food}'!")

    def show_name(self):
        """ Show name the pet store """
