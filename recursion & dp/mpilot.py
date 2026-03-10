# your code goes here
'''
Docstring for recursion & dp.mpilot
4 
5000 3000
6000 2000
8000 1000
9000 6000

6
10000 7000
9000 3000
6000 4000
5000 1000
9000 3000
8000 6000


19000
32000
'''

n = int(input())

s_c = []
s_a = []

for _ in range(n):
	c, a = input().split()
	s_c.append(int(c))
	s_a.append(int(a))


def f(i, cc, ca, dp = {}):
	if i >= n:
		return 0
	if (i, cc, ca) in dp:
		return dp[(i, cc, ca)]
	ans = float('inf')
	if cc == ca:
		ans = s_a[i] + f(i+1, cc, ca-1)
	else:
		if ca > 0 and cc > 0:
			ans = s_a[i] + f(i+1, cc, ca-1)
			ans = min(ans, s_c[i] + f(i+1, cc-1, ca))
		elif ca == 0:
			ans = s_c[i] + f(i+1, cc-1, ca)
		elif cc == 0:
			ans = s_a[i] + f(i+1, cc, ca-1)
	dp[(i, cc, ca)] = ans
	return ans

print(f(0, n//2, n//2))


def f_opt(i, x, dp = {}):
    if i >= n:
        return 0
    if (i,x) in dp:
        return dp[(i,x)]
    ans = float('inf')
    if x == 0:
        ans = s_a[i] + f_opt(i+1, x+1)
    elif x == n-i:
        ans = s_c[i] + f_opt(i+1, x-1)
    else:
        ans = min(s_a[i] + f_opt(i+1, x+1), s_c[i] + f_opt(i+1, x-1))
    dp[(i,x)] = ans
    return ans

print(f_opt(0, 0))