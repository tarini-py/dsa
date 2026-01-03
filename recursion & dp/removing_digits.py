import math,sys
sys.setrecursionlimit(10**7)

#x = int(input())

def f(n, dp={}):
    if n==0:
        return 0
    
    if n < 0:
        return math.inf
    
    if n in dp:
        return dp[n]
    count_min = math.inf
    for i in str(n):
        if i!='0':
            count_min = min(count_min, 1+f(n-int(i)))
    
    dp[n] = count_min
       
    return dp[n]

for i in range(0,101):
    print(i,' - ',f(i))