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
