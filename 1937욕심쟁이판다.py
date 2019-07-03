import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

#dir=[[0,1],[1,0],[0,-1],[-1,0]]
dx=[1,0,0,-1]
dy=[0,1,-1,0]

n=int(input())
grid=[list(map(int,input().split()))for _ in range(n)] # 각 대나무의 갯수
check=[[0]*n for _ in range(n)]  # 각 대나무가 있는 위치에서의 판다의 최대 생존일수. 

def dfs(y,x):

    if check[y][x]==0:
        check[y][x]=1

        for i in range(4):       
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
                
            if grid[y][x]<grid[ny][nx]:
                print("y,x check[y][x],ny,nx,dfs(ny,nx)+1",y,x,check[y][x],ny,nx,dfs(ny,nx)+1)
                check[y][x]=max(check[y][x],dfs(ny,nx)+1)
                print("max넣은 check[y][x]",check[y][x])
                
    return check[y][x]   

maxx=0
for y in range(n):
    for x in range(n):
        if check[y][x]==0:
            maxx=max(maxx,dfs(y,x))
       
print(maxx)    
