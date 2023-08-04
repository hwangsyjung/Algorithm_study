dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    global result
    q = set()
    q.add(x,y,array[x][y])
    while q:
        x,y,step = q.pop()
        result = max(result, len(step))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 nx < r and ny < c and array[dx][dy] not in step:
                q.add(nx,ny,array[nx][ny])
r, c = map(int,input().split())
array = []
for _ in range(r):
    array.append(input())

result = 0
bfs(0,0)
print(result)