from handler import Handler

class DefaultHandler(Handler): # Inherits from the abstract handler
	"""Default handler"""

	def _handle(self, request):
		"""If there is no handler available"""
		#No condition checking since this is a default handler
		print("End of chain, no handler for {} (in DefaultHandler)".format(request))
		return True # Indicates that the request has been handled