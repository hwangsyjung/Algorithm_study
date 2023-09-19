n,l,k = map(int(input().split()))
hard, easy = 0, 0
for _ in range(n):
    a,b = map(int,input().split())
    if b<=l:
        hard +=1
    elif a <=l:
        easy +=1
score = 0
ans = min(hard, k)*140
if hard < k:
    ans+=min(easy, k-hard) * 100
print(ans)