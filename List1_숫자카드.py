t = int(input())
for i in range(t):
    n = int(input())
    cards = list(map(int,input()))
    cnt = [0]*(max(cards)+1)
    for c in cards:
        cnt[c] = cards.count(c)

    maxx = max(cnt)
    index = 0
    for j in range(len(cnt)):
        if cnt[j] == maxx:
            index = j
 
    print("#{} {} {}".format(i+1,index,maxx))
