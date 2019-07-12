n=int(input())
cnt = 0
while n > 0:
    n -= cnt
    cnt += 1
n = cnt + n -1

if cnt % 2 != 0 :
    print("{}/{}".format(n,cnt-n))

if cnt % 2 == 0:
    print("{}/{}".format(cnt-n,n))


    
    
