from visitor import Visitor

class HvacSpecialist(Visitor): #Inherits from the parent class, Visitor
	"""Concrete visitor: HVAC specialist"""
	def visit(self, house):
		house.work_on_hvac(self) #Note that the visitor now has a reference to the house object