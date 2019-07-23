t = int(input())
for tt in range(1,t+1):
    str1 = input()
    str2 = input()

    s1 = {}
    s2 = {}
    for i in str1:
        if i in s1:
            s1[i] +=1
        s1[i] = 0

    s2 = s1
    for j in str2:
        if j in s2:
            s2[j] +=1
             
    ans = max(s2.values())

    print("#{} {}".format(tt,ans))
