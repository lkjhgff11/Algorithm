nan = sorted([int(input()) for _ in range(9)])
for i in range(1<<9):  # 000000000 ~ 11111111 까지 돈다.
    sub = [nan[index] for index in range(9) if 1<<index & i] # 1<<index는 자릿수랑 i(i는 난쟁이가 나오는 모든 경우의 수의 비트)를 비트연산하는데 각 자리수 비트연산결과 0이아니면 거기 자릿수에 해당하는 난쟁이[자릿수]를 집합에다 넣는다.  
    if len(sub) == 7 and sum(sub) == 100:
        print(*sub,sep='\n')
        break
