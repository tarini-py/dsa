def f(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )
    print('max lcs length: ',dp[-1][-1])
    
    lcs = '' #largest common subsequence
    scs = '' #shortest common supersequence
    #print(m,n)
    while m != 0 and n != 0:
        #print(m,n)
        if str1[m-1] == str2[n-1]:
            lcs = str1[m-1] + lcs
            scs = str1[m-1] + scs
            m -= 1
            n -= 1
        else:
            if dp[m][n-1] > dp[m-1][n]:
                scs = str2[n-1] + scs
                n -= 1
            else:
                scs = str1[m-1] + scs
                m -= 1

    while m != 0:
        scs = str1[m-1] + scs
        m -= 1

    while n != 0:
        scs = str2[n-1] + scs
        n -= 1

    print('lcs : ',lcs)
    print('scs : ',scs)
    

f("afbxyac", "fcaxby")
f("aaaaaaaa", "aaaaaaaa")