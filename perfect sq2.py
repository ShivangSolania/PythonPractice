import math
n = int(input("enter no: "))
s1 = math.sqrt(n)
s2 = s1 + 1
if isinstance(s2, int) is True:
    print(s2**2)
else:
    print("Null")