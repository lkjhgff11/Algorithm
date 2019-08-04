def combinations(arr, cnt):
    yield from _combinations(arr, cnt, -1, [])

# arr중에 cnt개 고르기
def _combinations(arr, cnt, index, selected):
    if len(selected) == cnt:
        yield tuple(selected)
        return

    for i in range(index+1, len(arr)):
        selected.append(arr[i])
        yield from _combinations(arr, cnt, i, selected)
        selected.pop()


n = int(input())
board = [list(map(int,input().split()))for i in range(n)]
m = n//2
arr = [i for i in range(1,n+1)]


minn = 10**10
mans = set(range(1,n+1))
for team_a in combinations(arr, m): # start팀과 link팀 나누기
    team_b = list(mans - set(team_a)) # start팀 아닌거는 link팀

    sum_a = sum(board[x-1][y-1] + board[y-1][x-1] for x,y in combinations(team_a, 2))
    sum_b = sum(board[x-1][y-1] + board[y-1][x-1] for x,y in combinations(team_b, 2))

    minn = min(minn, abs(sum_a-sum_b))
print(minn)
    
