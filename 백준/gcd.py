# 최대공약수
# 방법 1. 단순하게 반복문 사용
def gcd_naive(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0: return i

# 방법 2. 유클리드 호제법 이용
def gcd(a,b):
    if a%b==0: return b
    return gcd(b,a%b)

# 방법 3. 반복문으로 변경
def gcd2(a,b):
    while a%b != 0: a, b = b, a%b
    return b

# 방법 4. math의 GCD 사용
import math
math.gcd(1,2)

# 최소공약수
def LCM(a,b):
    return a*b/gcd(a,b)