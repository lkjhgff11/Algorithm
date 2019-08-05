# 0: 빈칸 , 1: 벽, 2: 바이러스
from pprint import pprint
dx = [1,0,0,-1]
dy = [0,1,-1,0]
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
maxx = 0

# 퍼트릴 바이러스들의 좌표를 담음
vr = []
for x in range(n):
    for y in range(m):
        if grid[x][y] == 2:
            vr.append((x,y))

            
# 벽 세우기
def build_wall(index):
    global maxx
    if index == 3:
        grid2 = [g[:] for g in grid]
       # print(grid2)

        for a,b in vr:
            virus(a,b,grid2)
        maxx = max(maxx,sum(1 for x in range(n) for y in range(m) if grid2[x][y] == 0))
        return maxx                   

    else:
        for cur_x in range(n):
            for cur_y in range(m):
                if grid[cur_x][cur_y] == 0 :
                    grid[cur_x][cur_y] = 1
                    build_wall(index+1)
                    grid[cur_x][cur_y] = 0
                   
                    
# 바이러스 퍼뜨리기
def virus(x,y,grid2):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx in (-1,n) or ny in (-1,m):
            continue

        if grid2[nx][ny] == 0:
            grid2[nx][ny] = 2
            virus(nx,ny,grid2)
    return grid2            

build_wall(0)
print(maxx)

