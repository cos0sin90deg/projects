print('Введите n')
N = int(input())
A = 1
B = 0
for i in range (1, N+1):
    A = A*i
    B = B + A
print(B)