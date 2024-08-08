def narcissistic(val):
    b=sorted(val)
    t=0
    for e in b:
        t+=int(e)**len(b)
    if t==int(a):
        print("T")
        return True
    else:
        print("F")
        return False
a = input(": ")
narcissistic(a)