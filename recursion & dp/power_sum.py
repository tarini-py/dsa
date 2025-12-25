import math
count=0
def f(x,n,i=1):
    global count
    if x==0:
        count+=1
        return
    
    if x<0:
        return
    
    if i > math.sqrt(x):
        return
    
    f(x-(i**n), n, i+1)
    f(x,n,i+1)
    

x=100
n=3

print(f(x,n))
print(count)