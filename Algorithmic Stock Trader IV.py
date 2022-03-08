a = [
    3,
    [
        100, 19, 155, 197, 132, 179, 70, 176, 153, 74, 33, 125, 184, 192, 24, 149, 9, 186, 53, 10, 170, 155, 94, 23, 89, 138,
        136, 131, 145, 117, 107, 58, 163, 96, 136, 12, 105, 97, 133, 129, 181, 172, 4
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

pot: list[int, list[int, int]] = []
for i in min:
    for j in max:
        if j > i and b[j] > b[i]:
            pot.append([b[j] - b[i], [i, j]])

pot.sort(key=lambda x: x[0], reverse=True)
pick = [0] * (len(pot))

for i in range(1, len(pot)):
    for j in range(i):
        if pot[j][1][0] >= pot[i][1][0] and pot[j][1][1] <= pot[i][1][1]:
            pick[i] = 1

pot_new = []
for i in range(len(pick)):
    if pick[i] == 0:
        pot_new.append(pot[i])

print(pot_new)
pick = [0] * (len(pot_new))


def p(i, pick, pot):
    res = [i]
    pick[i] = 1
    for j in range(i + 1, len(pot)):
        if (not pot[i][1][0] > pot[j][1][1]) and (not pot[j][1][0] > pot[i][1][1]):
            pick[j] = 1
            res.append(j)
    return res


def unp(l, pick):
    for i in l:
        pick[i] = 0


def loop(index, time, pick, pot):
    if index == len(pot):
        return 0, []
    elif time == 1:
        for i in range(index, len(pot)):
            if pick[i] == 0:
                return pot[i][0], [pot[i]]
        return 0, []
    m = 0
    h = []
    for i in range(index, len(pot)):
        if pick[i] == 0:
            c = p(i, pick, pot)
            t, l = loop(i + 1, time - 1, pick, pot)
            t += pot[i][0]
            unp(c, pick)
            if t > m:
                m = t
                h = [pot[i]]
                h.extend(l)
    return m, h


print(loop(0, time, pick, pot_new))
