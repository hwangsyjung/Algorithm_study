import sys
sys.setrecursionlimit(10000)

dx, dy = [1,-1,0,0,],[0,0,-1,1]
def dfs(x,y):
    if visited[x][y]:
        return
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<m and ny>=0 and ny<n and not visited[nx][ny] and lst[nx][ny]:
            dfs(nx,ny)

for _ in range(int(input())):  
    m,n,k = map(int,input().split())
    lst = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x,y = map(int,input().split())
        lst[x][y] = 1
    visited = [[False for _ in range(n)] for _ in range(m)]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and lst[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt)    
