a = [
    2,
    [
        88, 23, 40, 45, 132, 121, 26, 44, 117, 141, 22, 102, 160, 172, 177, 70, 18, 152, 173, 64, 99, 95, 80, 175, 149, 119, 78,
        146, 116, 41, 103, 21, 136
    ]
]

time = a[0]
b = a[1]


def pot(b):
    min = []
    max = []
    l = len(b)
    for i in range(l - 1):
        if (i == l - 1 or b[i + 1] >= b[i]) and (i == 0 or b[i - 1] >= b[i]):
            min.append(i)
        if (i == l - 1 or b[i + 1] <= b[i]) and (i == 0 or b[i - 1] <= b[i]):
            max.append(i)
    if b[-1] >= b[-2]:
        max.append(l - 1)

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
    return pot_new, [0] * (len(pot_new))


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


if __name__ == "__main__":
    pot_new, pick = pot(b)
    print(loop(0, time, pick, pot_new)[0])
