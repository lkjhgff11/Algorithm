def paper(a):
    if a == n:
        return 1
    if a > n:
        return 0
    return paper(a+10) + (2*paper(a+20)) 


t = int(input())    
for tt in range(1,t+1):
    n = int(input())
    ans = paper(0)    
    print("#{} {}".format(tt,ans))
