a = [[50, 17, 48, 21, 38, 18, 25, 4, 49, 13, 17, 8, 24], [22, 25, 6, 6, 43, 9, 29, 33, 50, 37, 6, 37, 37],
     [17, 43, 50, 29, 43, 30, 26, 44, 36, 48, 32, 29, 33], [5, 47, 3, 4, 24, 12, 27, 12, 44, 14, 20, 27, 49],
     [2, 44, 12, 28, 8, 8, 48, 48, 41, 37, 31, 44, 18], [23, 24, 17, 31, 48, 37, 10, 44, 26, 9, 34, 3, 30],
     [39, 17, 2, 40, 28, 49, 30, 26, 17, 1, 21, 28, 22], [38, 7, 6, 27, 37, 36, 9, 10, 4, 19, 17, 25, 48]]
height = len(a)
width = len(a[0])
b = []
for i in range(height):
    b.append([0] * width)


def check(b, i, j):
    if (0 <= i and i < len(b[0])) and (0 <= j and j < len(b)):
        return b[j][i] == 0


res = []


def pop(a, b, i, j, dir):
    global res
    res.append(a[j][i])
    b[j][i] = 1
    if dir == 0:
        if check(b, i + 1, j):
            pop(a, b, i + 1, j, dir)
        elif check(b, i, j + 1):
            pop(a, b, i, j + 1, dir)
        elif check(b, i - 1, j):
            pop(a, b, i - 1, j, dir)
        elif check(b, i, j - 1):
            pop(a, b, i, j - 1, 1 - dir)
    else:
        if check(b, i, j - 1):
            pop(a, b, i, j - 1, dir)
        elif check(b, i + 1, j):
            pop(a, b, i + 1, j, 1 - dir)
        elif check(b, i, j + 1):
            pop(a, b, i, j + 1, 1 - dir)
        elif check(b, i - 1, j):
            pop(a, b, i - 1, j, 1 - dir)


pop(a, b, 0, 0, 0)
print(res)