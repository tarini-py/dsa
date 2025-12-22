def fact_r(n):
    if n==0:
        return 1
    return n*fact_r(n-1)


def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)

print(fact_r(30))
print(fact_r(0))
print(sum_n(100))
