h,w,n = 7,9,4
board = ['111100000','000010011','111100011','111110011','111100011','111100010','111100000']

# (y,x)지점에서 dy,dx방향으로의 목이 몇목인가?


def get_cnt(y,x,dy,dx):
    if y in (-1,h) or x in (-1,w):
        return 0
    if board[y][x] == '0':
        return 0
    
    if board[y][x] == '1':
        return 1+get_cnt(y+dy,x+dx,dy,dx)
    
ans = 0
dirs = [(0,1), (1,0), (1,1), (-1,1)]
for y in range(h):
    for x in range(w):
        for dy,dx in dirs:
            py,px = y-dy,x-dx
            if py not in (-1,h) and px not in (-1,w):

                if board[py][px] == '1':
                    continue
            
            mok = get_cnt(y,x,dy,dx)
            if mok == n:
                ans += 1
print(ans)            
        
