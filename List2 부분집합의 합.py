
t = int(input())


for tt in range(1,t+1):
    a = [i for i in range(1,5)]
    n,k = map(int,input().split())
    l = len(a)
    li = []
    for i in range(1<<l):
        print(bin(i)[2:].zfill(l))
        li2 = []
        for j in range(l):
            if i&(1<<j):
                li2.append(a[j])
                
        li.append(li2)
        
    cnt = 0    
    for l in li:
        if len(l) == n and sum(l) == k:
            cnt += 1
            

    print("#{} {}".format(tt,cnt))
