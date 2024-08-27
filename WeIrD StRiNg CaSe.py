def to_weird_case(words):
    r=[]
    for w in words.split():
        ww=[]
        for i,c in enumerate(w):
            if i%2==0:
                ww.append(c.upper())
            else:
                ww.append(c.lower())
        r.append(''.join(ww))
    return ' '.join(r)
u=input(": ")
print(to_weird_case(u))