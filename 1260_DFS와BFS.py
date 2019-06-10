from collections import *
import sys
sys.setrecursionlimit(100000)
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
n,m,v=map(int,input().split())
graph=[0]+[list()for _ in range(n)]
visited=[]
visited2=[]

for i in range(m):
    y,x = map(int,input().split())
    graph[y].append(x)
    graph[x].append(y)


for i in range(1,n+1):
    graph[i].sort()
    

def dfs(start,index):
    visited.append(start)    
    if index==n:
        return
    for i in graph[start]:
        if i in visited:
            continue
        
        dfs(i,index+1)
        
li=[]
def bfs(start):
    q=deque()
    if start not in visited2:
        visited2.append(start)
        q.append(start)

    while q: 
        li=q.popleft()
        
        for i in graph[li]:
            if i not in visited2:
                visited2.append(i)
                q.append(i)  
    return

dfs(v,0)
bfs(v)
print(*visited)
print(*visited2)
