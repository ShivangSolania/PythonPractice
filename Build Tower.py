def tbuilt(nf):
    t=[]
    f=""
    for f in range(nf):
        st="*"*(f*2+1)
        sp=" "*(nf-f-1)
        fl=sp+st+sp
        t.append(fl)
    return t
def t2built(nf):
    f=1
    for i in range(nf):
        s="*"*f
        print(s.center(30," "))
        f+=2
a=int(input(": "))
print(tbuilt(a))
print(t2built(a))