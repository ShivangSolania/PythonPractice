def is_prime(n):
    if n<=1:
        return print(False)
    if n<=3:
        return print(True)
    if n%2!=0 and n%3!=0:
        return print(True)
    else:
        return print(False)
u=int(input())
is_prime(u)