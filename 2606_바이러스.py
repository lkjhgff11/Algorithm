com=int(input())
n=int(input())
graph=[""]+[[]for _ in range(com)]
visited=[]

for _ in range(n):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# node로부터 (여러 엣지를 걸쳐서라도) 연결되어있는 모든 노드를 반환하는 함수
def dfs(node):

    if node in visited:
        return
    visited.append(node)
    for near in graph[node]:
        dfs(near)
       
dfs(1)
print(len(visited)-1)
        
    
