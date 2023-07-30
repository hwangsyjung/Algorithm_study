# https://www.acmicpc.net/problem/2747

n = int(input())
def fibo(x):
    if x<=1:
        return x
    return fibo(x-1) + fibo(x-2)
print(fibo(n))

n = int(input())
a,b = 0,1
while n > 0:
    a, b = b, a+b
    n -= 1
print(a)