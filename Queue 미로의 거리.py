from collections import deque
from pprint import pprint
dx = [1,0,0,-1]
dy = [0,1,-1,0]

# 0: 통로, 1: 벽, 2: 출발, 3: 도착


def bfs(x,y,cnt):
    q.append((x,y,cnt))
    visited[x][y] = True

    while q:
        cur_x,cur_y,cnt = q.popleft()
        for i in range(4):
            nxt_x = cur_x + dx[i]
            nxt_y = cur_y + dy[i]

            if nxt_x in (-1,n) or nxt_y in(-1,n):
                continue

            if miro[nxt_x][nxt_y] == 3:
                return cnt

            if miro[nxt_x][nxt_y] == 0 and not visited[nxt_x][nxt_y]:
                q.append((nxt_x,nxt_y,cnt+1))
                visited[nxt_x][nxt_y] = True
    return 0
    

t = int(input())
for tt in range(1,t+1):
    n = int(input())
    miro = [list(map(int,input()))for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    q = deque()
    cnt = 0
    for x in range(n):
        for y in range(n):
            if miro[x][y] == 2:
                cnt = bfs(x,y,cnt)
    print("#{} {}".format(tt,cnt))
