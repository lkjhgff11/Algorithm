r,c = map(int,input().split())
grid = [list(map(int,input().split()))for _ in range(r)]

root = [[(-1,-1)]*c for _ in range(r)]

# y,x의 루트를 줭
def rec(y,x):
    if root[y][x] != (-1,-1):
        return root[y][x]

    minn = (10**10,0,0)
    for dy in range(-1,2):
        for dx in range(-1,2):
            ny = y + dy
            nx = x + dx

            if ny in (-1,r) or nx in (-1,c):
                continue
            minn = min(minn,(grid[ny][nx],ny,nx))

   
    minn = minn[1:] 
    if minn == (y,x):
        root[y][x] = (y,x)
        return root[y][x]
     

    else:
        (ny,nx) = minn
        root[y][x] = rec(ny,nx)
        return root[y][x]
    
for y in range(r):
    for x in range(c):
        rec(y,x)

ans = [[0]*c for _ in range(r)]
for y in range(r):
    for x in range(c):
        ans_y,ans_x = root[y][x]
        ans[ans_y][ans_x] += 1
    
for a in ans:
    print(*a)
