t=int(input())
for _ in range(t):
    d,l,r=map(int,input().split())
    if l<=d<=r:
        print('Take second dose now')
    elif d>r:
        print('Too Late')
    else:
        print('Too Early')
