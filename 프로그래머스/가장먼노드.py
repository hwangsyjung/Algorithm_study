from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    q = deque([(1)])
    dist = [-1]*(n+1) # 1에서 그 노드까지의 거리
    dist[1] = 0
    while q:
        a = q.popleft()
        for i in graph[a]:
            if dist[i]==-1:
                dist[i] = dist[a]+1
                q.append(i)
    max_d = max(dist)
    for idx,i in enumerate(dist):
        if i == max_d:
            answer+=1
    return answer