i = 0
A = input()
A = A.split()
B = []
for i in range (len(A)):
    A[i] = int(A[i])
i = 0
while i < len(A):
    if A[i] > A[i-1]:
        B.append(A[i])
    i = i + 1
print (B)