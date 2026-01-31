def modInv(a, m):
    return pow(a, -1, m)


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
    for i in range(1, len(a)):
        c = c<<2
        if a[i] == '1':
            c = c^1
    return bin(c)[2:]


def binInv(a, f):
    u = a
    v = f

    g1 = '1'
    g2 = '0'

    while u != '1':
        j = len(u) - len(v)
        if j < 0:
            u, v = v, u
            g1, g2 = g2, g1
            j = -j
        zj = format(1 << j, "08b")
        u = binAdd(u, binMult(zj, v))
        g1 = binAdd(g1, binMult(zj, g2))

    return g1


def binReduc(c, fz, m):
    # print(f"Reducing: {c}...")
    intC = int(c, 2)
    intFz = int(fz, 2)

    for i in range(len(c)-1, m-1, -1):
        if (intC & (1<<i))>>i == 1:
            k = i-m
            intC = intC ^ (intFz<<k)

    return bin(intC)[2:]

def binGcd(a, b):
    assert a != "0" and b != "0"
    assert len(b) > len(a)

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
            h1, h2 = h2, h1
            j = -j

        zj = format(1 << j, "08b")
        u = binAdd(u, binMult(zj, v))
        g1 = binAdd(g1, binMult(zj, g2))
        h1 = binAdd(h1, binMult(zj, h2))

