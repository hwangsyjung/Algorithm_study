from itertools import permutations
def solution(babbling):
    answer = 0
    # 이어붙인 것 혹은 하나씩 쓴것
    for i in babbling:
        cnt = 0
        word = ''
        for j in i:
            word+=j
            if word in ["aya", "ye", "woo", "ma"]:
                cnt+=1
                word = ''
        if len(word)==0 and cnt>=1:
            answer+=1
    return answer