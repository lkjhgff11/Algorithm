import sys
input = sys.stdin.readline

n=int(input())
A=[]
B=[]
C=[]
D=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

cnt=0

E=[a+b for a in A for b in B]
F=[c+d for c in C for d in D]

E.sort()
F.sort()

def bS(target,left,right):
    mid=(left+right)//2
    if F[mid]==target:
        return mid

    if right<left:
        return -1

    if F[mid]<target:
        return bS(target,mid+1,right)

    if F[mid]>target:
        return bS(target,left,mid-1)
    
cnt=0
for e in E:
    target=-e
    result=bS(target,0,n*n-1)
    if result != -1 :
        cnt += 1 
print(cnt)                                 
