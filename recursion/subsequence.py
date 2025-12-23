def f(arr):
    n = len(arr)
    x = -1 + 2**n
    
    while x>=0:
        if x==0:
            print()
            break
        temp=''
        num = bin(x)[2:].zfill(n)
        for i in range(len(num)):
            if num[i]=='1':
                print(arr[i],end='')
        print()
        x-=1
            

def f_opt(s,i=0,output=''):
    if i >= len(s):
        print(output)
        return
    f_opt(s,i+1,output+s[i])
    f_opt(s,i+1,output)
    
    
    

arr=[1,2,3]
f(arr)
print('-')
f_opt('1234')