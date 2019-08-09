string= input()
init = {s:0 for s in string}
for s in string:
    if s in init:
        init[s] += 1

for (key,value) in init.items():
    print(key,end=',')
    print(value)


