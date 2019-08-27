from collections import deque
from pprint import pprint

def bfs(y,x,w_cnt,s_cnt):
    global ans_w, ans_s
    visited = [[False]*c for _ in range(r)]
    q = deque()
    visited[y][x] = True
    q.append((y,x))
   
    while q:
        #print(q)
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny in (-1,r) and nx in (-1,c):
                continue

            if grid[ny][nx] == '#' or visited[ny][nx]:
                continue

            if not visited[ny][nx]:

                if grid[ny][nx] == 'v':
                    w_cnt += 1
                    grid[ny][nx] = '.'
                    visited[ny][nx] = True
                    q.append((ny,nx))
    
                if grid[ny][nx] == 'k':
                    s_cnt += 1
                    grid[ny][nx] = '.'
                    visited[ny][nx] = True
                    q.append((ny,nx))

                if grid[ny][nx] == '.':
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    
    if w_cnt >= s_cnt:
        ans_w += w_cnt

    if s_cnt > w_cnt:
        ans_s += s_cnt

dx = [1,0,0,-1]
dy = [0,1,-1,0]
r,c = map(int,input().split())
grid = [list(input())for _ in range(r)]
ans_w = 0
ans_s = 0

for y in range(r):
    for x in range(c):
        if grid[y][x] == 'v':
            grid[y][x] = '.'
            bfs(y,x,1,0)
         
        if grid[y][x] == 'k':
            grid[y][x] = '.'        
            bfs(y,x,0,1)
            
print(ans_s,ans_w)
