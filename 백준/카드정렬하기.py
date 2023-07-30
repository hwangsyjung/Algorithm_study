import heapq

n=int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
result = 0

while len(heap) != 1:
    one = heapq.heappop(heapq)
    two = heapq.heappop(heapq)
    sum_value = one+two
    heapq.heappush(sum_value)
    result += sum_value
print(result)