from handler import Handler

class ConcreteHandler1(Handler): # Inherits from the abstract handler
	"""Concrete handler 1"""
	def _handle(self, request):
		if 0 < request <= 10: # Provide a condition for handling
			print("Request {} handled in ConcreteHandler 1".format(request))
			return True # Indicates that the request has been handled