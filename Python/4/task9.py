print('Введите n')
N = int(input())
A = 0
for i in range (1, N+1):
    print('Введите целое число')
    B = int(input())
    if B == 0:
        A = A + 1
print(A)