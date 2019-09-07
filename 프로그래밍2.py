input_s = input()
'''
"(()())()"   "(()())()"
")("         "()"
"()))((()"   "()(())()"


'''
def is_right(s):
    stack = 0
    for x in range(len(s)):
        if s[x] == '(':
            stack += 1

        if s[x] == ')':
            stack -= 1

        if stack < 0:
            return False
    return stack == 0            
            
        
    
    

def solution(p):
    if p == '':
        return ''

    v = ""
    u = ""
    l = 0
    for i in range(len(p)):
        x = p[i]
        if x == '(':
            l += 1
            u = u +'('

        if x == ")":
            l -= 1
            u = u + ')'
            
        if l == 0:
            break

    v = p[i+1:]    
        
    if is_right(u):
        return u + solution(v)

    else:
        s = '(' + solution(v) + ')'

        for x in u[1:-1]:
            if x == '(':
                s += ')'
                
            if x == ')':
                s += '('

        
        return s        

        
print(solution(input_s))
        
        
      
                    

                    
                    
        
    
