def f(r,c):
    if r==0:
        return
    print("*"*c)
    f(r-1,c)
    
def f1(n,i=0):
    if i==n:
        return
    print("*"*n)
    f1(n,i+1)

def p1(n):
    if n==0:
        return
    print('*'*n)
    p1(n-1)

def p1_rev(n):
    if n==0:
        return
    p1_rev(n-1)
    print('*'*n)

f(2,2)
print()
f1(5)
print()

p1(5)
print()

p1_rev(5)