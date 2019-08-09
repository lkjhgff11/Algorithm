import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase

st = input()
l = 0
u = 0

for s in st:
    if s in lower:
        l += 1

    if s in upper:
        u += 1

print("UPPER CASE",u)
print("LOWER CASE", l)
