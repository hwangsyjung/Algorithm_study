lst = list(map(int,input().split(' ')))
ascending = True
descending = True
for i in range(1,len(lst)):
    if lst[i] < lst[i-1]: 
        ascending=False
    else:
        descending=False
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
