# 익은토마토:1, 안익은토마토:0, 토마토가없는 빈칸:-1
from collections import deque
m,n = map(int,input().split())  # m은 가로, n은 세로
box = [list(map(int,input().split())) for _ in range(n)]
visited=[[0 for _ in range(m)]for _ in range(n)]
dirs=[0,1,0,-1,0]

q= deque()
# 첨에 토마토 익은것들 다 큐에 넣기
for y in range(n):
    for x in range(m):
        if box[y][x]==1:
            q.append((y,x))
            visited[y][x]=1


day=0
# 큐에서 익은거 중심으로 상하좌우 익히기
while q:
    size = len(q)

    for _ in range(size):
        y,x = q.popleft()    
        #print("#",y,x)

        for i in range(4):
            ny=y+dirs[i]
            nx=x+dirs[i+1]
    
            if ny in (-1,n) or nx in (-1,m):
                continue

            if box[ny][nx]==1 or box[ny][nx]==-1:
                continue
        

            # 토마토 익히기
            if box[ny][nx]==0 and visited[ny][nx]==0:
                box[ny][nx]=1
                visited[ny][nx]=1
                q.append((ny,nx))
    day+=1
     
    
for y in range(n):
    for x in range(m):
        if box[y][x]==0:
            day=0
            print(-1)
            exit()
            
if day!=0:
    print(day-1)





