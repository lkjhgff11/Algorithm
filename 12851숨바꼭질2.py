from collections import deque
n,k = map(int,input().split())
q = deque()
cnt = 0
q.append((0,n))
MAX = 500005
minn = 10**10
visited = [0]*MAX

while q:
  
    time,x = q.popleft()

    if x == k and cnt == 0:
        minn = time
  
    if x == k and time == minn :
        cnt +=1

    if time > minn:
        print(minn)
        print(cnt)
        break


    for nx in (x-1,x+1,2*x):
        if nx < -1 or nx > 200000:
            continue

        if not visited[nx] or visited[nx] == visited[x]+1:
            q.append((time+1,nx))
            visited[nx] = visited[x]+1
    
