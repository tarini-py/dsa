def f(n, output=''):# TLE O(3^n * n^2)
        if n==0:
            result.add(output)
            return
        f(n-1, '('+output+')')
        f(n-1, output+'()')
        f(n-1, '()'+output)
        for i in range(len(output) + 1):
            f(n - 1, output[:i] + '()' + output[i:])


def f_opt(n, open=0, close=0, output=''):# O(4^n / sqrt(n))
    if n==open==close:
        result_opt.append(output)
        return
    if open < n:
        f_opt(n, open+1, close, output+'(')
    if close < open:
        f_opt(n, open, close+1, output+')')


result=set()
n=5
f(n)
print(len(result))
print(result)

result_opt=[]
f_opt(n)
print(len(result_opt))
print(result_opt)

