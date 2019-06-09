r,c=map(int,input().split())
board=[list(input())for _ in range(r)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]

# 지금까지 visited한 알파벳은 제외하고,
# y,x지점에서 출발해서 갈 수 있는 최대거리를 반환한다.
def dfs(y,x,visited):
    visited.add(board[y][x])
    maxx = 0
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or nx>=c or ny>=r:
            continue

        if board[ny][nx] not in visited:
            maxx = max(maxx,dfs(ny,nx,visited))
    visited.remove(board[y][x])
    return 1+maxx
            
print(dfs(0,0,set()))
