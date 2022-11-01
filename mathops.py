def modInv(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x


def binAdd(a, b):
    binA = int(a, 2)
    binB = int(b, 2)

    return bin(binA ^ binB)[2:]


def binMult(a, b):
    binB = int(b, 2)

    if a[len(a)-1] == '1':
        c = binB
    elif a[len(a)-1] == '0':
        c = 0

    for i in range(1, len(a)):
        binB = binB<<1

        if a[len(a)-(1+i)] == '1':
            c = c ^ binB

    return bin(c)[2:]


def binSquare(a):
    if a[0] == '1':
        c = 1
    elif a[0] == '0':
        c = 0
    for i in range(1, len(a)-1):
        c = c<<2
        if a[i] == '1':
            c = c^1
    return bin(c)[2:]


def eegcd(a, b):
    u = a
    v = b

    g1 = '1'
    g2 = '0'
    h1 = '0'
    h2 = '1'

    while u != '0':
        j = len(u) - len(v)
        if j < 0:
            u, v = v, u
            g1, g2 = g2, g1
            h1, h2, = h2, h1
            j = -j

        zj = format(1 << j, "08b")
        u = binAdd(u, binMult(zj, v))
        g1 = binAdd(g1, binMult(zj, g2))
        h1 = binAdd(h1, binMult(zj, h2))
    d = v
    g = g2
    h = h2

    return [d, g, h]


def binInv(a, f):
    u = a
    v = f

    g1 = '1'
    g2 = '0'

    while u != '1':
        j = len(u) - len(v)
        if j<0:
            u, v = v, u
            g1, g2 = g2, g1
            j = -j
        zj = format(1 << j, "08b")
        u = binAdd(u, binMult(zj, v))
        g1 = binAdd(g1, binMult(zj, g2))

    return g1


if __name__ == '__main__':
    print(modInv(26, 17))
    print(binAdd("1010011", "11001010"))

    a1 = "1010011"
    print(hex(int(a1, 2)))
    b1 = "11001010"
    print(hex(int(b1, 2)))
    print(binMult(a1, b1))

    print(f"{a1} squared: {binSquare(a1)}")

    d, g, h = eegcd(a1, b1)
    print(f"d = {d}, g = {g}, h = {h}")

    print(f"{binAdd(binMult(a1, g), binMult(b1, h))}")

    binInv()




