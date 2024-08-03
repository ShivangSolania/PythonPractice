for __ in range(int(input("Enter runs: "))):
    ns = int(input())
    n=list(map(int,input().split()))
    if 1 in n:
        print("CHEF")
    else:
        if sum(n)%2==0:
            print("CHEFINA")
        else:
            print("CHEF")