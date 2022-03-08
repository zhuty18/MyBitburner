a = [8,176,126,18,137,75,146,103,13,125,97,56,87,31,168,71,146,104,136,61,200]
l = len(a)

pro = 0
buy = 0
for i in range(l - 1):
    if a[i + 1] > a[i] and buy == 0:
        buy = a[i]
    if a[i + 1] < a[i] and buy != 0:
        pro += a[i] - buy
        buy = 0
if (buy != 0):
    pro += a[l - 1] - buy
print(pro)
