t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k!=0:
        print(n%k)
    else:
        print(n)
    # n1,n2=n-k,0
    # while n1>=0 and k!=0 and n1-k>=0:
    #     if k==1:
    #         print(0)
    #     else:
    #         n1=n1-k
    #         n2=n1
    # else:
    #     if k!=0 and n-k==0:
    #         print(0)
    #     elif k==0:
    #         print(n)
    #     elif n2!=0:
    #         print(n2)
    #     else:
    #         print(n)