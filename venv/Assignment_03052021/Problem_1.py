sampleStr = input("Enter a String:") #Input from the user
firstChar = sampleStr[0] #Extracting the first character
print("Your Input:" + sampleStr)
temp_list = list(sampleStr) # Coverting to List since String is immutable
for i in range(1, len(temp_list)):
    if(temp_list[i] == firstChar):
        temp_list[i] = "$"
print(temp_list) # Validating the List with replaced characters
sampleStr = "".join(temp_list) # Converting the list back to string
print(sampleStr)