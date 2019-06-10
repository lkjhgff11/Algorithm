from pprint import pprint
# 1은 이동가능, 0은 이동 불가능
n,m=map(int,input().split())
miro=[list(map(int,input()))for _ in range(n)]
visited=[[0]*6 for _ in range(n)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
cnt=0

# miro(y,x)에서 출발해서 miro(N-1,M-1)위치로 이동할때 지나는 최소의 칸수
def dfs(y,x):

    if y==n and x==m:
        return 1
 
    print("방문y x:",y,x)
    print("cnt",cnt)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or ny<0 or ny>n-1 or nx>m-1:
            continue

        if miro[ny][nx]==1 and visited[ny][nx]==0:
            visited[ny][nx]=2
            dfs(ny,nx)
            visited[y][x]=1
            
            return 1



print(dfs(0,0))

for i in visited:
    print(i)

