import sys

sys.setrecursionlimit(10**7)
x = int(input())
dp=[-1]*(x+1)

def f(n):

    if n==0:
        return 1
    if dp[n] != -1:
        return dp[n]
    count= 0
    for i in range(1,7):
        if i <= n:
            count += f(n-i)
    dp[n] = count
    return dp[n]
            


ans = f(x) % (10**9 +7)
print(ans)