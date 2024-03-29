from korean import Korean
from british import British
from adapter import Adapter

def main():
    #List to store speaker objects
    objects = []

    #Create a Korean object
    korean = Korean()

    #Create a British object
    british = British()

    #Append the objects to the objects list
    objects.append(Adapter(korean, speak=korean.speak_korean))
    objects.append(Adapter(british, speak=british.speak_english))

    print("Result")
    for obj in objects:
        print("{} says '{}'\n".format(obj.name, obj.speak()))

if __name__=="__main__":
    main()