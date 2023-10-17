# 개수는 천만이 넘는데 수자체의 범위가 작을때(1~10000) 계수정렬 이용.
import sys
input = int(sys.stdin.readline())
array = [0]*10001
for i in range(input):
    data = int(sys.stdin.readline())
    array[data]+=1
for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
