from composite import Composite
from child import Child

def main():
    #Build a composite submenu 1
    sub1 = Composite("submenu1")

    #Create a new child sub_submenu 11
    sub11 = Child("sub_submenu 11")
    #Create a new Child sub_submenu 12
    sub12 = Child("sub_submenu 12")

    #Add the sub_submenu 11 to submenu 1
    sub1.append_child(sub11)
    #Add the sub_submenu 12 to submenu 1
    sub1.append_child(sub12)

    #Build a top-level composite menu
    top = Composite("top_menu")

    #Build a submenu 2 that is not a composite
    sub2 = Child("submenu2")

    #Add the composite submenu 1 to the top-level composite menu
    top.append_child(sub1)

    #Add the plain submenu 2 to the top-level composite menu
    top.append_child(sub2)

    #Let's test if our Composite pattern works!
    top.component_function()

if __name__=="__main__":
    main()