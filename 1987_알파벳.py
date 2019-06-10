r,c=map(int,input().split())
board=[list(map(str,input()))for _ in range(r)]
#check=[list(0 for _ in range())for _ in range(r)]
visited=[]

dx=[1,0,0,-1]
dy=[0,1,-1,0]
cnt=0

# y,x 좌표를 돌며 visited에 추가
def dfs(y,x):
    visited.append(board[y][x])
    print("y,x",y,x)
    print("@visited",visited)
        
              
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if ny<0 or nx<0 or ny>=r or nx>=c:
            continue

        if board[ny][nx] in visited:
            continue
        
        if board[ny][nx] not in visited:
            dfs(ny,nx)

            
dfs(0,0)
print(len(visited))


