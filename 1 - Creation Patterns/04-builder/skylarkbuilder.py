from builder import Builder

class SkyLarkBuilder(Builder):
    """ Concrete Builder --> provides parts and tools to work on the parts """

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo Engine"