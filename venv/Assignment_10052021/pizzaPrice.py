# Function for checking if the number of pieces are even or odd
def IsEven(n):
    if n%2 == 0:
        return True
    else:
        return False
# Determine Pizza Price based on the number of Slices
slices = int(input("Enter number of slices:"))
if IsEven(slices):
    print("Total Price for even slices is Rs."+str(slices*120))
else:
    print("Total Price for odd slices is Rs."+str(slices*123))
