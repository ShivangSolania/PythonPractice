for __ in range(int(input("Enter runs: "))):
    l = int(input("Enter len: "))
    bs = input("Enter binary str: ")
    z = bs.count("0")
    o = bs.count("1")
    if z==o:
        print(l)
    elif z<o:
        print((z*2)+1)
    else:
        print((o*2)+1)