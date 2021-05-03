# Find the first repeated character in a String
sampleStr = "aeioissuebdfhkssd"
duplicates = []
for char in sampleStr:
   if sampleStr.count(char) > 1:
      if char not in duplicates:
         duplicates.append(char)
print("First Character that was duplicated: " + duplicates[0])