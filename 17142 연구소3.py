# 0: 빈칸, 1: 벽, 2: 바이러스 위치
# 벽:-, 비활성바이러스: * , 활성바이러스: # (0 대신에 #을 활성바이러스로..)

def spread(virus,grid2,t):
    q = deque()
    for y,x in virus:
        grid2[y][x] = '#'
        q.append((y,x,0))
      
        
    for iy,ix in iv:
        if (iy,ix) in virus:
            continue
        grid2[iy][ix] = '*'

  
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny in (-1,n) or nx in (-1,n):
                continue 
            
            if grid2[ny][nx] == '*' :
                q.append((ny,nx,cnt+1))
                
                
            if grid2[ny][nx] == 0:
                grid2[ny][nx] = cnt+1
                q.append((ny,nx,cnt+1))    
               
    for y in range(n):
        for x in range(n):
            if grid2[y][x] == 0 :
                return
            if type(grid2[y][x]) == int:
                t = max(grid2[y][x],t)

                
    ans.append(t)           

        

from itertools import combinations
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline
dy = [1,0,0,-1]
dx = [0,1,-1,0]
n,m = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]
iv = [(y,x)for y in range(n) for x in range(n) if grid[y][x] == 2]
minn = sys.maxsize
  
# 1이던 벽을 - 로 고정
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            grid[y][x] = '-'

# 비활성 바이러스(iv)들 중에 활성 바이러스 m개 선택
av = list(combinations(iv,m))
ans = []

if all(grid[y][x] for y in range(n) for x in range(n)) in (1,2):
    print(0)
    
else:
    for a in av:
        g = [g[:] for g in grid]
        spread(a,g,-1)

    if ans == []:
        print(-1)
    
    else:
        print(min(ans))
