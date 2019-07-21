t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    ans = max(li) - min(li)
    print("#{} {}".format(i+1,ans))
