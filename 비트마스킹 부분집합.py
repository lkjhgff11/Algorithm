li = [1,5,8,14]
total = []
for i in range(1<<len(li)):
    print("@",i)
    sub = []
    for j in range(len(li)):
        if i&(1<<j):
            sub.append(li[j])
            print("##",sub)
    total.append(sub)

print(total)
