# https://www.acmicpc.net/problem/2750

# 1. 선택정렬

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
for i in range(N):
    min_index=i
    for j in range(i+1,N):
        if lst[min_index]>lst[j]:
            min_index = j
    lst[min_index], lst[i] = lst[i], lst[min_index]

for i in lst:
    print(i)

# 2. 파이썬의 기본 정렬 라이브러리

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
for j in lst:
    print(j)