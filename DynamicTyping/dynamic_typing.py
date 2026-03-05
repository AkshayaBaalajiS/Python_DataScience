iVar = 12
string = "Akshaya Baalaji S"
fvar= 12.212121
print(iVar)
print(string)
print(fvar)


print("-------")
c =10
d =10
print(id(c))
print(id(d))
# both are holding same address cause the object of type integer created in memory and the name c is bind to it 
print("-------")


print("===========")
a = 23
b= a
a= 24
print(id(a))
print(id(b))
print("===========")


print("***********")
a = 23
b= 23
print(id(a))
print(id(b))

"""
Python does NOT create two integer objects.
Name c  ─┐
         ├──>  integer object 10  (already existing)
Name d  ─┘
This is an optimization:
	Integers are immutable
	Reusing them is safe
	Saves memory
	Faster comparison

Why is this safe?
Because integers are immutable.
You cannot modify the object 10.
If you do:
	c = 10
	c = 20
	You are not modifying 10.
	You are rebinding c.
"""
print("***********")
