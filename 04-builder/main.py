from skylarkbuilder import SkyLarkBuilder
from director import Director

def main():
    # El patrón de diseño Builder se utiliza para construir objetos complejos paso a paso.
    # Permite la creación de diferentes representaciones de un objeto utilizando el mismo proceso de construcción.
    
    builder = SkyLarkBuilder()
    director = Director(builder) 
    director.construct_car()

    car = director.get_car()
    print(car)

if __name__ == "__main__":
    main()
