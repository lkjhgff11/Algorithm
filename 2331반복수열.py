import sys
input = sys.stdin.readline
a,p = input().split()

def dfs(start,arr,):
    #print(arr)
    for s in arr:             
        if arr.count(s) == 3:
            return arr
        
    summ = 0
    for i in start:
       summ += int(i)**int(p)
       
    arr.append(str(summ))
    dfs(str(summ),arr)

arr = []
arr.append(a)
dfs(a,arr)
for i in arr:
    if arr.count(i) >= 2:
        ix = arr.index(i)
        del arr[ix:]
print(len(arr))        
        
