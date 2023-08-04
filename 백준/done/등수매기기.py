rate = []
for _ in range(int(input())):
    rate.append(int(input()))
rate.sort()
unsatisfy = 0
for i in range(1, len(rate)+1):
    unsatisfy+=abs(rate[i-1]-i)
print(unsatisfy)