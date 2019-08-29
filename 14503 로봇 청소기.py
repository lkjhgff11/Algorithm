# 둘째줄 0: 북쪽(-1,0), 1: 동쪽(0,1), 2: 남쪽(1,0), 3: 서쪽(0,-1)
# 셋째줄 0: 빈칸, 1: 벽

# 현재방향에서 왼쪽방향으로 회전
def spin_left(n):
    if n == (-1,0):  # 북쪽에서 왼쪽은 서쪽
        return (0,-1)

    if n == (0,1):  # 동쪽에서 왼쪽은 북쪽
        return (-1,0)

    if n == (1,0):  # 남쪽에서 왼쪽은 동쪽
        return (0,1)

    if n == (0,-1):  # 서쪽에서 왼쪽은 남쪽
        return (1,0)

# 이제 후진만 제대로 하자
# 한칸후진
def back(n):
    if n == (-1,0): # 북쪽 뒤는 남쪽
        return (1,0)
    
    if n == (0,1):   # 동쪽 뒤는 서쪽
        return (0,-1)
    
    if n == (1,0):  # 남쪽 뒤는 북쪽
        return (-1,0)
    
    if n == (0,-1): # 서쪽 뒤는 동쪽
        return (0,1)

 # 탐색 진행
def search(y,x,d):
   
    (sy,sx) = spin_left(d)
    ny = y + sy
    nx = x + sx

    cnt = 0 # 벽이거나 청소 다 되있는경우 cnt 증가
    for i in range(4):
        dir_y = y + dy[i]
        dir_x = x + dx[i]

        if grid[dir_y][dir_x] != 0: # 벽(1)이거나 청소가 다 되어있으면(5)  cnt+1 한다.
            cnt += 1

    if cnt == 4:
       # print("back해서 돌아가야댐",y,x,d)
        (by,bx) = back(d)
        bny = y + by
        bnx = x + bx

        if grid[bny][bnx] == 1:
            return
    
        else:
            #print("back했다",bny,bnx,d)
            search(bny,bnx,d)

    if cnt != 4:
        if ny not in (-1,n) or nx not in (-1,m):
            if grid[ny][nx] == 0:
                cleaning(ny,nx,(sy,sx))
                return

            if grid[ny][nx] != 0 :
                search(y,x,(sy,sx))
                return
                     
                          
# 청소한거를 5로  표시하기
def cleaning(y,x,d):
    global summ

    # 현재위치 청소
    if grid[y][x] == 0:
        grid[y][x] = 5
        summ += 1
       # print("청소y,x,d,summ",y,x,d,summ)

        search(y,x,d)
        return
       
       
import sys
from pprint import pprint
sys.setrecursionlimit(10**6)
dy = [1,0,0,-1]
dx = [0,1,-1,0]
n,m = map(int,input().split())
cur_y,cur_x,d = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]

if d == 0:
    d = (-1,0)
if d == 1:
    d = (0,1)
if d == 2:
    d = (1,0)
if d == 3:
    d = (0,-1)

summ = 0
cleaning(cur_y,cur_x,d)    
print(summ)
