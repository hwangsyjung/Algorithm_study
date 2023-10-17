# https://www.acmicpc.net/problem/2751
# 1. 병합정렬
def merge_sort(array):
    if len(array) <=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1 
    elif j==len(right):
        while i < len(left):
            array[k] = right[i]
            i+=1
            k+=1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
array = merge_sort(array)
for data in array:
    print(data)

# 파이썬 기본 정렬 라이브러리
n=int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)

for data in array:
    print(data)