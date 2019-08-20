# 0: 빨강, 1: 초록, 2:파랑
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

def get_dp(n,c):
    
    if n == 0:
        return grid[n][c]

    if dp[n][c] != -1:
        return dp[n][c]
    
    color = [0,1,2]
    color.remove(c)
    a = color[0]
    b = color[1]
    dp[n][c] = min(get_dp(n-1,a), get_dp(n-1,b)) + grid[n][c]
    return dp[n][c]
    

print(min(get_dp(n-1,i) for i in range(3)))
