# def maskify(cc):
#     t=len(cc)
#     ns=""
#     c=0
#     for i in cc:
#         if c<(t-4):
#             ns+="#"
#         else:
#             ns+=i
#         c+=1
#     print(ns)
# cn=input(": ")
# maskify(cn)
###########better###########
def m2(c1):
    t=len(c1)
    if t<=4:
        return c1
    else:
        m="#"*(t-4)+c1[-4:]
        return m
i=input(": ")
print(m2(i))