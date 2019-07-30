n,k = map(int,input().split())
nums = [True for i in range(n+1)]


def solve():
    cnt = 0
    for i in range(2, n+1):
        if nums[i] == False:
            continue

        for rm in range(i, n+1, i):
            if nums[rm] == False:
                continue
            cnt += 1
            if cnt == k:
                print(rm)
                return
            nums[rm] = False
solve()
