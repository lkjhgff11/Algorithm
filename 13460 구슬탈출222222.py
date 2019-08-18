from collections import deque
dy = [1,0,0,-1]
dx = [0,1,-1,0]
n,m = map(int,input().split())
grid = [list(input())for _ in range(n)]
visited = [[[[False]*13 for _ in range(13)]for _ in range(13)]for _ in range(13)]
q= deque()

for y in range(n):
    for x in range(m):
        if grid[y][x] == 'R':
            start_ry,start_rx = y,x

        if grid[y][x] == 'B':
            start_by,start_bx = y,x

        if grid[y][x] == 'O':
            goal = y,x

q.append((start_ry,start_rx,start_by,start_bx,0))
visited[start_ry][start_rx][start_by][start_bx] = True

def move(y,x,dy,dx,cnt):
    while grid[y+dy][x+dx] != '#' and grid[y][x] != 'O':
        y += dy
        x += dx
        cnt +=1
    return y,x,cnt


def bfs():
    while q:
        cur_ry,cur_rx,cur_by,cur_bx,count = q.popleft()
        if count > 10:
            break

        for i in range(4):
            rny,rnx,rc = move(cur_ry,cur_rx,dy[i],dx[i],0)
            bny,bnx,bc = move(cur_by,cur_bx,dy[i],dx[i],0)

            if grid[bny][bnx] == 'O':
                continue

            if grid[rny][rnx] == 'O' and grid[bny][bnx] != 'O':
                if count <= 10:
                    print(count+1)
                    return
                
            if rny == bny and rnx == bnx:
                if rc > bc:
                    rny = rny-dy[i]
                    rnx = rnx-dx[i]

                else:
                    bny = bny-dy[i]
                    bnx = bnx-dx[i]

            if not visited[rny][rnx][bny][bnx]:
                visited[rny][rnx][bny][bnx] = True
                q.append((rny,rnx,bny,bnx,count+1))

    print(-1)

bfs()
