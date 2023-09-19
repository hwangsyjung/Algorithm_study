a = sorted(list(map(int,input().split())))
if len(set(a))==1:
    print(10000+a[0]*1000)
elif len(set(a))==2:
    print(1000+(a[1])*100)
else:
    print(a[2]*100)