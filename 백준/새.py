N = int(input())
k = 1
time = 0
while N:
    if N<k:
        k=1 
    N-=k
    time+=1
    k+=1
print(result)
