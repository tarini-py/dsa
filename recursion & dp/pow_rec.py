def pow_r(a,n):
    if n==1:
        return a
    return a*pow_r(a,n-1)

print(pow_r(5,3))