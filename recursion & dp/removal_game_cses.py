
def f(n, left, right):
    
    if n <= 0:
        return 0
    
    score = 0

    if left < right and left < n and right > 0:
        score = max(
                arr[left] + max(f(n-2, left+2, right), f(n-2, left+1, right-1)),
                arr[right] + max(f(n-2, left+1, right-1), f(n-2, left, right-2))
        )

    return score
    
    




n = 4
arr = [4,5,1,3]

left = 0
right = len(arr) - 1

print(f(n, left, right))
    
    
    