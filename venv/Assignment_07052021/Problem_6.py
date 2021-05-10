# Write a Python program to find the repeated items of a tuple
mytuple = (1, "ABC", "DA500", 700, ["ABC", "Augmentium"], 9.879, "DA500", 'ABC')
for i in range(0,len(mytuple)):
    print(mytuple[i])
    print(type(mytuple[i]))
seen = set()