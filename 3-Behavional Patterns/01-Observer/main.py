from core import Core
from tempviewer import TempViewer

def main():
    #Let's create our subjects
    c1 = Core("Core 1") 
    c2 = Core("Core 2") 

    #Let's create our observers
    v1 = TempViewer() 
    v2 = TempViewer() 

    #Let's attach our observers to the first core
    c1.attach(v1)
    c1.attach(v2)

    #Let's change the temperature of our first core
    c1.temp = 80
    c1.temp = 90


if __name__=="__main__":
    main()