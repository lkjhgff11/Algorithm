n = int(input())
m = int(input())

grid = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    grid[a][b] = 1


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = 1 


for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if not grid[i][j] and not grid[j][i]:
            cnt += 1
    print(cnt-1)    
