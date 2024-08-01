from collections import namedtuple, defaultdict
p = namedtuple("Pt", "x,y")
pt = p(1, -4)
print(pt)
print(pt.x, pt.y)
#############
#default sets dict type like int str list etc
d = defaultdict(list)
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)
#deque kud deklo