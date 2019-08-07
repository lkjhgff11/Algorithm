n = int(input())
for case in range(1,n+1):
    a,b = map(int,input().split())
    print("Case #{}: {} + {} = {}".format(case,a,b,a+b))
