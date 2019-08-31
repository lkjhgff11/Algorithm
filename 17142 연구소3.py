from itertools import combinations
from collections import deque
from pprint import pprint
# 0:'O'빈칸, 1: '-'벽, 2: '#' 방문안한 비활성 바이러스(방문하면 *로 바뀐다.)

def get_time(virus):
    area = [g[:] for g in grid]
    dic = 'O-#'
    for y in range(n):
        for x in range(n):
            area[y][x] = dic[area[y][x]]
                           
    q = deque()
    for (y,x) in virus:
        q.append((y,x,0))

    time = MAX
    while q:
        y,x,cnt = q.popleft()
       
        if area[y][x] != '*':
            time = cnt
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny in (-1,n) or nx in (-1,n) or area[ny][nx] not in ('O','#'):
                continue

            if area[ny][nx] == '#':
                area[ny][nx] = '*'

            else:
                area[ny][nx] = cnt+1
            q.append((ny,nx,cnt+1))

    for y in range(n):
        for x in range(n):
            if area[y][x] == 'O':
                time = MAX

    return time


dy = [1,0,0,-1]
dx = [0,1,-1,0]
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
viruses = [(y,x)for y in range(n) for x in range(n) if grid[y][x] == 2]

MAX = 10 ** 10
ans = min(map(get_time,combinations(viruses,m)))
print(ans if ans != MAX else -1) 
