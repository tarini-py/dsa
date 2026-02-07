#https://www.spoj.com/problems/BVAAN
def f(s1, s2, i, j, k, dp):
    
    if k == 0:
        return 0
    
    if i < 0 or j < 0:
        return -float('inf')
    
    if (i,j,k) in dp:
        return dp[(i,j,k)]
    
    if s1[i] == s2[j]:
        dp[(i,j,k)] = ord(s1[i]) + f(s1, s2, i-1, j-1, k-1, dp)
    else:
        dp[(i,j,k)] = max(f(s1, s2, i-1, j, k, dp), f(s1, s2, i, j-1, k, dp))

    return dp[(i,j,k)]

def f_bu(s1, s2, i, j, k):
    dp = [[[-float('inf') for _ in range(k+1)] for _ in range(j+1)] for _ in range(i+1)]
    
    for ix in range(i+1):
        for jx in range(j+1):
            dp[ix][jx][0] = 0
                
    for ix in range(1, i+1):
        for jx in range(1, j+1):
            for kx in range(1, k+1):
                if s1[ix-1] == s2[jx-1]:
                    dp[ix][jx][kx] = ord(s1[ix-1]) + dp[ix-1][jx-1][kx-1]
                else:
                    dp[ix][jx][kx] = max(
                        dp[ix][jx-1][kx],
                        dp[ix-1][jx][kx]
                    )
    return dp[-1][-1][-1]

t = int(input())
s1 = [0]*t
s2 = [0]*t
k=[0]*t
for i in range(t):
    s1[i] = input()
    s2[i] = input()
    k[i] = int(input())

for i in range(len(k)):
    dp = {}
    temp = f(s1[i], s2[i], len(s1[i])-1, len(s2[i])-1, k[i], dp)
    if temp == -float('inf'):
        print(0)
    else:
        print(temp)

for i in range(len(k)):
    temp2 = f_bu(s1[i], s2[i],  len(s1[i]), len(s2[i]), k[i])
    if temp2 == -float('inf'):
        print(0)
    else:
        print(temp2)