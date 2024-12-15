a = input()
b = a.find('h')
c = len(a) - a[::-1].find('h') - 1
print(a[:b] + a[c - len(a):b - len(a):-1] + a[c:])