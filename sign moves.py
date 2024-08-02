#Basic type :)
d = 0
for __ in range(int(input("Enter runs: "))):
    x = int(input("Enter coor: "))
    if d<0:
        d+=x
        print(d)
    elif d>0:
        d-=x
        print(d)
    elif d==0:
        if x<0:
            d+=x
            print(d)
        elif x>0:
            d-=x
            print(d)
        else:
            print(d)
    else:
        print(d)
#little more smart:)
for i in range(int(input("Enter runs: "))):
    x2 = int(input("Enter coor: "))
    if x%2==0:
        print(x//2)
    else:
        print(-(x//2+1))