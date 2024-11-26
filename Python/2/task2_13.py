print('Введите N')
N = int(input())
print('Введите M')
M = int(input())
print('Введите x')
x = int(input())
print ('Введите y')
y = int(input())
if N > M:
    b = N
    a = M
else:
    b = M
    a = N
if a - x > x:
    a = x
else:
    a = a - x
if b - y > y:
    b = y
else:
    b = b - y
if a > b:
    print (b)
else:
    print (a)