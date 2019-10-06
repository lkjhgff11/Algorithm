k = 2
#score = [24,22,20,10,5,3,2,1]
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
diff = {}
cnt = {}
for i in range(1,len(score)):
    d = score[i-1] - score[i]
    if d not in diff:
        cnt[d] = 0
        diff[d] = set()
    cnt[d] += 1
    diff[d].add(i-1)
    diff[d].add(i)

remove = set()
for key in cnt:
    if cnt[key] >= k:
        for index in diff[key]:
            remove.add(index)

print(len(score) - len(remove))
  
print(score)

