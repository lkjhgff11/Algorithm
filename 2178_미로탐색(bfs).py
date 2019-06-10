from collections import *
n,m=map(int,input().split())
miro=[list(map(int,input()))for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[1,0,0,-1]
dy=[0,1,-1,0]

q=deque()
q.append((0,0,1))

while q:
    y,x,dis = q.popleft()
    if y==n-1 and x==m-1:
        break
   
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue
        
        if miro[ny][nx]==1 and visited[ny][nx]==0:
            visited[ny][nx]=2
            q.append((ny,nx,dis+1))


print(dis)    
