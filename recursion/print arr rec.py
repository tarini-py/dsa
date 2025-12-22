import numpy as np

def print_arr(arr,i=0):
    if i==len(arr):
        return
    print(arr[i],end=' ')
    print_arr(arr,i+1)
    

arr = np.random.randint(2,99,(15,))
print(arr)
print_arr(arr)