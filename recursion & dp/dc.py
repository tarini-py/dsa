MOD = 10**9 + 7

x = int(input())

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    for j in range(1, 7):
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % MOD

print(dp[x])
print(dp)