import sys 
from heapq import heappush,heappop # 이렇게 안하면 heapq.heappush(),heapq.heappop() 이런식으로 push나 pop앞에 heapq를 붙여야 된다
input = sys.stdin.readline  # 빠른 입출력
print = sys.stdout.write
INF = sys.maxsize

# 입력받기
n,e=map(int,input().split()) # n은 정점의 갯수, e는 간선의 개수
k=int(input())-1        # k는 시작점
dist = [INF]*n    # 거리는 처음에 무한대로 초기
a= [[] for _ in range(n)]  # a는 도착하는 정점, 가중치 담는다

for _ in range(e):
    u,v,w=map(int,input().split()) # u에서 v로가는 가중치w를 각각 입력받음
    a[u-1].append([w,v-1])  # 인덱스 u-1에서 v-1로가는 가중치

# 다익스트라 알고리즘
# 우선순위큐는 정점번호, 해당정점까지의 거리를 쌍으로 넣는다.
def dijkstra():
    pq = []         # 우선순위 큐
    heappush(pq,(0,k))  # 가중치,시작정점
    dist[k]=0  # 처음 시작정점은 자기 자신이므로 0
    
    while pq:    
        weight,cur = heappop(pq)  # 가중치,현재정점 뽑기
        if dist[cur] < weight:  
            continue

        # 더 짧은 경로 발견하면, dist[]갱신하고 우선순위 큐에다 넣는다.
        for nxt_weight,nxt in a[cur]:   
            nxt_weight += weight   

            if dist[nxt] > nxt_weight:
                dist[nxt] = nxt_weight
                heappush(pq,(nxt_weight,nxt))

dijkstra()

for i in range(n):

    if dist[i] != INF:
        print("%d\n" %dist[i])
    else:
        print("INF\n")
    #print("%d\n" % dist[i] if dist[i] != INF else "INF\n")
    



