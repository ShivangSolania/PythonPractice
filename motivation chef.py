t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    c=[]
    c1=[]
    for __ in range(n):
        si,ri=map(int,input().split())
        r=[si,ri]
        c.append(r)
    for i,j in c:
        if i<=x: 
            c1.append(j)
    print(max(c1))