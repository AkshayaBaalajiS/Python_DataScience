
# { } is NOT a block delimiter.
# {
# mul values to mul var in one line 
a, b, c = "Akshaya Baalaji S", 23, 23.234
print(f"{a} , {b}, {c}")	
# }

# {		
# same value to mul variable 
a = b = c = "Akshaya Baalaji S"
print(f"{a} , {b}, {c}")

# a[0] = 'a' # this is not possible in python  # error : str' object does not support item assignment
print(a[0]) 

for i in a:
	print(i , end = " ")



# }		