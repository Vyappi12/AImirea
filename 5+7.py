import math


def main(y, z):
    sum = 0
    n = len(y)
    y = [0] + y
    z = [0] + z
    for i in range(1, n + 1):
        a = (y[n + 1 - i] ** 3)
        b = (-18 * z[n + 1 - math.ceil(i / 2)] - 71)
        sum += 96 * (a + b) ** 2
    return 86 * sum
def main(s):
    i = int(s)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i >> 7)
    c3 = 0b11 & (i >> 17)
    c5 = 0b111111111 & (i >> 27)
    return tuple(map(str, (c1, c2, c3, c5)))
def main(s):
    s = int(s)
    s = str(format(s, 'b'))
    for num in s:
        if len(s) < 28:
            cout0 = 28 - len(s)
            for i in range(0, cout0):
                s = '0' + s
    s = s[12:17] + s[24:28] + s[3:12] + s[17:24] + s[0:3]
    return str(int(s, 2))