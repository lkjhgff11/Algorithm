t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    hap = 0
    maxx = 0
    minn = 10**6
    for a in range(n-m+1):
        for b in range(a,a+m):
            hap = hap + arr[b]
            
        if hap > maxx:
            maxx = hap

        if hap < minn:
            minn = hap

        hap = 0

    ans = maxx-minn

    print("#{} {}".format(i+1,ans))
        
