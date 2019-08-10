from pprint import pprint
dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c,n = map(int,input().split())
grid = [list(input())for _ in range(r)]
time = [[0]*c for _ in range(r)]

cnt = 0
for y in range(r):
        for x in range(c):
            if grid[y][x] == 'O':
                time[y][x] = 1
cnt += 1
while True:
    bomb = set()
    if cnt == n:
        break
    
    cnt += 1
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'O':
                time[y][x] += 1
                
            if grid[y][x] == '.' :
                grid[y][x] = 'O'
                time[y][x] += 1
    #print("==============={}=================".format(cnt))
    #pprint(grid)
    #pprint(time)
    if cnt == n:
        break
                
    cnt += 1
    for y in range(r):
        for x in range(c):
            if time[y][x] == 2:
                grid[y][x] = '.'
                bomb.add((y,x))

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if ny in (-1,r) or nx in (-1,c):
                        continue

                    grid[ny][nx] = '.'
                    bomb.add((y,x))

    if cnt == n:
        break
    
    for (y,x) in bomb:
        time[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny in (-1,r) or nx in (-1,c):
                continue
            time[ny][nx] = 0
            
    #print("==============={}=================".format(cnt))
    #pprint(grid)
    #pprint(time)

for g in grid:
    print("".join(g))
