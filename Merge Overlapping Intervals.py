a = [[20, 24], [4, 8], [16, 26], [2, 6]]
min = -1
max = -1
for i in a:
    if i[0] < min or min == -1:
        min = i[0]
    if i[1] > max or max == -1:
        max = i[1]

b = [0] * (max - min + 1)
for i in a:
    for j in range(i[0], i[1] + 1):
        b[j - min] = 1

last = 0
res = []
head = 0
for i in range(min, max + 1):
    if last == 0 and b[i - min] == 1:
        head = i
    if last == 1 and b[i - min] == 0:
        res.append([head, i - 1])
    last = b[i - min]
res.append([head, max])
print(res)