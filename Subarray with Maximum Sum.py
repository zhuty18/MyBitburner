a = [-5,0,2,8,-2,7,-3,-8,-5,-7,-3,-4,-2,-10,0,6,-10,-1,6,-6,-1,-1,-4,-1,-1,-3,4,-10,-4,-5,10,-5,9,4,-10]

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
