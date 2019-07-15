import sys
from pprint import pprint
input = sys.stdin.readline
minn = 999999
n,m = map(int,input().split())
arr = [[minn]*n for _ in range(n)]
for _ in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    arr[u][v]=1
    arr[v][u]=1

for k in range(n):   # 거쳐가는거
    for i in range(n): # 출발하는거
        for j in range(n): # 도착하는거
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = arr[j][i] = 0

#pprint(arr)
            
ans = 0
for i in range(n):
    summ = 0
    for j in range(n):
        summ += arr[i][j]
    if summ < minn:
        minn = summ
        ans = i

print(ans+1)
