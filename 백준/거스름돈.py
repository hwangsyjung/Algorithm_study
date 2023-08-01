money = 1000-int(input())
cnt = 0
for i in [500, 100, 50, 10, 5, 1]:
    cnt += money // i
    money %= i
print(cnt)