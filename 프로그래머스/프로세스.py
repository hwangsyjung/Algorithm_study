def solution(priorities, location):
    answer = 0
    p = [(idx,x) for idx, x in enumerate(priorities)]
    loca = 1
    while True:
        if p[0][1]==max(priorities):
            if p[0][0]==location:
                break
            p.pop(0)
            priorities.pop(0)
            loca +=1
        else:
            p.append(p.pop(0))
            priorities.append(priorities.pop(0))
    return loca