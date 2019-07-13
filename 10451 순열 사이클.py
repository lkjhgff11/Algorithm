t = int(input())

def dfs(v,cnt):
    if visited[v] == 1:
        cnt=cnt+1
        return cnt
    visited[v]= 1
    dfs(arr[v],cnt)


for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    visited=[0]*n
    for i in range(len(arr)):
        arr[i]-=1
    li=[]    
    for i in range(n):
        if visited[i] == 0:
            dfs(i,0)
            li.append(1)

    print(sum(li))
    '''
    arr = list(map(int,input().split()))
    l = list(i for i in range(1,len(arr)+1))
    graph = []
    for i in range(len(arr)):
        graph.append((l[i],arr[i]))
    '''
