def solution(n):
    a=0
    for i in range(1,n):
        if i%3==0:
            a+=i
        elif i%5==0:
            a+=i
    return a
u=int(input(": "))
print(solution(u))