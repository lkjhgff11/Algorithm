l,c=map(int,input().split())
s=list(input().split())
s.sort()

def rec(s2,index,cur):
    if index==l:
        if 'a'or 'e' or 'i' or 'o' or 'u'in s2:
            print(*s2)
            return

    for i in range(cur,l):
        if i in s2:
            continue
        s2.append(i)
        rec(s2,index+1,i)
        s2.pop()
       

print(rec([],0,0))
