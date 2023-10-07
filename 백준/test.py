dx = [1,-1,0,0,]
dy = [0,0,1,-1]

def bfs(x,y):
    global result
    q = set()
    q.add((x,y,array[x][y]))
    while q:
        a,b,c = q.pop()
        result = max(len(c),result)
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if 0<=nx<r and 0<=ny<c and array[nx][ny] not in c:
                

r,c = map(int,input().split())
array = []
for _ in range(r):
    array.append(input())

result = 0
bfs(0,0)
print(result)