n,m = list(map(int,input().split(' ')))
lst = list(map(int,input().split(' ')))
lst.sort(reverse = True)
max_value = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1, len(lst)):
            sum_value = lst[i]+lst[j]+lst[k]
            if m >= sum_value:
                max_value = max(max_value, sum_value)

print(max_value)