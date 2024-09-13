def last_digit(n1, n2):
    l1 = []
    for i in range(1,5):
        l = (n1**i)%10
        l1.append(l)
    f1 = n2%4
    if n2 == 0:
        return 1
    if f1 == 0:
        return (l1[-1])
    else:   
        return (l1[f1-1])
##OR EZ WAY
def last_digit(n1, n2):
    return pow(n1,n2,10)