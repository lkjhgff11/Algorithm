dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input())
grid = [list(map(int,input().split()))for _ in range(n)]
visited = [[False]*n for _ in range(n)]
q = []
fish_cnt = 0
ans = 0
for x in range(n):
    for y in range(n):
        if grid[x][y] == 9:
            start_x,start_y = x,y
            grid[x][y] = 0
        if grid[x][y] != 0 and grid[x][y] < 2:
            fish_cnt += 1

q.append((0,start_x,start_y,2,0,fish_cnt))
if fish_cnt == 0:
    ans = 0

elif fish_cnt >= 1:
    while True:
        q.sort()
        if len(q) == 0:
            break
        dis,cur_x, cur_y, baby_size, eat_num,fish_cnt = q.pop(0)
      
        #print("cur_x, cur_y, baby_size, eat_num,fish_cnt,dis",cur_x, cur_y, baby_size, eat_num,fish_cnt,dis)

        # 공백(0)이 아니고, 아기고래보다 사이즈 작으면 물고기 냠냠
        if grid[cur_x][cur_y] != 0 and grid[cur_x][cur_y] < baby_size:
            grid[cur_x][cur_y] = 0
            visited = [[False]*n for _ in range(n)]
            visited[cur_x][cur_y] = True
            fish_cnt -= 1
            eat_num += 1
            ans += dis
            #print("현재거리",ans)
            dis = 0
            q = []
            q.append((dis,cur_x,cur_y,baby_size,eat_num,fish_cnt))
            q.pop(0)
            #print("물고기 먹고난후 q,cur_x,cur_y,eat_num,fish_cnt,dis",q,cur_x,cur_y,eat_num,fish_cnt,dis)
            #print(grid)
             
            
        # 먹은 물꼬기수가 아기상어크기보다 많으면 아기상어크기 1 증가시키고, 먹은거는 다시 0으로 초기화
        # 커진 아기상어 크기에따라 먹을수있는 물고기수 다시 세기
        if eat_num >= baby_size :      
            baby_size += 1
            eat_num = 0
            fish_cnt = 0
            #visited = [[False]*n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if grid[x][y]!=0 and grid[x][y] < baby_size:
                        fish_cnt += 1                      
        
        if fish_cnt == 0:
            break

        # 물고기수 한마리이상
        else:      
            for i in range(4):
                nx = cur_x + dx[i]
                ny = cur_y + dy[i]

                if nx in (-1,n) or ny in (-1,n):
                    continue

                if grid[nx][ny] <= baby_size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((dis+1,nx,ny,baby_size,eat_num,fish_cnt))
                           

print(ans)            
    
