import math
import sys
input = sys.stdin.readline

def get_distance(p1,p2):
    a=p1[0]-p2[0]
    b=p1[1]-p2[1]
    return math.sqrt((a*a) + (b*b))

def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n]) # root 찾기

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

edges = [] # 모든 점사이의 edge 와 거리
parent = {}
locations = []
n,m = map(int, input().split())

for _ in range(n): # 4
    x, y = map(int, input().split())
    locations.append((x,y)) 

for i in range(n - 1): # 0,1,2
    for j in range(i + 1, n): #1,2,3
        edges.append((i+1, j+1, get_distance((locations[i], locations[j]))))

for i in range(1, n+1):
    parent[i] = i # 초기화

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges.sort(key = lambda data: data[2])
result = 0
for a, b, cost in edges:
    if not find_parent(parent,a,b):
        union_parent(parent,a,b)
        result +=cost
print("%0.2f"%result)