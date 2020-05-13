
for i in range(345,10000):
    s=i**3
    a=[]
    i+=1

    while len(str(i**3))==len(str(s)):
        if sorted(list(str(s)))==sorted(list(str(i**3))):
            a.append(i**3)
        i+=1
        if len(a)==4:
            print(s,a)
            exit()
