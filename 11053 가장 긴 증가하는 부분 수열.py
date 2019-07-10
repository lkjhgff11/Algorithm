n = int(input())
arr = list(map(int,input().split()))

maxx = 0
dp=[0]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
    maxx = max(dp[i],maxx)

print(maxx+1)    
          
