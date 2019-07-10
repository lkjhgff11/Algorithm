from itertools import *
li=[]
for _ in range(9):
    x=input()
    li.append(x)


li2 = list(combinations(li,7))

for i in li2:
    if sum(map(int,i))==100:
        for x in i:
            print(x)
