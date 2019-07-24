t = int(input())

def dfs(start):
    global ans
    visited[start] = 1
    for nxt in range(1,v+1):
        if graphMap[start][nxt] and not visited[nxt]:
            if nxt == g:
                ans = 1
                return ans
            dfs(nxt)

for tt in range(1,t+1):
    v,e = map(int,input().split())
    graphMap = [[0]*(v+1) for _ in range(v+1)]
    visited = [0]*(v+1)
    for _ in range(e):
        start,end = map(int,input().split())
        graphMap[start][end] = 1

    s,g = map(int,input().split()) # 경로 존재확인    
    
    ans = 0    
    dfs(s)   
    print("#{} {}".format(tt,ans))
