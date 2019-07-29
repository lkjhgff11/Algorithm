# 메모이제이션을 이용한 피보나치수열
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0,1]
n = int(input())
print(fibo(n))
