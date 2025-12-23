
def f(n,k,start='M'):
    
    for _ in range(n-1):
        temp=''
        for i in start:
            if i=='M':
                temp+='MF'
            else:
                temp+='FM'
        start = temp
    
    return start,start[k-1]

def f_rec(n,k,i=0,start='M'):
    if len(start)==2**n - 1:
        return start[(-1+2**(n-1)):], start[(-1+2**(n-1))+k-1]
    if start[i]=='M':
        return f_rec(n,k,i+1,start+'MF')
    else:
        return f_rec(n,k,i+1,start+'FM')
    

def f_opt(n,k,start='M'):
    if n==1:
        return start
    if k <= (2**(n-1))//2:
        return f_opt(n-1,k,start)
    else:
        if start == 'M':
            start = 'F'
        else:
            start = 'M'
        return f_opt(n-1,k - (2**(n-1))//2,start)

n=10
k=8

print(f(n,k))
print(f_rec(n,k))
print(f_opt(n,k))
    
    
    
    


