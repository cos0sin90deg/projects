print('Введите номер столбца первой клетки')
a = int(input())
print('Введите номер строки первой клетки')
b = int(input())
print('Введите номер столбца второй клетки')
c = int(input())
print('Введите номер строки второй клетки')
d = int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print ('YES')
else:
    print ('NO')