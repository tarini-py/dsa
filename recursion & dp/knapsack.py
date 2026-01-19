n, w_cap = [int(i) for i in input().split()]
weights = [0]*n
values = [0]*n
for i in range(n):
    w, v = [int(_) for _ in input().split()]
    weights[i] = w
    values[i] = v

print(n,w_cap)
print(weights, values)

def f(n, w_cap, i = 0, dp = {}):
    
    if w_cap == 0:
        return 0

    if w_cap < 0:
        return -values[i-1]
    if (w_cap, i) in dp:
        return dp[(w_cap, i)]
    if i >= n:
        return 0
    
    max_val = -float('inf')
    
    for k in range(i,n):
        max_val = max(max_val, values[k] + f(n, w_cap-weights[k], k+1), f(n, w_cap, k+1))
    
    dp[(w_cap, i)] = max_val
    return max_val


dp = {}
print(f(n, w_cap, 0, dp = dp))


def f_2d_dp(n, w_cap, i, dp):
    
    if w_cap == 0:
        return 0

    if w_cap < 0:
        return -values[i-1]
    
    if i >= n:
        return 0
        
    if dp[w_cap][i] != -1:
        return dp[w_cap][i]
    
    max_val = -float('inf')
    
    for k in range(i,n):
        max_val = max(max_val, values[k] + f_2d_dp(n, w_cap-weights[k], k+1, dp), f_2d_dp(n, w_cap, k+1, dp))
    
    dp[w_cap][i] = max_val
    return max_val

dp = [[-1] * (n+1) for _ in range(w_cap+1)]
print(f_2d_dp(n, w_cap, 0, dp))