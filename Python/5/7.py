a = input()
b = a.find('h')
c = len(a) - a[::-1].find('h') - 1
print(a[:b] + a[c+1:])