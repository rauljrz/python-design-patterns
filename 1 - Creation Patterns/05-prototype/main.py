from car import Car
from prototype import Prototype

def main():
    c = Car()
    proto= Prototype()
    proto.register_object('skylar', c)

    c2 = proto.clone('skylark')
    print(c2)

if __name__ == "__main__":
    main()