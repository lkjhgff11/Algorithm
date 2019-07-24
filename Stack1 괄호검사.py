t = int(input())
for tt in range(1,t+1):
    string = input()
    stack = []
    ans = 1
    for s in string:
        if s == '{' or s == '(':
            stack.append(s)

        if s == '}':
            if len(stack) == 0:
                ans = 0
            else:    
                s2 = stack.pop()
                if s2 != '{':
                    ans = 0
                
        if s == ')':
            if len(stack) == 0:
                ans = 0
            else:
                s2 = stack.pop()
                if s2 != '(':
                    ans = 0

    if len(stack) > 0:
        ans = 0
   
    print("#{} {}".format(tt,ans))
