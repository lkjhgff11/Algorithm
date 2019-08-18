from pprint import pprint
n = int(input())
INF = 10**10
grid = [[INF]*(n+1)for _ in range(n+1)]

while True:
    a,b = map(int,input().split())
    if (a,b) == (-1,-1):
        break
    grid[a][b] = 1
    grid[b][a] = 1
    
    

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if grid[i][j] > grid[i][k] + grid[k][j]:
                grid[i][j] = grid[i][k] + grid[k][j]
        
    
candidate = [INF]+[0]*n
for c1 in range(1,n+1):
    for c2 in range(1,n+1):
        if c1 == c2:
            continue

        if grid[c1][c2] > candidate[c1]:
            candidate[c1] = grid[c1][c2]
            

ans_minn = min(candidate)
ans_candi = []
for c in range(len(candidate)):
    if candidate[c] == ans_minn:
        ans_candi.append(c)


cnt = len(ans_candi)
ans_candi.sort()

print(ans_minn,cnt)
print(*ans_candi)
    
    
