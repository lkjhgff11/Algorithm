t = int(input())
for tt in range(t):
    n = int(input())
    board = [[0]*30 for _ in range(30)]
  
    for _ in range(n):
        start_x,start_y,dst_x,dst_y,color = map(int,input().split())

        for i in range(start_x,dst_x+1):
            for j in range(start_y,dst_y+1):
                board[i][j] += color        

    cnt = 0
    for x in range(30):
        for y in range(30):
            if board[x][y] == 3:
                cnt += 1

    print("#{} {}".format(tt+1,cnt))
 
