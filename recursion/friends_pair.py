from functools import lru_cache

@lru_cache
def f(n,i):
    if i<=0:
        return 1
    return f(n,i-1)+(n-i)*f(n,i-2)

@lru_cache
def f1(n):
    if n==1 or n==2:
        return n
    return f1(n-1)+(n-1)*f1(n-2)

n=40
print(f(n,i=n))
print(f1(n))