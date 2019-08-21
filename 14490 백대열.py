def gcd(a,b):
    if a<b:
        a,b = b,a

    if a%b:
        g = gcd(a%b,b)
        return g

    else:
        return b
        

n,m = map(int,input().split(':'))
g = gcd(n,m)
print(n//g,m//g,sep=':')
