n = int(input())
k=1
cnt = 0
while n:
    if n<k:
        k=1
    else:
        n-=k
        k+=1
        cnt+=1
print(cnt)