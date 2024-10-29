t=int(input())
for _ in range(t):
    l=int(input())
    u=input()
    ct=0
    for c in u:
        if c not in ['a','e','i','o','u']:
            ct+=1
            if ct>=4:
                break
        else:
            ct=0
    if ct>=4:
        print('NO')
    else:
        print('YES')