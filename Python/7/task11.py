A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
k = int(input())
for i in range (k, len(A)-1):
    A[k] = A[k+1]
    k = k + 1
    i = i + 1
A = A[0:len(A)-1]
print (A)