t = int(input())
for tt in range(1,t+1):
    string = list(input())
    
    li =[]
    n = len(string)
    for i in range(n):
        if len(li) == 0 or li[-1] != string[i]:
            li.append(string[i])

        elif li[-1] == string[i]:
            li.pop()

    ans = len(li)
    print("#{} {}".format(tt,ans))
