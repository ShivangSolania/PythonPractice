def ad(a,b):
    l=[]
    for i in a:
        if i not in b:
            l.append(i)
    return l
x=list(map(int,input().split()))
y=list(map(int,input().split()))
print(ad(x,y))
