from collections import defaultdict
def solution(clothes):
    answer = 1
    p = defaultdict(list)
    for i in clothes:
        p[i[1]].append(i[0])
    for k, v in p.items():
        answer*=(len(v)+1)
    return answer-1