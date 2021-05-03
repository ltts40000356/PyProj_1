# Removing a character by index in  a String
strObj = input("Please enter a string:")
strIndex = int(input("Please input the index where chractecter should be replaced:"))
strObj = strObj[ 0 : strIndex : ]+strObj[ strIndex+1 : : ]
print(strObj)