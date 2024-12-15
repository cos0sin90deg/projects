a = input()
b = a.find('f')
c = a.find('f', b+1)
if b == -1:
    print(-2)
else:
    print(c)