i = 0
k = 0
j = 1
A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
while (i < len(A)):
    while j < len(A):
        if (A[j] == A[i]):
            k = k + 1
            break
        j = j + 1
    i = i + 1
    j = i + 1
print (len(A) - k)