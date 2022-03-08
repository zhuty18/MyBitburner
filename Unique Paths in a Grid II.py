a = [[0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

m = len(a[0])
n = len(a)

res = [0] * (m * n)
for i in range(m):
    for j in range(n):
        if a[j][i] == 1:
            res[i * n + j] = 0
        elif i == 0 and j == 0:
            res[i * n + j] = 1
        elif i == 0:
            res[i * n + j] = res[i * n + j - 1]
        elif j == 0:
            res[i * n + j] = res[(i - 1) * n + j]
        else:
            res[i * n + j] = res[i * n + j - 1] + res[(i - 1) * n + j]
print(res)
print(res[m * n - 1])
