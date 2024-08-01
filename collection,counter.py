from collections import Counter
a = "gigiqoqqgqigiqu"
print(Counter(a))
# and can access dict keys and values by .keys and .values, [0] phela tupple kholega, [1] uski 2nd index
print(Counter(a).most_common(2)[1][1])
# print(Counter(a).keys)