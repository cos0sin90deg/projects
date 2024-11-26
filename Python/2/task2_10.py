print('Введите номер столбца первой клетки')
a = int(input())
print('Введите номер строки первой клетки')
b = int(input())
print('Введите номер столбца второй клетки')
c = int(input())
print('Введите номер строки второй клетки')
d = int(input())
if (-2 <= a - c <= 2) and (-2 <= b - d <= 2) and (abs (a - c) + abs (b - d)) == 3:
    print ('YES')
else:
    print ('NO')