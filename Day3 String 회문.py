import copy
t = int(input())
for tt in range(1,t+1):
    n,m = map(int,input().split())  # m은 팰린드롬 되는 숫자
    grid = [list(input())for _ in range(n)]

    # grid2는 grid 세로들을 가로들로 바꾼 이차원배열 
    grid2 = copy.deepcopy(grid)
    for i in range(n):
        for j in range(n):
            grid2[i][j] = grid[j][i]

    s1 = []
    s2 = []
    s3 = []
    s4 = []
    for x in range(n):
        for y in range(n):
            if y+m <= n:
                s1 = grid[x][y:y+m]
                s2 = list(reversed(s1))

                s3 = grid2[x][y:y+m]
                s4 = list(reversed(s3))


                if s1 == s2:
                    ans = s1

                if s3 == s4:
                    ans = s3

    print("#{} {}".format(tt,"".join(ans)))
