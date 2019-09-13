import sys
dy = [0,1,0,-1] #  오른쪽 밑 왼쪽 위
dx = [1,0,-1,0]

# y,x좌표를 입력받으면 d방향으로 감시            
def watch(y,x,d): 
    ny = y + dy[d]
    nx = x + dx[d]

    if ny in (-1,n) or nx in (-1,m):
        return

    if grid[ny][nx] == 6:
        return
    
    grid[ny][nx] = -1
    watch(ny,nx,d)
       

# 감시 안된 영역 구하기
def safe_area(grid):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if grid[y][x] == 0:
                cnt += 1
    return cnt

    
def dfs(index):
    global grid
    global ans
    if index == cctv_cnt:
        cnt = safe_area(grid)
        if cnt < ans:
            ans = cnt
        return
    copy = [g[:]for g in grid]

    for i in range(4):
        if cctv[index][0] == 1: # 한방향
            watch(cctv[index][1],cctv[index][2],i)

        if cctv[index][0] == 2: # 반대방향
            watch(cctv[index][1],cctv[index][2],i)
            watch(cctv[index][1],cctv[index][2],(i+2)%4)

        if cctv[index][0] == 3: # 직각방향
            watch(cctv[index][1],cctv[index][2],i)
            watch(cctv[index][1],cctv[index][2],(i+1)%4)

        if cctv[index][0] == 4: # ㅗ 방향 
            watch(cctv[index][1],cctv[index][2],i)
            watch(cctv[index][1],cctv[index][2],(i+1)%4)
            watch(cctv[index][1],cctv[index][2],(i+2)%4)
            
        if cctv[index][0] == 5: # + 방향 
            watch(cctv[index][1],cctv[index][2],i)
            watch(cctv[index][1],cctv[index][2],(i+1)%4)
            watch(cctv[index][1],cctv[index][2],(i+2)%4)
            watch(cctv[index][1],cctv[index][2],(i+3)%4)
            
        dfs(index+1)
        grid = [c[:]for c in copy]


ans = sys.maxsize 
n,m = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]

cctv = []
for y in range(n):
    for x in range(m):
        if grid[y][x] in range(1,6):
            cctv.append((grid[y][x],y,x))

cctv_cnt = len(cctv)
dfs(0)
print(ans)
