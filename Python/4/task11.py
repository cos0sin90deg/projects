print('Введите n')
N = int(input())
A = 0
for j in range (1, N+1):
    A = A + j
C = A
for i in range (1, N):
    B = int(input())
    
    C = C - B
print(C)