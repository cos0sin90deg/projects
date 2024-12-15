a = input()
i = 0
for i in range (0, len(a)//3 + 1):
    a = a[:3*i] + ' ' + a[3*i + 1:]
print(a.replace(' ', ''))