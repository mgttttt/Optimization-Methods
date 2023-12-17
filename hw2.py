A = [[2, -1], [1, -1], [0, 1]]
b = [1, 0, 1]

At = [list(i) for i in zip(*A)]
AtA = [[sum(a * b for a, b in zip(At_row, A_col)) for A_col in zip(*A)] for At_row in At]
Atb = [sum(a * b for a, b in zip(At_row, b)) for At_row in At]

extended_matrix = [row + [b_elem] for row, b_elem in zip(AtA, Atb)]
n = len(Atb)
for i in range(n):
    max_row = max(range(i, n), key=lambda r: abs(extended_matrix[r][i]))
    extended_matrix[i], extended_matrix[max_row] = extended_matrix[max_row], extended_matrix[i]
    pivot = extended_matrix[i][i]
    for j in range(i, n + 1):
        extended_matrix[i][j] /= pivot
    for k in range(i + 1, n):
        factor = extended_matrix[k][i]
        for j in range(i, n + 1):
            extended_matrix[k][j] -= factor * extended_matrix[i][j]

x = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
    x[i] = extended_matrix[i][n]
    for j in range(i + 1, n):
        x[i] -= extended_matrix[i][j] * x[j]
print("Обобщённое решение СЛАУ:")
print(x)
