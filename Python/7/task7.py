i = 0
A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
x = int(input())
while (i < len(A)) and (A[i] >= x):
    i = i + 1
print (i+1)