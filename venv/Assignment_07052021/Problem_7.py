# Converting a Tuple to Dictionary
tuple = ("Apple", "Banana", "Guava", "Onion", "Jalepino")
print("Tuple is: "+str(tuple))
dict = {}
for i in range(0, len(tuple)):
    dict[i] = tuple[i]
print("After converting Tuple to Dictionary: "+str(dict))