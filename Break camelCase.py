def soln(s):
    l2=""
    for a in s:
        if a.isupper():
            l2+=" "+str(a)
        else:
            l2+=str(a)
    return l2
u=input()
print(soln(u))