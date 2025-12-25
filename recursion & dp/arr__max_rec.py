import math

def f_max(arr:list, i = 0, m = -math.inf)-> int:
    if i == len(arr):
        return m
    m = max(m, arr[i])
    return f_max(arr,i+1,m)

def f_max2(arr:list, i = 0)-> int:
    if i==len(arr)-1:
        return arr[i]
    return max(arr[i],f_max2(arr,i+1))

def f_sum(arr,i=0):
    if i==len(arr)-1:
        return arr[i]
    return arr[i]+f_sum(arr,i+1)

arr = [23,1,4,121,12,56,87,2]

print(f_max(arr))
print(f_max2(arr))
print(f_sum(arr))

print(sum(arr))
    