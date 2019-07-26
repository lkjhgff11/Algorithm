# 맨 마지막줄 2에서 출발해서 제일 첫줄 3이있는 곳까지 도착하면 1, 도착 못하면 0
from pprint import pprint
dx = [0,1,0,-1]
dy = [1,0,-1,0]  

def path(x,y):
    global ans
    visited[x][y] = True
    if miro[x][y] == 3:
        ans = 1
        return 
         
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n :
            continue

        if visited[nx][ny]:
            continue

        if miro[nx][ny] != 1 and not visited[nx][ny]:
            path(nx,ny)
            
    if ans == 1:
        return ans
    return ans    
         

t = int(input())
for tt in range(1,t+1):
    n = int(input())
    miro = [list(map(int,input()))for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    ans = 0

    for x in range(n):
        for y in range(n):
            if miro[x][y] == 2:
                ans = path(x,y)
                
    print("#{} {}".format(tt,ans))        

    
