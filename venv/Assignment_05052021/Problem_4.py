# Finding the Second Smallest Element of the List
n = int(input("Please enter the number of elements you want to enter:"))
for i in range(0, n):
    num = int(input("Enter Elemement:"))
    list.append(num)
print(list)
# Sorting the List in Ascending Order
list.sort()
# Printing the Sorted List
print(list)
# Printing the Second Element of the Sorted List
print(list[1])