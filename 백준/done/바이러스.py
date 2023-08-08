n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0 

for _ in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
def dfs(now_pos):
    global count
    count += 1
    visited[now_pos]=True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)
            
dfs(1)
print(count-1)