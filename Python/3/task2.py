import math
print('Введите скорость v')
v = float(input())
print('Введите время t')
t = int(input())
print('Вася остановится на отметке ', math.floor(v*t % 109))