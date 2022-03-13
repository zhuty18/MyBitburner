a = "6418249141"
l = len(a)
pos = []


def check(s):
    k = int(s)
    return k < 256 and str(k) == s


for i in range(l):
    if l - i >= 1 and check(a[i:i + 1]):
        pos.append([i, i + 1])
    if l - i >= 2 and check(a[i:i + 2]):
        pos.append([i, i + 2])
    if l - i >= 3 and check(a[i:i + 3]):
        pos.append([i, i + 3])

res = []
# print(pos)
for i in range(1, 4):
    if [0, i] in pos:
        for j in range(i + 1, l + 4):
            if [i, j] in pos:
                for k in range(j + 1, j + 4):
                    if [j, k] in pos and [k, l] in pos:
                        res.append(a[0:i] + "." + a[i:j] + "." + a[j:k] + "." + a[k:l])

print("["+", ".join(res)+"]")
