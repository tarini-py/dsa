from functools import lru_cache

@lru_cache
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)


def fib_dp(n:int, dp:dict = {}):
    if n==0 or n==1:
        return n
    if n in dp:
        return dp[n]
    dp[n] = fib_dp(n-1)+fib_dp(n-2)
    return dp[n]
        
n=900
print(fib(n))
print(fib_dp(n))