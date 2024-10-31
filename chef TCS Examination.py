t=int(input())
for _ in range(t):
    dl=list(map(int,input().split()))
    sl=list(map(int,input().split()))
    if sum(dl)>sum(sl):
        print('DRAGON')
    elif sum(dl)<sum(sl):
        print('SLOTH')
    else:
        if dl[0]>sl[0]:
            print('DRAGON')
        elif dl[0]<sl[0]:
            print('SLOTH')
        else:
            if dl[1]>sl[1]:
                print('DRAGON')
            elif dl[1]<sl[1]:
                print('SLOTH')
            else:
                print('TIE')