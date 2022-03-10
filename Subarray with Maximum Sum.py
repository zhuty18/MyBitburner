a = [-9,-3,9,8,-5,-7,0,4,3,4,8,-1,-1,-10,-2,-1,-2,-8,3,-3,-4,9,-5,10]

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
