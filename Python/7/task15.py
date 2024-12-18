A = input()
A = A.split()
for i in range (len(A)):
    A[i] = int(A[i])
    i = i + 1
N = A[0]
K = A[1]
C = ["I"]*N
i = 0
while i < K:
    B = input()
    B = B.split()
    li = int(B[0]) - 1
    ri = int(B[1]) - 1
    j = li
    while li <= j and j <= ri:
        C[j] = "."
        j = j + 1
    i = i + 1
i = 0
for i in (0, len(C)):
    print(C[i], end = "")