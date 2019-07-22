# start: 시작쪽수, total: 전체 쪽수, goal: 찾기를 원하는 쪽수,cnt: 원하는 쪽수를 몇번만에 찾았는지 
def bSearch(start,total,goal,cnt):
    if start > total:
        return
    mid = (start+total)//2
    cnt += 1
    if mid == goal:
        return cnt

    elif goal > mid:
        return bSearch(mid,total,goal,cnt)

    elif goal < mid:
        return bSearch(start,mid,goal,cnt)


t = int(input())
for tt in range(1,t+1):
    p,pa,pb = map(int,input().split())

    pa_cnt = bSearch(1,p,pa,0)
    pb_cnt = bSearch(1,p,pb,0)

    if pa_cnt < pb_cnt:
        ans = "A"

    elif pb_cnt < pa_cnt:
        ans = "B"

    elif pa_cnt == pb_cnt:
        ans = 0

    print("#{} {}".format(tt,ans))    
