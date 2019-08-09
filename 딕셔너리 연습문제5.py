fruit = ['   apple    ','banana','  melon']
new_fruit = []
for f in fruit:
    f = f.replace(" ","")
    new_fruit.append(f)

ans = {f:len(f) for f in new_fruit}
print(ans)
