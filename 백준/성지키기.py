# https://www.acmicpc.net/problem/1236
N,M = list(map(int, input().split()))
castle = []
for _ in range(N):
    castle.append(input())
row = [0] * N
column = [0] * M
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i]=1
            column[j]=1
row_count = 0
for i in range(N):
    if row[i] == 0 :
        row_count +=1 

column_count = 0
for j in range(M):
    if column[j] == 0 :
        column_count +=1 

print(max(row_count, column_count))