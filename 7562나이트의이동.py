from collections import deque
t = int(input())

dx = [1, 2,  2,  1,  -1, -2, 2, -1]
dy = [2, 1, -1, -2,  -2, -1, 1,  2] 
# 한변의 길이 i , 현재있는칸 y1,x1, 나이트가 이동하려는칸 y2,x2 
for _ in range(t):

    n = int(input())
    y1,x1 = map(int,input().split())
    y2,x2 = map(int,input().split())

    visited=[[0]*n for _ in range(n)]

    q=deque([(y1,x1,0)])

    while q:
        y,x,cnt=q.popleft()

        if y==y2 and x==x2:
            print(cnt)
            break

            
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
         
            if ny<0 or nx<0 or ny>=n or nx>=n:
                continue
              
            if visited[ny][nx]==0:
                q.append((ny,nx,cnt+1))
                visited[ny][nx]=1

    
