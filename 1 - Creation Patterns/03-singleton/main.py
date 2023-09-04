"""
Example of using sinngleton pattern in Python
"""
from singleton import Singleton


def main():
    """ principal function """
    # Let's create a singleton object and add our first acronym
    first = Singleton(HTTP="Hyper Text Transsfer Protocol")

    # Print the object
    print(first)

    # Let's create another singleton object and
    # if it refers to the same attribute dictionary
    # by adding another acronym
    second = Singleton(SNMP="Simple Network Management Protocol")

    # Print the object
    print(second)


if __name__ == "__main__":
    main()
