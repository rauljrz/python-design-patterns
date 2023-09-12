from visitor import Visitor

class Electrician(Visitor): #Inherits from the parent class, Visitor
	"""Concrete visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self) #Note that the visitor now has a reference to the house object