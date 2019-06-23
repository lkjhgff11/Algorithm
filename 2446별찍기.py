# 9  7  5  3  1  3  5 7  9
n=int(input())

for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(i*2-1))


# 3  5  7  9
s=1
for j in range(1,n):  # 3 5 
    s=s+2
    print(' '*(n-j-1)+'*'*s)
    


#     
