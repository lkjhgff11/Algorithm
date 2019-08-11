from collections import deque
dy = [-1,-1,-1,0,1,1,1,0]
dx = [-1,0,1,1,1,0,-1,-1]

r,c = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(r)]

ball = [[1]*c for _ in range(r)]


while True:
    before_ball = [b[:]for b in ball]
    for y in range(r):
        for x in range(c):       
            balls = []
            minn = 10 ** 10
            for i in range(8):
                ny = y+dy[i]
                nx = x+dx[i]

                if ny in (-1,r) or nx in (-1,c):
                    continue

                if grid[y][x] < grid[ny][nx]:
                    continue    

                if grid[y][x] > grid[ny][nx] and ball[y][x] != 0:
                    balls.append((ny,nx))

                
            # 가장 작은 정수칸 이동
            if len(balls) > 0:    
                for (a,b) in balls:
                    if minn > grid[a][b]:
                        minn = grid[a][b]
                        minn_xy = (a,b)
                
                ball[y][x] -= 1
                ball[minn_xy[0]][minn_xy[1]] += 1

    
    if before_ball == ball:
        break
               
for i in range(r):
    for j in range(c):
        print(ball[i][j],end=" ")
    print()            
