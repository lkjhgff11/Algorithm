import re
p = re.compile('.*U.*C.*P.*C.*')
ucpc = input()
m = p.match(ucpc)
if m:
    print("I love UCPC")
else:
    print('I hate UCPC')
