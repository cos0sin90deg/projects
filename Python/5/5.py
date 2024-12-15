a = input()
b = a.find('f')
c = a[::-1].find('f')
if b == len(a) - 1 - c:
    print(b)
else:
    print(b)
    print(len(a) - 1 - c)