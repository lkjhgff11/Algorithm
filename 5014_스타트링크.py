# F: 총 층수, S: 강호가 지금있는층,  G:목적지층, U: 위로U층 D: 아래로D층을 가는버튼
# 만약, 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"
from collections import *
f,s,g,u,d = map(int,input().split())
q=deque([(0,s)])
visited = set()
answer = -1
while q:
    cnt,x=q.popleft()
    if x==g:
        answer = cnt
        break
    
    if x+u<=f and (x+u) not in visited:
        visited.add(x+u)
        q.append((cnt+1,x+u))

    if x-d>0 and (x-d) not in visited:
        visited.add(x-d)
        q.append((cnt+1,x-d))
         
if answer == -1:
    print('use the stairs')
else:
    print(answer)
