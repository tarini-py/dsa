# https://atcoder.jp/contests/dp/tasks/dp_c

def max_happiness():
    global arr
    n=len(arr)
    dp= [[0, 0, 0] for _ in range(n)]
    
    #base case
    dp[-1][0] = arr[-1][0]
    dp[-1][1] = arr[-1][1]
    dp[-1][2] = arr[-1][2]
    
    for i in range(n-2,-1,-1):
        dp[i][0] = arr[i][0] + max( dp[i+1][1], dp[i+1][2] )
        dp[i][1] = arr[i][1] + max( dp[i+1][0], dp[i+1][2] )
        dp[i][2] = arr[i][2] + max( dp[i+1][0], dp[i+1][1] )

    return max( dp[0][0], dp[0][1], dp[0][2])
    
    
n = int(input())
arr = []

for i in range(n):
    arr.append([int(j) for j in input().strip().split(' ')])

print(max_happiness())