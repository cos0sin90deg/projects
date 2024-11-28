import math
print('Введите натуральное число')
h = int(input())
print(((h % 10) + (h // 10) % 10 + (h // 100)))