def aa(a,b=2):
    if a==0:
        return 0
    aa(a-1)
    d=b*a 
    print(f"{b}*{a}={d}")
    return d
aa(10)