# 처음에는 모든칸 양분 5
# k년 후 살아있는 나무의 갯수를 구하기
import sys
from collections import deque
input = sys.stdin.readline
n,m,k = map(int,input().split())
nut = [[5 for _ in range(n)] for _ in range(n)] # 처음 양분
tree =[[deque()for _ in range(n)]for _ in range(n)]# 나무의 나이
add_nut = [list(map(int,input().split()))for _ in range(n)] # 추가되는 양분

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

cnt = 0
for _ in range(m):
    x,y,age = map(int,input().split())
    tree[x-1][y-1].append(age)
    cnt += 1

for k in range(k):
    # 봄에 나이먹고 양분 먹고, 여름에 죽은나무(양분보다 나무나이가 많은나무)를 없애고 양분추가  
    for x in range(n):
        for y in range(n):
            for z in range(len(tree[x][y])):
                if nut[x][y] >= tree[x][y][z]:
                    nut[x][y] -= tree[x][y][z]
                    tree[x][y][z] += 1

               
                elif nut[x][y] < tree[x][y][z]:
                    while z < len(tree[x][y]):
                        nut[x][y] += (tree[x][y].pop()//2)
                        cnt -= 1
                    break    

        
   # 가을에 번식, 겨울에 양분추가
    for x in range(n):
        for y in range(n):
            for z in range(len(tree[x][y])):
                if tree[x][y][z] % 5 == 0:
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx in (-1,n) or ny in (-1,n):
                            continue
                        tree[nx][ny].appendleft(1)
                        cnt += 1                      
            nut[x][y] += add_nut[x][y]

                    
print(cnt)              

    
