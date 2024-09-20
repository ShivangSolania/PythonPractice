import sys
#WITHOUT GENERATOR
n=1000000
nums=[i for i in range(n)]

#WITH GENERATOR
#1
def gen(n):
    num=0
    while num<n:
        yield num
        num+=1
print(sys.getsizeof(sum(nums)))
print(sys.getsizeof(sum(gen(1000000))))
#2
def fib(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
a=fib(10)
print(list(a))
#3
#This is why we use generator as it uses way less memory than normal things and is faster
mygen=(i for i in range(100000) if i%2==0)
print(sys.getsizeof(mygen))
myl=[i for i in range(100000) if i%2==0]
print(sys.getsizeof(myl))