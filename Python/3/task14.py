import math
print('Введите часы')
H = int(input())
print('Введите минуты')
M = int(input())
print('Введите секунды')
S = int(input())
print(((H*3600 + M*60 + S)/(12*3600) * 360) % 360)