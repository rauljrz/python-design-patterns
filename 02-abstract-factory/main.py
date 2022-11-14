"""
Example main function of Abstract Factory.
"""
from petstore import PetStore
from dogfactory import DogFactory


def main():
    """ Principal Function """

    # Create a Concrete Factory
    factory = DogFactory()

    # Create a pet store housing our Abstract Factory
    shop = PetStore(factory)

    # Invoke the utility method to show the details of our pet.
    shop.show_pet()


if __name__ == "__main__":
    main()
