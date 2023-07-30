# https://www.acmicpc.net/problem/1966
case_num = int(input())
for i in range(case_num):
    N, location = list(map(int, input().split(' ')))
    important_lst = list(map(int, input().split(' ')))
    important_lst = [(i, idx) for idx, i in enumerate(important_lst)]
    count = 0
    while True:
        if important_lst[0][0] == max(important_lst, key = lambda x: x[0])[0]:
            count = 0
            if important_lst[0][1] == location:
                print(count)
                break
            else:
                important_lst.pop(0)
        else:
            important_lst.append(important_lst.pop(0))
            