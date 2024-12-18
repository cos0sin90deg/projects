A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
i = 0
j = input()
j = j.split()
k = int(j[0])
C = int(j[1])
A.append(C)
i = len(A) - 1
while i > k:
    A[i] = A[i-1]
    i = i - 1
A[k] = C
print (A)