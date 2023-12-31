def solution(arr):
    answer = []
    for i in arr:
        if len(answer)>=1:
            if i == answer[-1]:
                continue
            else:
                answer.append(i)
        else:
            answer.append(i)
    return answer