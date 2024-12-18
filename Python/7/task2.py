i = 0
A = input()
A = A.split()
B = []
for i in range (len(A)):
    A[i] = int(A[i])
i = 0
while i < len(A):
    if int(A[i])%2 == 0:
        B.append(A[i])
    i = i + 1
print (B)