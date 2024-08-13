def tribonacci(sig, n):
    l=[sig[0]]
    if len(sig) in (0,1,2) or n<=0:
        return []
    else:
        a,b,c=sig[0],sig[1],sig[2]
        for n in range(n-1):
            a,b,c=b,c,a+b+c
            l.append(a)
    return l
s=list(map(int,input().split()))
r=int(input("Run: "))
print(tribonacci(s,r))