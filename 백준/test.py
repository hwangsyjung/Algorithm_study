from collections import deque
import heapq
import sys
input = sys.stdin.readline
def dijkstra():
    heap_data = []
    distance[s] = 0
    heapq.heapush(heap_data,(0,s))
    while heap_data:
        w,x = heapq.heappop(heap_data)
        if w > distance[x]:
            continue
        for i in adj[x]:
            cost = i[1]+distance[w]
            if distance[]
def bfs():

while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    start, end = map(int,input().split())
    adj = [[] for _ in range(n+1)]
    reverse_adj = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y,cost = map(int,input().split())
        adj[x].append((y,cost))
        reverse_adj[y].append((x,cost))
    dropped = [[False] * (n+1) for _ in range(n+1)]
    distance = [1e9]*(n+1)
    dijkstra()
    bfs()
    distance = [1e9]*(n+1)
    dijkstra()