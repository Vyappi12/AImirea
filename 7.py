def extract(val, beg, end):
    mask = (1 << (end - beg)) - 1
    return (val >> beg) & mask


def main(n):
    n = int(n, 16)
    n &= ~(1 << 7)
    l1 = extract(n, 0, 7)
    l2 = extract(n, 7, 8)
    l3 = extract(n, 8, 11)
    l4 = extract(n, 11, 17)
    l5 = extract(n, 17, 27)
    l6 = extract(n, 27, 29)
    l_sum = l6 << 27 | l4 << 21 | l2 << 20 | l3 << 17 | l1 << 10 | l5
    return str(l_sum)


# 11101111010101100011110110000

print(main('0x1f617d31'))


## decoder
def main(s):
    i = int(s)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i >> 7)
    c3 = 0b11 & (i >> 17)
    c5 = 0b111111111 & (i >> 27)
    return tuple(map(str, (c1, c2, c3, c5)))

##transcoder
def transcode(v):
    k1 = v & 0xff
    k2 = (v >> 8) & 0x7f
    k3 = (v >> 15) & 0x7
    k4 = (v >> 18) & 0x1
    k3 = (v >> 19) & 0x7
    d = k4 | (k3 << 1) | (k1 << 4) | (k5 << 12) | (k2 << 15)
    return str(d)
