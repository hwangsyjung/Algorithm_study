def solution(dots):
    answer = 0
    def slope(i,j):
        return ((i[1]-j[1])/(i[0]-j[0]))
    if slope(dots[0], dots[1]) == slope(dots[2],dots[3]):
        answer+=1
    elif slope(dots[1], dots[2]) == slope(dots[3],dots[0]):
        answer+=1
    elif slope(dots[0], dots[2]) == slope(dots[1],dots[3]):
        answer+=1
    else:
        pass
    return answer