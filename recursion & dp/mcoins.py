import sys

sys.setrecursionlimit(1_000_000)

k, l, m = [int(i) for i in input().split()]
n = [int(i) for i in input().split()]

dp = [-1] * 1_000_000
#print(n)

def f(x):
    if x == 0:
        return False
    if x < 0:
        return True
    
    elif x == 1 or x == k or x == l:
        return True
    
    if dp[x] != -1:
        return dp[x]
    
    dp[x] = not ( f(x-1) and f(x-k) and f(x-l) )
    
    return dp[x]


for i in range(len(n)):
    if f(n[i]):
        print('A',end='')
    else:
        print('B',end='')
            
