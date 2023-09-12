class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = [] # This where references to all the observers are being kept
                                # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        #If the observer is not already in the observers list
        # append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:  # For all the observers in the list
            if modifier != observer:      # Don't notify the observer who is actually updating the temperature 
                observer.update(self)     # Alert the observers!