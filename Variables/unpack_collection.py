a = ["Akshaya Baalaji", 32, "Baalaji S"]
print(a)
b = a


# unpacking list 
Name, age, SurName = a
print(Name,"---", age, "---", SurName)

print(id(a))
print(id(b))