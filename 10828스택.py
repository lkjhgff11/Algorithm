n=int(input())
li=[]
stack=[]
for i in range(n):
    s=input()
    
    if s[:5]=="empty":
        if stack:
            print(0)
        else:
            print(1)

    if s[:4]=="push":
        stack.append(s[5:])

    if s[:4]=="size":
        print(len(stack))
        
    if s[:3]=="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    if s[:3]=="pop":
        if stack:
            p=stack.pop()
            print(p)
            
        else:
            print(-1)
        

