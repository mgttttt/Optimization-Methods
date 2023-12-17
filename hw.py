import numpy as np

A = np.array([[2, -1], [1, -1], [0, 1]])
b = np.array([1, 0, 1])

At = A.T
AtA = np.dot(At, A)
Atb = np.dot(At, b)

x = np.linalg.solve(AtA, Atb)
print("Обобщённое решение СЛАУ:")
print(x)
