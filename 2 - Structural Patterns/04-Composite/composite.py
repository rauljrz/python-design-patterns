from component import Component

class Composite(Component): #Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of the composite object
        self.name = args[0]
        

        #This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):

        #Print the name of the composite object
        print("{}".format(self.name))

        #Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()