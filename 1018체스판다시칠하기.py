from pprint import pprint

n,m=map(int,input().split())
grid=[list(input())for _ in range(n)]
ans=999

white = [['WB'[((x+y)%2)] for y in range(8)] for x in range(8)]
black = [['BW'[((x+y)%2)] for y in range(8)] for x in range(8)]

def wh(y,x):
    cnt=0
    for i in range(y,y+8):
        for j in range(x,x+8):
            if white[i-y][j-x] != grid[i][j]:
                cnt+=1
    return cnt

def bl(y,x):
    cnt=0
    for i in range(y,y+8):
        for j in range(x,x+8):
            if black[i-y][j-x] != grid[i][j]:
                cnt+=1
    return cnt


for i in range(n-7):
    for j in range(m-7):
        ans=min(ans,wh(i,j),bl(i,j))
        
print(ans)        
