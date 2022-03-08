a = [2,7,10,3,0,4,0,5,7,3,0,4,7,5,0,10,7]
l = len(a)
b = [0] * l
b[l - 1] = 1

for i in range(l - 2, -1, -1):
    for j in range(a[i] + 1):
        if i + j < l:
            b[i] = b[i] | b[i + j]

print(b[0])
