import numpy as np

def f(arr,n,i=0):
    if i==len(arr):
        return f"Element {n} not found\n"
    if arr[i]==n:
        return f"Element {arr[i]} found at index = {i}\n"
    return f(arr,n,i+1)

arr = [32,7826,8,3,5,90,12]

print(f(arr,90))
print(f(arr,0))