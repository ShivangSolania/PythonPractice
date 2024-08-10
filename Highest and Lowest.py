def high_and_low(n):
    s=""
    if not n:
        print("list empty")
        return
    ma=max(n)
    mi=min(n)
    s=f"{str(ma)} {str(mi)}"
    return print(s)
l=list(map(int,input().split()))
high_and_low(l)