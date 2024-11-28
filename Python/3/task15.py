import math
print('Введите угол')
a = float(input())
b = math.floor((a/360) * 12 * 60 * 60)
S = (b % 60) % 60
M = (b // 60) % 60
H = b // 3600
print(H)
print(M)
print(S)