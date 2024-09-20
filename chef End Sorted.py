t=int(input())
for _ in range(t):
    #SHORT AND SIMPLE WAY
    n=int(input())
    l=list(map(int,input().split()))
    ct=0
    mind=l.index(min(l))
    maxd=l.index(max(l))
    if maxd>mind:
        ct+=n-maxd-1
    else:
        ct+=(n-maxd-1)-1
    print(ct)

    #LONG AND COMPLEX
    # if l[0]==min(l) and l[-1]==max(l):
    #     print(0)
    # else:
    #     for i in range(1,len(l)):
    #         while l[0]!=min(l):
    #             l[i],l[i-1]=l[i-1],l[i]
    #             ct+=1
    #             break
    #     for j in range(1,len(l)-1):
    #         while l[-1]!=max(l):
    #             l[j],l[j+1]=l[j+1],l[j]
    #             ct+=1
    #             break
    #     print(ct)