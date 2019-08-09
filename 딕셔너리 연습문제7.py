import string
digit = "0123456789"
letter = string.ascii_letters
string = input()
l = 0
d = 0
for i in string:
    if i in letter:
        l += 1

    if i in digit:
        d += 1


print("LETTERS {}".format(l))
print("DIGITS {}".format(d))
