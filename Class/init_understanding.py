class ClassA :
	def __init__(self):	
		print("Class A init called")

cobj = ClassA()
print(cobj)
print("id of class obj = " , id(cobj))

"""
Why __init__
"""
class ClassB:
	pass

bobj = ClassB()
# Manual set 
bobj.name = "Akshaya Baalaji"
bobj.id = 12
print(bobj.name)

"""
With __init__
"""

class ClassC:
	def __init__(self, n, i):
		name = n 
		inte = i
		"""
		without self it state that no attribute 
		"""
		self.sname = n
		self.si = i

cobj = ClassC("Akshay S", 12)
"""
The below cant be done cause the self is not there so it will not be the class member
print("ClassC.Name = ", cobj.name)
print("ClassC.inte = ", cobj.inte)
"""
print("ClassC.Name = ", cobj.sname)
print("ClassC.inte = ", cobj.si)

