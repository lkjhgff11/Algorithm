n = int(input())
li = []
for i in range(n):
    age,name = input().split()
    li.append((int(age),name,i))

li2 = sorted(li,key = lambda li: (li[0],li[2]))
for (age,name,i) in li2:
    print(age,name)
