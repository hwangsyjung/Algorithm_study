N = int(input())
dp = [0] * 1000001
dp[1]=1
dp[2]=2

for i in range(2,n+1):
    dp[i] = (dp[i-1]+ df[i-2]) % 15746

print(dp[n])