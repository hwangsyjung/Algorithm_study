def solution(nums):
    select = len(nums)//2
    p = {}
    for i in nums:
        if i in p:
            p[i] +=1
        else:
            p[i] = 1
    if len(p.keys()) >= select:
        return select
    else:
        return len(p.keys())