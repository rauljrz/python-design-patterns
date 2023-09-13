class Handler: #Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor    # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request) #If handled, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')