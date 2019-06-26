x = input()
s = ''.join([bin(int(c))[2:].zfill(3) for c in x])
for i in range(3):
    if s[0] == '0':
        s = s[1:]

print(s)

