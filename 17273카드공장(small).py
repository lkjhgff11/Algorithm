front=[]
back=[]
n,m=map(int,input().split()) 
for _ in range(n):
    a,b=map(int,input().split())
    front.append(a)
    back.append(b)

hap=front+back
k=list(int(input())for _ in range(m))

temp=0
for i in k:
    for j in range(n):
        if hap[j]<=i:
            temp=hap[j]
            hap[j]=hap[j+n]
            hap[j+n]=temp

ans=0
for r in range(n):
    ans+=hap[r]
print(ans)    

    
