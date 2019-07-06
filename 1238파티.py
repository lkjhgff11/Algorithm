import sys
from heapq import *

input=sys.stdin.readline
INF=sys.maxsize

n,m,dst=map(int,input().split())  # n명의 학생, m개의 도로, dst 마을 도착지
arr=[[]for _ in range(n)]
longtime=[INF]*n

for _ in range(m):
    start,end,t=map(int,input().split())  # 도로시작, 도로끝,시간
    start-=1
    end-=1
    arr[start].append((end,t))
    

def dijkstra(start,dst):
    pq=[]
    heappush(pq,(0,start)) # 시간,시작집
    longtime[start]=0
    
    while pq:
        time,cur=heappop(pq)
        
        if cur==dst:
            return longtime[dst]

        if longtime[cur]<time:
            continue

        for nxt,nxt_time in arr[cur]:
            nxt_time+=time
            
            if longtime[nxt]>nxt_time:
                longtime[nxt]=nxt_time
                heappush(pq,(nxt_time,nxt))

dis1=[]
dis2=[]
for i in range(n):             
    #print("목적지로 갈때 다익스트라 start 시간가중치 반환",dijkstra(i,dst-1))
    dis1.append(dijkstra(i,dst-1))
    #print(dst-1,longtime[dst-1])
    longtime=[INF]*n

for i in range(n):
    #print("돌아올때 다익스트라 start,시간가중치반환",dijkstra(dst-1,i))
    dis2.append(dijkstra(dst-1,i))
    longtime=[INF]*n

     
hap=[0]*n
for i in range(n):
    hap[i]=dis1[i]+dis2[i]

print(max(hap))    
