n=int(input())
p=0
for i in range(n):
    s=input()
    for j in range(3,len(s)):
        for i in range(len(s)-j+1):
            c = s[i:i+j]
            if c == c[::-1]:
                print(c)
 
    
