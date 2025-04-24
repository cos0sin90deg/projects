import numpy as np
A = np.array([[2, 6], [4, 9]])
b = np.array([1, 3])
def find_pseudo_solution(A, b):
    A_T = np.transpose(A)
    A_T_A = np.dot(A_T, A)
    A_T_b = np.dot(A_T, b)
    x_pseudo = np.linalg.solve(A_T_A, A_T_b)
    return x_pseudo
pseudo_solution = find_pseudo_solution(A, b)
print(pseudo_solution)