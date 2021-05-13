# Merging two dictionaries
dict1 = {1:"Apple", 8:"Pinapple", 3:"Guava", 4: "Pears", 5:"Orange"}
dict2 = {90:"Ironman", -3:"Spiderman", 6:"Thor"}
print("Dictionary 1: ",str(dict1))
print("Dictionary 2: ",str(dict2))

# Merge using Update
dict2.update(dict1)
print(sorted(dict2.items()))