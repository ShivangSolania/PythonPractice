#Direct use of lamda func
f1=lambda x:x+10
print(f1(2))
f2=lambda x,y:x*y
print(f2(2,4))

#in def
def myfun(n):
    return lambda x:x*n
t=myfun(5)
print(t(4))

#using as key
points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorby=sorted(points2D,key=lambda x:x[1])#Sort by index 1 in list
print(sorby)
##########
mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key=lambda x:abs(x))#sort by mod of every no in list
print(sorted_by_abs)

#SEE LOGGING IN FREECODECAMP