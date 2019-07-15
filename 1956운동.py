import sys
from pprint import pprint
INF = sys.maxsize
v,e = map(int,input().split())
arr = [[INF]*v for _ in range(v)]
for _ in range(e):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    arr[a][b] = c


for k in range(v):
    for i in range(v):
        for j in range(v):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

ans = INF
for i in range(v):
    for j in range(v):
        if i==j:
            continue
        if arr[i][j] != INF and arr[j][i] != INF:
            ans = min(ans,arr[i][j] + arr[j][i])
            
if ans == INF:
    print(-1)

else:
    print(ans)
