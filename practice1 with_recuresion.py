#basic for whole sequence
def fib1(n):
   a,b=0,1
   for i in range(n):
      a,b=b,a+b
      print(a)
print(fib1(5))
print("********************")    
#inter for specific no in sequence
def fib(n):
   if n<=1:
      return n
   else:
      return fib(n-1) + fib(n-2)
print(fib(5))
print("********************")
#tribo inter code
def trib(n):
    a,b,c=0,0,1
    for i in range(n):
        a,b,c=b,c,a+b+c
        print(a)
print(trib(5))
