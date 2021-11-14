def is_prime(n):
    if n==1: return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def count_primes(a,b):
    count = 0
    for i in range(a,b+1):
        if is_prime(i):
            count+=1
    return count   


N=int(input())
M=int(input())

K=N//M
for k in range(1,K+1):
    w=count_primes((k-1)*M+1,k*M)/M
    print("%.4f"%w)
