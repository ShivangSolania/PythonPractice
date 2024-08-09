def find_outlier(inte):
    c=0
    for l in inte:
        a,b=inte[c],inte[c+1]
        c+=1
        if (a%2)==0:
            if (b%2)==0:
                continue
            else:
                print(b)
                break
        else:
            if a%2==1:
                if b%2==1:
                    continue
                else:
                    print(b)
                    break
d=list(map(int,input().split()))
find_outlier(d)