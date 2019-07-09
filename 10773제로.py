k=int(input())
li=[]
for _ in range(k):
    s=int(input())
    if s==0:
        li.pop()

    else:
        li.append(s)

if li:
    print(sum(li))
    
else:
    print(0)
