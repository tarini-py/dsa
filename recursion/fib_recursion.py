def fib(a,b,cnt):
    if cnt == 0:
        return
    print(a)
    fib(b,a+b,cnt-1)

def fib_n(a,b,cnt):
    print(a)
    print(b)
    for i in range(cnt-2):
        a,b= b,a+b
        print(b)



a=0
b=1
cnt=10
print("fib")
fib(a,b,cnt)
print("\nfib_n")
fib_n(a,b,cnt)

