t = int(input())
for tt in range(1,t+1):
    string = input().split()
    li = []
    flag = 0

    for s in string:
        if s not in ('+','-','*','/','.'):
            li.append(s)

        elif s == '.':
            break
    
        else:
            try:
                b = int(li.pop())
                a = int(li.pop())

                if s == '+': ins = a + b
                if s == '-': ins = a - b
                if s == '*': ins = a * b 
                if s == '/': ins = a // b     
                li.append(ins)                
            except :
                 flag = 123456789
            
        
    if flag == 0 and len(li) == 1:
        print("#{} {}".format(tt,li[0]))
    
    elif flag == 123456789 or len(li) > 1:
        print("#{} {}".format(tt,"error"))    
