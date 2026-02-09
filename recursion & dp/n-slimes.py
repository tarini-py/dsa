def f(i, j, arr, dp):
    if i == j:
        return 0
    if (i,j) in dp:
        return dp[(i,j)]
    cost = float('inf')
    for k in range(i, j):
        cost = min(cost, f(i,k,arr,dp) + f(k+1,j,arr,dp) + sum(arr[i:j+1]))
    dp[(i,j)] = cost
    return cost
        
    
    
l = int(input())
arr = [int(i) for i in input().split()]
sum_arr = [[0] * l for _ in range(l)]
for i in range(l):
    for j in range(i,l):
        if i == j:
            sum_arr[i][j] = arr[j]
        else:
            sum_arr[i][j] = arr[j] + sum_arr[i][j-1]

dp = {}
print(f(0, l-1, arr, dp))