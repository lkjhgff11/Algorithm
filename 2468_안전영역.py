import sys
sys.setrecursionlimit(10**6)
n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)]
visited=[[0]*n for _ in range(n)]

dx=[1,0,0,-1]
dy=[0,1,-1,0]


#안전영역 4방향 돌기
def dfs(y,x,area):

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
       
        if area[ny][nx]!=0 and visited[ny][nx]==0:
            visited[ny][nx]=1
            dfs(ny,nx,area)
           
cnt=0
maxx=0
init_max = max(grid[y][x] for y in range(n) for x in range(n))
# 물에 잠기기
def water(x,area):
    for i in range(n):
        for j in range(n):
            if area[i][j]<=x:
                area[i][j]=0

    return area
    
for i in range(init_max):
    area = [g[:] for g in grid]
    water(i,area)
    cnt=0
    # dfs로 안전지대 구하기.
    visited=[[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):   
            if area[y][x]!=0 and visited[y][x]==0:
                dfs(y,x,area)               
                cnt+=1
 
    maxx=max(maxx,cnt)              
print(maxx)
