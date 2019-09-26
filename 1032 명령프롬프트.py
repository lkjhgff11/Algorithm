n = int(input())
arr = []
for _ in range(n):
    st = input()
    arr.append(st)

arr_cnt = len(arr)
nums = len(arr[0])

ans = []
for i in range(nums):
    s = arr[0][i]
    ss = True
    for j in range(1,arr_cnt):
        if s == arr[j][i] and ss == True:
            ss = True
        else:
            ss = False
    if ss == True:
        ans.append(s)

    else :
        ans.append('?')

print(*ans,sep='')
