import sys
sys.setrecursionlimit(3000)

def f(left, right, dp):
    
    if left > right:
        return 0
    
    if (left, right) in dp:
        return dp[(left, right)]

    score = max(
            arr[left] + min( f(left+2, right, dp), f(left+1, right-1, dp)),
            arr[right] + min(f(left+1, right-1, dp), f(left, right-2, dp))
    )  

    dp[(left, right)] = score
    return dp[(left, right)]


arr_len = int(input())
arr = [int(i) for i in input().split()]
# n = 4
# arr = [4,5,1,3]

l = 0
r = arr_len - 1
dp = {}
if arr_len - 1 == 0:
    print(arr[0])
else:
    print(f(l, r, dp))
    
print(dp)
    
    
    