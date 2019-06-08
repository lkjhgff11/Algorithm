from collections import deque
import math
cnum=int(input())
n=int(input())
graph=[]
graph2=[[0]*100 for _ in range(100)]
visited = set([])

for _ in range(n):
    y,x = map(int,input().split())
    graph.append((y,x))
    graph2[y][x]=1

q = deque()
cnt = 0 
for y,x in graph:
    if 1 in (y,x):
        q.append((y,x))
        
while q:
    y,x = q.popleft()
    cnt+=1
    
    for (a,b) in graph:
        if (a,b) in visited:
            continue
        else:
            if graph2[a][b]==1:
                q.append((a,b))
                visited.add((a,b))
                continue

answer = math.ceil(cnt/2)
print(answer)        
