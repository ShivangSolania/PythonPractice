def decode(n):
    l1=['_','-']
    l2=list(n)
    s=''
    for i in range(len(n)):
        e=n[i]
        if e not in l1:
            if i>0 and l2[i-1] in l1:
                s+=e.upper()
            else:
                s+=e
    return s
a=input('enter: ')
print(decode(a))