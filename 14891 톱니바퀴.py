# N극:0 , S극:1
# 1: 시계방향, -1: 반시계방향
# 바퀴1번 1이면 1점,바퀴2번 1이면 2점, 바퀴3번 1이면 4점, 바퀴4번 1이면 8
# 배열 인덱스 0번은 12시방향, 톱니바퀴 돌지 판단하는건 배열인덱스 2번,6번

from pprint import pprint

def gear(num,spin_dir,visited):
    target = wheel[num]
    visited.append(num)
    if spin_dir == 1: # 시계방향 오른쪽으로 1칸씩이동

        if num == 0 and num+1 not in visited: # 1번 톱니바퀴는 주변바퀴 2번(오른쪽)이랑만 비교.
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,-1,visited)                

        if num == 1 and num+1 not in visited: # 2번(오른쪽)이랑 3번(왼쪽) 비교
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,-1,visited)

        if num == 1 and num-1 not in visited: # 2번(왼쪽)이랑 1번  비교
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,-1,visited)

        if num == 2 and num+1 not in visited: # 3번(오른쪽)이랑 4번(왼쪽) 비교
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,-1,visited)

        if num == 2 and num-1 not in visited: # 3번(왼쪽)이랑 2번(오른쪽) 비교
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,-1,visited)


        if num == 3 and num-1 not in visited:  # 4번 톱니바퀴는 주변바퀴 3번(왼쪽)이랑만 비교.
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,-1,visited)
            


        # 해당 톱니바퀴 돌리기
        l = len(target)
        tmp = target[l-1]
        for i in range(l-1,0,-1):
            target[i] = target[i-1]
        target[0] = tmp
        check = True
            
            

    # spin_dir이 -1일때 (반 시계방향, 왼쪽으로 1칸씩 이동) 
    else:
        
        if num == 0 and num+1 not in visited: # 1번 톱니바퀴는 주변바퀴 2번(오른쪽)이랑만 비교.
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,1,visited)                

        if num == 1 and num+1 not in visited: # 2번(오른쪽)이랑 3번(왼쪽) 비교
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,1,visited)

        if num == 1 and num-1 not in visited: # 2번(왼쪽)이랑 1번  비교
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,1,visited)

        if num == 2 and num+1 not in visited: # 3번(오른쪽)이랑 4번(왼쪽) 비교
            target_up = wheel[num+1]
            if target[2] != target_up[6]:
                gear(num+1,1,visited)

        if num == 2 and num-1 not in visited: # 3번(왼쪽)이랑 2번(오른쪽) 비교
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,1,visited)


        if num == 3 and num-1 not in visited:  # 4번 톱니바퀴는 주변바퀴 3번(왼쪽)이랑만 비교.
            target_down = wheel[num-1]
            if target[6] != target_down[2]:
                gear(num-1,1,visited)

        # 해당 톱니바퀴 돌리기
        l = len(target)
        tmp = target[0]

        for i in range(l-1):
            target[i] = target[i+1]
        target[l-1] = tmp    
        check = True


wheel = []
for _ in range(4):
    w = list(input())
    wheel.append(w)
             
cnt = int(input())

for _ in range(cnt):
    wheel_num, spin_dir = map(int,input().split())
   # print("num,dir====================================",wheel_num,spin_dir)
    gear(wheel_num-1, spin_dir,[])
   # pprint(wheel)


ans = 0
if wheel[0][0] == '1':
    ans += 1

if wheel[1][0] == '1':
    ans += 2

if wheel[2][0] == '1':
    ans += 4
    
if wheel[3][0] == '1':
    ans += 8

print(ans)    
    
