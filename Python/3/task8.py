import math
print('Введите часы первого момента')
a = int(input())
print('Введите минуты первого момента')
b = int(input())
print('Введите секунды первого момента')
c = int(input())
print('Введите часы второго момента')
a1 = int(input())
print('Введите минуты второго момента')
b1 = int(input())
print('Введите секунды второго момента')
c1 = int(input())
d = (a1 - a)*3600 + (b1 - b)*60 + c1 - c
print(d)