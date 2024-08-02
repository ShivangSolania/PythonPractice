#Normal way
# for __ in range(int(input("Enter runs: "))):
#     a,b,c=map(int,input().split())
#     x=min(a,b)
#     y=min(b,c)
#     z=min(c,a)
#     if(x==y and y==z and z==x):
#         print("Yes")
#     else:
#         print("NO")
# diffenent approach
for __ in range(int(input("Enter runs: "))):
    l=list(map(int,input().split()))
    print(l)
    l.sort()
    if l[0]==l[1]:
        print("Yes")
    else:
        print("NO")