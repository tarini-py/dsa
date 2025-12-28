import math

def f(amount, dp={}):
    
    if amount < 0:
        return math.inf
    if amount==0:
        return 0
    if amount in dp:
        return dp[amount]
    min_count = math.inf
    for k in range(len(coins)):
        if amount >= coins[k]:
            min_count = min(min_count, f(amount-coins[k]))
    
    dp[amount] = min_count+1
    return dp[amount]

coins = [3,7,405,436]
amount = 8839
ans = f(amount)
if ans == math.inf:
    print(-1)
print(ans)






            
        