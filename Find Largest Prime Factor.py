from math import sqrt

a = 495449310


def check(x):
    for i in range(2, (int(sqrt(x)) + 1)):
        if x % i == 0:
            return check(x // i)
    return x


print(check(a))