def ips_between(start,end):
    s1=start.split('.')
    s2=end.split('.')
    t1=0
    t2=0
    c1,c2=0,0
    for i in s1:
        t1+=int(i)*(256**(3-c1))
        c1+=1
    for e in s2:
        t2+=int(e)*(256**(3-c2))
        c2+=1
    f=t1-t2
    if f<0:
        return -f
    elif f>=0:
        return f
n1,n2=map(str,input().split())
print(ips_between(n1,n2))