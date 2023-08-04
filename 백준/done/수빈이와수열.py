n = int(input())
lst = list(map(int,input().split(' ')))
result = []
for idx, x in enumerate(lst):
    if idx >=1 :
        result[idx] = lst[idx] * (idx+1) - sum(lst[:idx])
    else:
        result[idx] = (lst[idx]) * (idx+1)