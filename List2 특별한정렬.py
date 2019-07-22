t = int(input())
for tt in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    l = len(arr)
    mid = l//2
    slist = []
    for i in range(mid):
        slist.append(arr[l-i-1])
        slist.append(arr[i])

    ans= slist[:10]      
    print("#{} {}".format(tt," ".join(map(str,ans))))        
        
        
