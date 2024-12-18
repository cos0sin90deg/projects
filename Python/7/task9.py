i = 0
k = 0
A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
while (i < len(A) - (len(A))%2):
    m = A[i]
    A[i] = A[i+1]
    A[i+1] = m
    i = i + 2
print (A)