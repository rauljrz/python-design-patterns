import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Default Strategy"
        
        #If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)
        
            
    def execute(self): #This gets replaced by another version if another strategy is provided.
        """The defaut method that prints the name of the strategy being used"""
        print("{} is used!".format(self.name))