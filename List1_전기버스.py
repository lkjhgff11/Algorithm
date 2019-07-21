# drive는 bus에서 0번에서시작해 k번 거리안에 충전하면서 맨 끝까지 갈수 있는 각 횟수 cnt가 담긴 리스트 li를 반환한다.
# 만약에 맨 끝까지 못가면 0을 반환한다.
# k는 충전하면 한번에 갈수있는거리. bus는 버스안의 충전소표시, start에서 출발해서 goal에 도착할때까지 들리는 충전소 갯수 나타내는 li반환
def drive(li,k,bus,start,goal,cnt):
    for i in range(k,0,-1):
        if start+i >= goal:
            li.append(cnt)
            return li
          
        if bus[start+i] == 1:
            start = start+i
            cnt = cnt+1
            drive(li,k,bus,start,goal,cnt)
      
t = int(input())
for test in range(t):
    k,n,m = map(int,input().split())
    bus = list(0 for i in range(n+1))
    bus[0] = 1
    charge = list(map(int,input().split()))
    for i in charge:
        bus[i] = 1

    cnt = 0
    goal = len(bus)-1
    li = []
    drive(li,k,bus,0,goal,cnt)
    if len(li) > 0:
        print("#{} {}".format(test+1,min(li)))
    if len(li) == 0:
        print("#{} {}".format(test+1,0))
   
