n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v):
    if visited[v] == True:
        return
    visited[v] = True
    
    for i in arr[v]:
        if visited[i] == False:
            dfs(i)

for _ in range(m):
    u,v = map(int,input().split())
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)

cnt = 0
for i in range(n):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)
