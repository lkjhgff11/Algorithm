from collections import deque
n = int(input())
grid = [list(map(int,input().split()))for _ in range(n)]

q = deque()

# 플로이드-워셜 3중 for문 제일바깥 부터 k는 거쳐가는거 s는 시작점, d는 도착  
for k in range(n):
    for s in range(n):
        for d in range(n):
            if grid[s][k] == 1 and grid[k][d] == 1:
                grid[s][d] = 1
                




for g in grid:
    print(*g)
            

