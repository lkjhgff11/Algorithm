from collections import deque
n,k = map(int,input().split())
q = deque()
cnt = 0
q.append((n,k,0))
minn = 10**10

while q:
    x,k,time = q.popleft()
   
    if x == k and cnt == 0:
        minn = time
        cnt += 1 

    if x == k and time == minn :
        cnt +=1
      
    if time > minn:
        print(minn)
        print(cnt-1)
        break

    q.append((x-1,k,time+1))
    q.append((x+1,k,time+1))
    q.append((2*x,k,time+1)) 
         
