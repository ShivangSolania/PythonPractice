t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    ch=True
    for i in range(n):
        s+=l[i]
        if s<k:
            ch=False
            print(f'NO {i+1}')
            break
        s-=k
    if ch:
        print('YES')