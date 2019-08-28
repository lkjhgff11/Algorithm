from collections import deque
from pprint import pprint

dy = [1,0,0,-1]
dx = [0,1,-1,0]

r,c,t = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(r)]
air_cleaner = []

for tt in range(t):
    dust = []
    for y in range(r):
        for x in range(c):
            if 0 < grid[y][x]:
                dust.append((y,x))

            if grid[y][x] == -1:
                air_cleaner.append((y,x))
                
    
    # 먼지 전파
    spread = []
    for y,x in dust:
        if grid[y][x] < 5:
            continue

        add = grid[y][x]//5
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny in (-1,r) or nx in (-1,c) or grid[ny][nx] == -1:
                continue
                    
            grid[y][x] -= add
            spread.append((ny,nx,add))
                

    for y,x,add in spread:
        grid[y][x] += add


    #print("먼지전파{}".format(tt))
    #pprint(grid)
    #print()
    
    
    
    # 공기청정기 위쪽
    ay,ax = air_cleaner[0]
    for y in range(ay-1,0,-1): 
        grid[y][0] = grid[y-1][0]

    for x in range(c-1):
        grid[0][x] = grid[0][x+1]

    for y in range(ay):
        grid[y][c-1] = grid[y+1][c-1]

    for x in range(c-1,0,-1):
        grid[ay][x] = grid[ay][x-1]
        if x == 1:
            grid[ay][x] = 0
       

    # 공기청정기 아래쪽
    ay2,ax2 = air_cleaner[1]
    for y in range(ay2+1,r-1):
        grid[y][0] = grid[y+1][0]

    for x in range(c-1):
        grid[r-1][x] = grid[r-1][x+1]

    for y in range(r-1,ay2,-1):
        grid[y][c-1] = grid[y-1][c-1]

    for x in range(c-1,ax2,-1):
        grid[ay2][x] = grid[ay2][x-1]
        if x == 1:
            grid[ay2][x] = 0
    
        
    #print("공기청정기{}".format(tt))
    #print('------------------')
    #pprint(grid)              
    

print(sum(map(sum,grid))+2)
