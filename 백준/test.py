import heapq
heap = []
result = []
n,m = map(int,input().split())
lst = [[] for _ in range(n+1)]
degree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    degree[b]+=1

for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(heap,i)

while heap:
    a = heapq.heappop(heap)
    result.append(a)
    for i in lst[a]:
        degree[i]-=1
        if degree[i]==0:
            heapq.heappush(heap,i)
for i in result:
    print(i,sep=' ')