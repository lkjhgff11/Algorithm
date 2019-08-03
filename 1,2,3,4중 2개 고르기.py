# arr 1,2,3,4..n 중 select개 고르기
def rec(arr,select,index,cur):
    if index == select:
        print(*arr)
        return
    for i in range(cur,n+1):
        if i in arr:
            continue
        arr.append(i)
        rec(arr,select,index+1,i)
        arr.pop()


tmp = []
n = int(input())
select = int(input())
rec([],select,0,1)
