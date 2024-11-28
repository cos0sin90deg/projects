import math
print('Введите P')
P = int(input())
print('Введите X')
X = int(input())
print('Введите Y')
Y = int(input())
S = X*100 + Y
S1 = S * (1+(P/100))
print(S1 // 100)
print(S1 % 100)