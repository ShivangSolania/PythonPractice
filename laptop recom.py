from collections import Counter
f = []
for __ in range(int(input("Enter no.: "))):
    n = int(input("Enter recomm: "))
    f.append(n)
print(Counter(f))

if Counter(f).most_common(1)[0][1] != Counter(f).most_common(2)[1][1]:
    print(Counter(f).most_common(1)[0][1])
else:
    print("Confused")