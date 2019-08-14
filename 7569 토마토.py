# 익은토마토:1, 안익은토마토:0, 토마토 없는 칸:-1
from collections import deque
from pprint import pprint
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,0,1),(0,-1,0),(0,0,-1)]

m,n,h = map(int,input().split())
grid = [list()for _ in range(h)]

for i in range(h): # 쌓아올려지는 상자수만큼
    grid[i] = []
    for _ in range(n):
        grid[i].append(list(map(int,input().split())))

def get_all():
    for z in range(h):
        for y in range(n):
            for x in range(m):
                yield (z,y,x)
                
q = deque((0,z,y,x) for z,y,x in get_all() if grid[z][y][x] == 1)

cnt = 0                 
while q:
    cnt,z,y,x = q.popleft()

    for dz,dy,dx in dirs:
        nz,ny,nx = z+dz, y+dy, x+dx

        if nz in (-1,h) or ny in (-1,n) or nx in (-1,m):
            continue

        if grid[nz][ny][nx] == 0:
            grid[nz][ny][nx] = 1
            q.append((cnt+1,nz,ny,nx))    

              

if any(grid[z][y][x] == 0 for z,y,x in get_all()):
    print(-1)
else:
    print(cnt)
