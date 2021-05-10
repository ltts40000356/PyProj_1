# Finding the minimum and maximum values in a set
set1 = set()
print(type(set1))
try:
    set1.update(map(int, input().split()))
except:
    print("WARNING: Multiple Types Specified. Ignoring all values except Integers")
print(set1)
print("Maximum: ",max(set1))
print("Minimum: ",min(set1))