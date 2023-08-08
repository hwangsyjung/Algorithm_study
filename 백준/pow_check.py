# 빠른 거듭제곱과 모듈러
def pow_advanced(a,b,mod):
    ret = 1
    while b>0:
        if b%2: ret = ret*a%mod
        a,b = a*a%mod, b//2
    return ret

