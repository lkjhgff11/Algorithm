'''
 Baby gin게임은 6자리 숫자를 입력받아서
 3개가 같은 숫자면 triple
 3개가 연속된 숫자면 run인데
 6개의 숫자가 run 이나 triple로 2개 구성되면 Baby gin

'''
num = int(input())
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for _ in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triple 조사후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue

    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i+=1
        
if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")    
