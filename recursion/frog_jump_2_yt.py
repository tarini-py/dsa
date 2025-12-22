import math
def min_cost(height,k, i=0, dp = {}):
    if i==len(height)-2:
        return abs(height[i]-height[i+1])
    if i==len(height)-1:
        return 0
        
    if i in dp:
        return dp[i]
    
    min_path = math.inf
    for n in range(1,k+1):
        if n+i >= len(height):
            break
        min_path = min(min_path, abs(height[i]-height[i+n])+min_cost(height,k, i+n,dp) )
    
    dp[i] = min_path
    #dp[i] = min(abs(height[i]-height[i+1])+min_cost(height,i+1,dp),abs(height[i]-height[i+2])+min_cost(height,i+2,dp))
    
    return dp[i]


height=[10,20,40,50,30]
k=3
print(min_cost(tuple(height),k))