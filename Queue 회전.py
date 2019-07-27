t = int(input())
for tt in range(1,t+1):
    n,m = map(int,input().split())
    li = list(map(int,input().split()))
    for _ in range(m):
        a = li.pop(0)
        li.append(a)
    ans = li[0]
    print("#{} {}".format(tt,ans))
