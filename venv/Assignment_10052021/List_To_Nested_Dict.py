# Converting a list to Nested Dictionary
dict = {}
name_list = input("Enter 3 Names: ").split()
age_list = input("Enter Ages: ").split()
loc_list = input("Enter Locations: ").split()
for i in range(0,3):
    dict[(i+1)] = {'Name':name_list[i], 'Age':int(age_list[i]), 'Location:':loc_list[i]}
print(dict)