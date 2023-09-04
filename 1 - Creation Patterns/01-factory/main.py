"""
Example the pattern Factory
"""
from dog import Dog
from cat import Cat


def get_pet(pet="dog"):
    """ The Factory Method """

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


def main():
    """ Principal Function """
    my_dog = get_pet("dog")
    print(my_dog.speak())

    my_cat = get_pet("cat")
    print(my_cat.speak())


if __name__ == "__main__":
    main()
