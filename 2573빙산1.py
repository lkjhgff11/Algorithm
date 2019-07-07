import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]

# 방향 돌면서 grid안의 저장된 칸수(0보다큰)가 녹아야 되는 횟수 기록하기.
def mel(y,x,cnt):

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue

        if grid[y][x]>0 and grid[ny][nx] == 0 :
            melt[y][x]+=1

            
def dfs(y,x):
    visited[y][x]=1

    for i in range(4): 
        ny=y+dy[i]
        nx=x+dx[i]

        if ny>=n or nx>=m or ny<0 or nx<0:
            continue

        elif grid[ny][nx]>=1 and visited[ny][nx]==0:
            dfs(ny,nx)            
     
cnt=0

while True:
    bf = [(i,j) for i in range(n) for j in range(m) if grid[i][j]]
    melt=[[0]*m for _ in range(n)]

    for y,x in bf:
        mel(y,x,cnt)
        
    for y in range(n):
        for x in range(m):
            grid[y][x] = max(0, grid[y][x] - melt[y][x])

    # sum(grid[y][x]for y in range(n) for x in range(n))
    if sum(sum(g) for g in grid)==0:
        print(0)
        break
        
    cnt+=1
    
    visited=[[0 for x in range(m)]for y in range(n)]
    dong=0
    for y in range(n):
        for x in range(m):
            if grid[y][x]>=1 and visited[y][x]== 0:
                dfs(y,x)
                dong+=1
                   
    if dong>=2:
        print(cnt)
        break
        
    
