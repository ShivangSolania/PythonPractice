t=int(input())
for _ in range(t):
    u,v,a,s=map(int,input().split())
    if ((u**2)-2*a*s)<0:
        print('Yes')
    elif v==u:
        print('Yes')
    elif v>=(((u**2)-2*a*s))**0.5:
        print('Yes')
    else:
        print('No')