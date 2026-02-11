#spoj - acode
# your code goes here
dp = {}
def f(s, i):
    global dp
    if i < 0:
        return 1

    if i in dp:
        return dp[i]

    ans = 0

    if int(s[i]) >= 1:
        ans += f(s, i-1)

    if i > 0 and int(s[i-1]) >= 1 and 10 <= int(s[i-1])*10 + int(s[i]) <= 26:
        ans += f(s, i-2)

    dp[i] = ans
    return ans

def f_bu(s):
    n = len(s)
    dp = [0] * (n+1)
    dp[-1] = 1
    
    for i in range(n):
        if int(s[i]) >= 1:
            dp[i] += dp[i-1]
        if i > 0 and int(s[i-1]) >= 1 and 10 <= int(s[i-1])*10 + int(s[i]) <= 26:
            dp[i] += dp[i-2]
    
    return dp[-2]
    
    
while True:
    s = input()
    if s == '0':
        break
    print(f_bu(s))
    print(f(s, len(s) - 1))
