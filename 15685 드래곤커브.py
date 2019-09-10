dy = [0,-1,0,1]
dx = [1,0,-1,0]

n = int(input())
grid = [[0]*102 for _ in range(102)]
for _ in range(n):
    curves = []
    x,y,d,g = map(int,input().split())
    curves.append(d)

    for j in range(g):           # 드래곤 커브 세대별 좌표 구하기 
        for k in range(len(curves)-1,-1,-1):
            curves.append((curves[k]+1) % 4) 
 
    # 커브에 해당하는 좌표들 grid에 그리기        
    grid[y][x] = 1
    for i in curves:
        y = y + dy[i]
        x = x + dx[i]
        grid[y][x] = 1



# 정사각형 갯수 카운팅
cnt = 0    
for y in range(102):
    for x in range(102):
        if grid[y][x] == 1 and grid[y+1][x] == 1 and grid[y+1][x-1] == 1 and grid[y][x-1] == 1:
            cnt += 1
        
print(cnt)
