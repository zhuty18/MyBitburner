b = [
    156, 53, 37, 33, 41, 122, 71, 189, 102, 39, 38, 114, 117, 61, 4, 72, 49, 22, 177, 126, 37, 77, 28, 89, 121, 123, 169, 151,
    168, 47, 116, 86, 108, 142, 83, 114, 167, 55, 141, 134, 145, 27
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

# print(pot_new)
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
        return 0
    elif time == 1:
        for i in range(index, len(pot)):
            if pick[i] == 0:
                return pot[i][0]
        return 0
    m = 0
    for i in range(index, len(pot)):
        if pick[i] == 0:
            c = p(i, pick, pot)
            t = loop(i + 1, time - 1, pick, pot)
            t += pot[i][0]
            unp(c, pick)
            if t > m:
                m = t
    return m


print(loop(0, 2, pick, pot_new))