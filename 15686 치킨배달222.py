# 치킨집은 최대 m 개 까지만됨. m개 이상이면 초과되는부분만큼 폐점시키기
# 0은 빈칸, 1은 집, 2는 치킨집
# 집들이 치킨집 까지 가는 치킨거리 합의 최소 구하기.
import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(n)]

homes = [(y,x) for y in range(n) for x in range(n) if grid[y][x] == 1]
chicks = [(y,x) for y in range(n) for x in range(n) if grid[y][x] == 2]

minn = 10 **10
# 조합을 바로 for문돌려서 그때그때 돈다.(만약 cs = list(combinations(chicks,m)) 이런식으로 list로 만들면 공간낭비)
# cs는 m개의 치킨집
for cs in combinations(chicks,m):
    summ = 0
    for hy,hx in homes:
        summ += min(abs(hy-cy) + abs(hx-cx) for cy,cx in cs)  # 각 집에서 가장 가까운 치킨집과의 거리를 구한걸 다 더한다.
    minn = min(minn,summ)  # 각 집에서 가장 가까운 치킨집과의 거리 합한것들중 최소를 구한다.(고른 치킨집에따라 가까운 거리합이 달라짐으로 그중 작은거 고른다)
print(minn)
