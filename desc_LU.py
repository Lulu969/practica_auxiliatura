import numpy as np

A = np.array([[1, 4, 9, 16],
              [4, 9, 16, 25],
              [9, 16, 25, 36],
              [16, 25, 36, 49]], dtype=float)

b = np.array([30, 54, 86, 126], dtype=float)

n = len(A)
L = np.eye(n)
U = A.copy()

for i in range(n):
    for j in range(i + 1, n):
        factor = U[j, i] / U[i, i]
        L[j, i] = factor
        U[j, i:] -= factor * U[i, i:]

y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]


print(" RESULTADO: ", x)
