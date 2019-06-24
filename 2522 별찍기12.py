n=int(input())

for i in range(n,0,-1):
    print(" "*(i-1)+"*"*(n-i+1))

for j in range(n,1,-1):
    print(" "*(n-j+1)+"*"*(j-1))
