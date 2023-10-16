import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    q = sys.stdin.readline().split()
    if q[0]=='1':
        lst.append(q[1])
    elif q[0]=='2':
        if len(lst)==0:
            print(1)
        else:
            print(lst.pop())
    elif q[0]=='3':
        print(len(lst))
    elif q[0]=='4':
        print(1 if len(lst)==0 else 0)
    elif q[0]=='5':   
        if len(lst)==0:
            print(-1)
        else:
            print(lst[-1])