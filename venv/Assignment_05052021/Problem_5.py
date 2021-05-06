list = []
n = int(input("Please enter the number of elements you want to enter:"))
for i in range(0, n):       # Taking list input from user
    num = int(input("Enter Elemement:"))
    list.append(num)
print(list)
temp_list = []              # To Hold the switched values
flag = False                # To handle odd numbered list
if len(list)%2 != 0:
    last_element = list[-1] # Extracting the Last Element
    list = list[:-1]        # Creating even numbered list
    flag = True
i=0
while i < len(list):        # Switching the i th position with (i+1) th position
    temp_list.extend([list[i+1], list[i]])
    i+= 2
if flag == True:            # In case of odd number sized list
    temp_list.append(last_element)
print(temp_list)