def solution(s):
    p = []
    if s[0]==')' or s[-1]=='(':
        return False
    for i in s:
        if i == '(':
            p.append(i)
        else:
            if len(p)==0:
                return False
            else:
                p.pop()
    if len(p)==0:
        return True
    else:
        return False