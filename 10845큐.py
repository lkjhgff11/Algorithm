from collections import *
n=int(input())
q=deque()
for _ in range(n):
    n = input().split()
    if n[0]=="push":
        q.append(n[1])
        
    if n[0]=="pop":
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)

    if n[0]=="front":
        if q:
            print(q[0])
        else:
            print(-1)
            
    if n[0]=="back":
        if q:
            print(q[-1])
        else:
            print(-1)
        
    if n[0]=="size":
        print(len(q))

    if n[0]=="empty":
        if q:
            print(0)
        else :
            print(1)
