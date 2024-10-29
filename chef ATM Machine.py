t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=''
    t=0
    for i in range(n): 
        if t+l[i]<=k:
            s+='1'
            t+=l[i]
        else:
            s+='0'
    print(s)