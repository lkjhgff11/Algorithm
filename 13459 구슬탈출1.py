import sys
from collections import deque
input = sys.stdin.readline

dy = [1,0,0,-1]
dx = [0,1,-1,0]


def move(y,x,dy,dx,cnt):
    while grid[y+dy][x+dx] != '#' and grid[y][x] != 'O':
          y += dy
          x += dx
          cnt += 1
    return y,x,cnt


def bfs():
    q = deque()
    q.append((ry,rx,by,bx,0))
    visited[ry][rx][by][bx] = True

    while q:
        cur_ry, cur_rx, cur_by, cur_bx, count = q.popleft()
        #print("cur_ry, cur_rx, cur_by, cur_bx, count ",cur_ry, cur_rx, cur_by, cur_bx, count )
        if count > 10:
            break
        
        for i in range(4):
            nxt_ry,nxt_rx,rc = move(cur_ry,cur_rx,dy[i],dx[i],0)
            nxt_by,nxt_bx,bc = move(cur_by,cur_bx,dy[i],dx[i],0)  

          #  print("nxt_ry,nxt_rx,rc",nxt_ry,nxt_rx,rc)
          #  print("nxt_by,nxt_bx,bc",nxt_by,nxt_bx,bc)
            if grid[nxt_by][nxt_bx] == 'O':
                continue

            if grid[nxt_ry][nxt_rx] == 'O' and grid[nxt_by][nxt_bx] != 'O' :
                if count < 10: 
                    print(1)
                    return
            
    
            if nxt_ry == nxt_by and nxt_rx == nxt_bx:
                if rc > bc:
                    nxt_ry -= dy[i]
                    nxt_rx -= dx[i]

                else:
                    nxt_by -= dy[i]
                    nxt_bx -= dx[i]

            if not visited[nxt_ry][nxt_rx][nxt_by][nxt_bx]:
                visited[nxt_ry][nxt_rx][nxt_by][nxt_bx] = True
                q.append((nxt_ry,nxt_rx,nxt_by,nxt_bx,count+1))
              
    print(0)        

n,m = map(int,input().split())
grid = [list(input())for _ in range(n)]
visited = [[[[False]*12 for _ in range(12)]for _ in range(12)]for _ in range(12)]

for y in range(n):
    for x in range(m):
        if grid[y][x] == 'R':
            ry,rx = y,x

        if grid[y][x] == 'B':
            by,bx = y,x

bfs()    
