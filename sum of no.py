#sum of no.s between 2 integers
x = int(input("enter no.1: "))
y = int(input("enter no.2: "))
s = 0

for i in range(x,y+1):
    s+=i
print(s)