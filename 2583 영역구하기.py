import sys
sys.setrecursionlimit(10**6)
from pprint import pprint
dy = [1,0,0,-1]
dx = [0,1,-1,0]
m,n,k = map(int,input().split())
grid = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]

def dfs(y,x):
    global cnt
    visited[y][x] = True
    cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny in (-1,m) or nx in (-1,n):
            continue

        if grid[ny][nx] == 0 and not visited[ny][nx]:
            dfs(ny,nx)
            
      
for _ in range(k):
    lx, ly, rx, ry = map(int,input().split())

    for y in range(ly,ry):
        for x in range(lx,rx):
            grid[y][x] = 1
          

ans = []
for y in range(m):
    for x in range(n):
        if grid[y][x] == 0 and not visited[y][x]:
            cnt = 0
            dfs(y,x)
            ans.append(cnt)

ans_cnt = len(ans)
ans.sort()
print(ans_cnt)
print(*ans)
