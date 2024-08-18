#ENUMERATE USAGE
def tsu(n,t):
    nti={}
    for i,nu in enumerate(n):
        co=t-nu
        if co in nti:
            return (nti[co],i)
        nti[nu]=i
    return None
o=list(map(int,input().split()))
t=int(input())
r=tsu(o,t)
print(r)