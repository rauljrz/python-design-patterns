from car import Car

class Builder():
    """ Abastract Builder """

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()
