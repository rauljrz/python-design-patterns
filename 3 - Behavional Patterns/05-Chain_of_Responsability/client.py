from defaulthandler import DefaultHandler
from concretehandler1 import ConcreteHandler1

class Client: # Using handlers
    def __init__(self):
        # Create handlers and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))
        
        # Note that the default handler has no successor

    def delegate(self, requests): # Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)