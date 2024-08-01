#for str
var1 = "name"
ms1 = "the variable is %s" %var1
print(ms1)
#for integer
var2 = 3
ms2 = "the variable is %d" %var2
print(ms2)
#for float, dot 3 for to use 3 decimal places
var3 = 3.2454235
ms3 = "the variable is %.3f" %var3
print(ms3)
#different approach for input, :.3f to take 3 decimal places
var3 = 3.2454235
var4 = "lololol"
ms4 = "the variable is {:.3f}, {}".format(var3, var4)
print(ms4)
#best mixture with f string
var5 = 3.2454235
var6 = "lololol"
ms5 = f"the variable is {var5*2}, {var6}"
print(ms5)