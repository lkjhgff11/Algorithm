def device(y,x,cnt):
    if y >= n:
        return True
    
    if grid[y][x] == '#':
        return device(y+1,x,cnt)

    elif grid[y][x] == '>':
        return device(y,x+1,cnt)

    elif grid[y][x] == '<':
        return device(y,x-1,cnt)

    elif grid[y][x] == '*':
        if cnt == 0 :
            return device(y+1,x,cnt+1)

        if cnt == 1:
            return False
        

def solution(grid):
    global n 
    n = len(grid)
    start = [(0,i) for i in range(n)]
   
    ans = []
    for y,x in start:
        check = device(y,x,0)
        if check == True:
            ans.append(x)
    return len(ans)

grid = ["######",">#*###","####*#","#<#>>#",">#*#*<","######"]
print(solution(grid))
