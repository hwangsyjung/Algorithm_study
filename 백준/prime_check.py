# 소수 체크
def prime_check(N):
    for i in range(2,N):
        if N%i == 0: return False
        if i*i > N : break
    return True
#소인수 분해
def prime_factorization(N):
    p, fac = 2, []
    while p ** 2 <= N:
        if N%p==0:
            N//=p
            fac.append(p)
        else:
            p +=1
    if N > 1 : fac.append(N)
    return fac
# 에라토스테네스의 체를 활용한 소수 리스트 구하기
def era_prime(N):
    A, p = [0 for _ in range(N+1)], []
    for i in range(2,N):
        if A[i] == 0 : p.append(i)
        else: continue
        for j in range(i**2, N, i):
            A[j] = 1
    return p
# 에라토스테네스의 체를 활용한 소인수의 개수
def era_factor_count(N):
    A = [0 for _ in range(N+1)]
    for i in range(2,N):
        for j in range(i,N,i):
            A[j] += 1
    return A 
# 에라토스테네스의 체를 활용한 소인수의 합
def era_factor_sum(N):
    A = [0 for _ in range(N+1)]
    for i in range(2,N):
        for j in range(i, N, i):
            A[j] += i
    return A
# 에라토스테네스의 체를 활용한 소인수분해
def era_factorization(N):
    A = [0 for _ in range(N+1)]
    for i in range(2,N):
        for j in range(i, N, i):
            A[j] = i
    return A