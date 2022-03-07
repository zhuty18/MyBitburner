a = [
    9,
    [
        131, 110, 87, 33, 110, 36, 59, 155, 15, 189, 82, 36, 200, 99, 194, 114, 126, 53, 149, 104, 83, 193, 85, 160, 149, 125,
        155, 196, 145, 152, 111, 80, 116, 151, 60, 154, 157, 124, 38, 89, 39, 149, 28, 90
    ]
]
time = a[0]
b = a[1]
l = len(a[1])
min = []
max = []

for i in range(l - 1):
    if (i == l - 1 or b[i + 1] > b[i]) and (i == 0 or b[i - 1] > b[i]):
        min.append(i)
    if (i == l - 1 or b[i + 1] < b[i]) and (i == 0 or b[i - 1] < b[i]):
        max.append(i)

pot = []
for i in min:
    for j in max:
        if j > i and b[j] > b[i]:
            pot.append([b[j] - b[i], [i, j]])

pot.sort(key=lambda x: x[0], reverse=True)
pick = [0] * (len(pot))

for i in range(1, len(pot)):
    for j in range(i):
        # print(pot[i][1],pot[j][1])
        # break
        # i=1
        # j=0
        # print(pot[i][1],pot[j][1])
        if pot[j][1][0] >= pot[i][1][0] and pot[j][1][1] <= pot[i][1][1]:
            pick[i] = 1
    # print(i)

pot_new = []
for i in range(len(pick)):
    if pick[i] == 0:
        pot_new.append(pot[i])

print(pot_new)
pick = [0] * (len(pot_new))



