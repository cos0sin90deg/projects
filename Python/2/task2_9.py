print('Введите номер столбца первой клетки')
a = int(input())
print('Введите номер строки первой клетки')
b = int(input())
print('Введите номер столбца второй клетки')
c = int(input())
print('Введите номер строки второй клетки')
d = int(input())
if abs (a - c) == abs (b - d):
    print ('YES')
else:
    print ('NO')