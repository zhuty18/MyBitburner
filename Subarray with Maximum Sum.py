a = [-3,-2,7,-6,-4,7,0,-8,-3]

subsum = a[0]
maxsum = a[0]


def max_(a, b):
    if b > a:
        return b
    else:
        return a


for i in range(1, len(a)):
    subsum = max_(a[i], subsum + a[i])
    maxsum = max_(subsum, maxsum)

print(maxsum)
