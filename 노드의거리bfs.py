from collections import deque
t = int(input())
for case in range(1,t+1):
    v,e = map(int,input().split())
    graph = [[]for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]

    for _ in range(e):
        s,g = map(int,input().split())
        graph[s].append(g)
        graph[g].append(s)
        
    start,end = map(int,input().split())

    q = deque()
    q.append((start,0))
    while q:
        cur,cnt = q.popleft()
        visited[cur] = 1  
        if cur == end:
            break
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append((nxt,cnt+1))
        cnt = 0          
    
    print("#{} {}".format(case,cnt))
