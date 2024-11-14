t=int(input())
for _ in range(t):
    f=[]
    c=int(input())
    l=list(map(int,input().split()))
    ch=True
    for c in l:
        if l.count(c)>2:
            ch=False
            break
    print('Yes' if ch else 'No')