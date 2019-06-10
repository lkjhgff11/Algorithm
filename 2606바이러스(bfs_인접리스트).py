from collections import * 
com=int(input()) 
n=int(input()) 
graph=['@']+[[]for _ in range(com)] 
 
for _ in range(n): 
    y,x=map(int,input().split()) 
 
    graph[y].append(x) 
    graph[x].append(y) 
     
q=deque() 
q.append(graph[1]) 
 
visited=[] 
adj=[] 
while q: 
    adj=q.popleft() 
 
    for i in adj: 
        if i in visited: 
            continue 
        visited.append(i) 
        q.append(graph[i]) 

print(len(visited)-1)
