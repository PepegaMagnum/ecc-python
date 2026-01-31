import random
import time

from binaryFieldCurve import BinaryFieldCurve
from Point import Point
from RhoPollard import pollardRho

def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:]

def bin_to_hex(bin_string):
    return hex(int(bin_string, 2))

def main():
    # m = 32
    # f = bin((1<<m)+int("10001101",2))[2:]
    # my_curve = BinaryFieldCurve(m, bin(int("b46574af",16))[2:], bin(int("f6c71ed1",16))[2:], f)
    # n = int("ffff1eaa",16)
    # print(n)

    n = 65920
    m = 16
    f = bin((1<<m) + int("101011",2))[2:]

    print(f)

    my_curve = BinaryFieldCurve(m, hex_to_bin("2905"), hex_to_bin("886f"), f)

    generator = Point(hex_to_bin("ba04"), hex_to_bin("9b3b"))

    assert my_curve.doesPointBelongToCurve(generator) == True

    # generate a point
    k = random.randint(2, n-2)
    print(f"")
    Q = my_curve.pointMult(generator, k)
    assert my_curve.doesPointBelongToCurve(Q) == True


    for i in range(1000):
        x = pollardRho(my_curve, generator, Q, n)
        print(f"x: {x}")
        print(f"k: {k}")

        if x is not None:
            result = my_curve.pointMult(generator, x)
            if result == Q:
                break

    print(f"x*P = ({bin_to_hex(result.x)}, {bin_to_hex(result.y)}), "
                             f" Q = ({bin_to_hex(Q.x)}, {bin_to_hex(Q.y)})")


if __name__ == "__main__":
    main()
