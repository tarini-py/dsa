def f(n: int):
    if n==0:
        return 0
    return (n % 10) + f(n//10)

print(f(12345))