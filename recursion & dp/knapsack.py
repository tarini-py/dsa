n, w_cap = [int(i) for i in input().split()]

weights = [0]*n
values = [0]*n

for i in range(n):
    w, v = [int(_) for _ in input().split()]
    weights[i] = w
    values[i] = v

# print(n,w_cap)
# print(weights, values)

def f(n, w_cap, i = 0, dp = {}):
    
    if w_cap == 0:
        return 0
    
    if w_cap < 0:
        return -values[i-1]
    
    if i >= n:
        return 0
    
    if (w_cap, i) in dp:
        return dp[(w_cap, i)]
    
    max_val = -float('inf')
    max_val = max(max_val, values[i] + f(n, w_cap-weights[i], i+1), f(n, w_cap, i+1))
    
    dp[(w_cap, i)] = max_val
    return max_val


def f_bu(n, w_cap):
    dp = [ [0] * (w_cap+1) for _ in range(n+1)]
            
    for i in range(n-1, -1, -1):
        for j in range(1, w_cap+1):
            
            max_val = dp[i+1][j]
            
            if weights[i] <= j:
                max_val = max(max_val, values[i] + dp[i+1][j - weights[i]])
            
            dp[i][j] = max_val
    
    return dp
    
            
dp = f_bu(n, w_cap)

# for i in dp:
#     print(i)
print(dp[0][w_cap])