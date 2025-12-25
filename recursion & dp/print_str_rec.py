def f(s:str,i=0):
    if i==len(s):
        return
    if s[i]!='x':
        print(s[i],end='')
    f(s,i+1)


def f1(s:str, out='', i=0):
    if i==len(s):
        return out
    if s[i]!='x':
        out += s[i]
    return f1(s,out,i+1)

s = 'abcxxadxacxe'
f(s)
print()
print(f1(s))

