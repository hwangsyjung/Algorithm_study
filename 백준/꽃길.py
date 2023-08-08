N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int,input().split(' '))))

dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret

ans = 10000
for i in range(N*N):
    for j in range(N*N):
        for k in range(N*N):
            ans = min(ans, ck(i,j,k))
print(ans)