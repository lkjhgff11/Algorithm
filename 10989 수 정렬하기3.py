import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10002

for _ in range(n):
    a = int(input())
    count[a] += 1

for i in range(10002):
    print('%s\n'%i*count[i],end='')
