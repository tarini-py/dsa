from functools import lru_cache

@lru_cache
def f(n):
    if n==1 or n==2:
        return n
    return f(n-1)+(n-1)*f(n-2)

def f_opt(n:int, dp:dict = {}):
    if n==1 or n==2:
        return n
    if n in dp:
        return dp[n]
    dp[n] = f_opt(n-1)+(n-1)*f_opt(n-2)
    return dp[n]

n=40
print(f(n))
print(f_opt(n))