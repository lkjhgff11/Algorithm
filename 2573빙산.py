n,m=map(int,input().split())
grid=[list(map(int,input().split()))for _ in range(n)]
grid2=[g[:]for g in grid]
grid3=[g[:]for g in grid]
visited=[[0]*m for _ in range(n)]
      
dx=[1,0,0,-1]
dy=[0,1,-1,0]


# 연결
def dfs(y,x):
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue

        if grid[ny][nx]!=0 and visited[ny][nx]==0:
            visited[ny][nx]=1
            dfs(ny,nx)



# 연결요소 갯수 구하기.
def connect():
    concnt=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]!=0 and grid[i][j]>0:
                concnt+=1
                dfs(i,j)
    return concnt



#빙하 녹이기
def melt(y,x):
    cnt=0

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue

        if grid[ny][nx]<=0 and grid[y][x]>0:
            cnt+=1

    return cnt        
    



while True:
    for i in range(n):
        for j in range(m):
            grid2[i][j]=melt(i,j)

    for i in range(n):
        for j in range(m):
            if grid3[i][j]<grid2[i][j]:
                grid3[i][j]=0
            grid3[i][j]-=grid2[i][j]

    cn=connect()
    
    if cn<1:
        print(0)
        break
    else:
        print(cn)
        break
