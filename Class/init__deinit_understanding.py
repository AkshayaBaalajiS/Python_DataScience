
class ClassC:
	def __init__(self, n, i):
		name = n 
		inte = i
		"""
		without self it state that no attribute 
		"""
		self.sname = n
		self.si = i
		print("-- ClassC init called --")
	def __del__(self):
		print("Object destroyed ")

cobj = ClassC("Akshay S", 12)
"""
The below cant be done cause the self is not there so it will not be the class member
print("ClassC.Name = ", cobj.name)
print("ClassC.inte = ", cobj.inte)
"""
print("ClassC.Name = ", cobj.sname)
print("ClassC.inte = ", cobj.si)
