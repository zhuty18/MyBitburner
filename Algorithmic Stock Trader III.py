b = [
    129, 37, 28, 192, 62, 96, 148, 128, 104, 142, 144, 137, 133, 126, 91, 43, 135, 54, 194, 22, 82, 167, 117, 69, 77, 126, 36,
    69, 96, 38, 123, 30, 177, 55, 174, 103, 186, 125, 110, 133, 15, 112, 7, 189, 192, 161, 127, 24, 169, 91
]

l = len(b)
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


print(loop(0, 2, pick, pot_new))