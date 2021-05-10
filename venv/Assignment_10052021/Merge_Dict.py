# Merging two dictionaries
dict1 = {1:"Apple", 2:"Pinapple", 3:"Guava", 4: "Pears", 5:"Orange"}
dict2 = {6:"Ironman", 7:"Spiderman", 8:"Thor"}
print("Dictionary 1: ",str(dict1))
print("Dictionary 2: ",str(dict2))
dict2.update(dict1)
print(dict2)