def is_pangram(st):
    d={}
    alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    c=0
    for e in st.lower():
        if e!=' ':
            if e not in d:
                d[e]=1
            else:
                d[e]+=1
    for v in d.values():
        c+=v
    ch=True
    for x in alp:
        if c>=26 and d.get(x) is not None:
            ch=True
        else:
            ch=False
            return False
    return True
print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))