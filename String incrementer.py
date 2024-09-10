def increment_string(strng):
    s,c='',''
    for i in strng:
        if i.isnumeric():
            c+=i
        else:
            s+=i
    if c=='':
        c+='1'
        return s+c
    else:
        l=len(c)-len(c.lstrip('0'))
        ns=int(c)+1
        return s+(str(ns).zfill(l))
u=input()
print(increment_string(u))