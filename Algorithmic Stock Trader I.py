a = [
    110, 23, 181, 40, 79, 20, 96, 98, 192, 136, 131, 107, 142, 11, 139, 165, 127, 173, 113, 64, 38, 185, 120, 12, 156, 30, 174,
    72, 156, 4, 164, 151, 65, 175, 95, 185, 39, 121, 58, 39, 114, 174, 174, 76, 24, 145
]

l = len(a)
min = []
max = []

for i in range(l - 1):
    if (i == l - 1 or a[i + 1] > a[i]) and (i == 0 or a[i - 1] > a[i]):
        min.append(i)
    if (i == l - 1 or a[i + 1] < a[i]) and (i == 0 or a[i - 1] < a[i]):
        max.append(i)

pot = []
for i in min:
    for j in max:
        if j > i and a[j] > a[i]:
            pot.append([a[j] - a[i], [i, j]])

pot.sort(key=lambda x: x[0], reverse=True)

print(pot[0][0])
