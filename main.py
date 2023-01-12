from binaryFieldCurve import BinaryFieldCurve
from ellipticCurve import EllipticCurve
from Point import Point
import time
import sys

def main():
    # Curve K-163
    print("Tests for binary field curve")

    k = 1000000000000 #int(sys.argv[1])

    f = bin((1<<163)+int("11001001", 2))[2:]
    k163 = BinaryFieldCurve(163, "1", "1", f)
    xhex = "02fe13c0537bbc11acaa07d793de4e6d5e5c94eee8"
    yhex = "0289070fb05d38ff58321f2e800536d538ccdaa3d9"

    xint = int(xhex, 16)
    yint = int(yhex, 16)

    xbin = bin(xint)[2:]
    ybin = bin(yint)[2:]

    print(f"Size of x: {len(xbin)}")
    print(f"Size of y: {len(ybin)}")

    g1 = Point(xbin, ybin)

    k163.doesPointBelongToCurve(g1)

    start_time1 = time.time_ns()
    gmult1 = k163.pointMult(g1, k)
    end_time1 = time.time_ns()

    multiplication_time1 = end_time1 - start_time1

    print(f"Multiplication time: {multiplication_time1 / (10 ** 9)} seconds")
    print(f"Size of result x: {len(gmult1.x)}")
    print(f"Size of result y: {len(gmult1.y)}")

    k163.doesPointBelongToCurve(gmult1)

    # secp192k1
    print("\nTests for prime field curve")

    phex = "fffffffffffffffffffffffffffffffffffffffeffffee37"
    pint = int(phex, 16)
    secp192k1 = EllipticCurve(0, 3, pint)

    g2 = Point(int("db4ff10ec057e9ae26b07d0280b7f4341da5d1b1eae06c7d", 16),
              int("9b2f2f6d9c5628a7844163d015be86344082aa88d95e2f9d", 16))

    size_of_x_g2 = len(bin(g2.x)[2:])
    size_of_y_g2 = len(bin(g2.y)[2:])

    print(f"size of x: {size_of_x_g2}")
    print(f"size of x: {size_of_y_g2}")

    secp192k1.doesPointBelongToCurve(g2)

    start_time2 = time.time_ns()
    gmult2 = secp192k1.pointMultiplication(g2, k)
    end_time2 = time.time_ns()

    secp192k1.doesPointBelongToCurve(gmult2)

    multiplication_time2 = end_time2 - start_time2
    print(start_time2)
    print(end_time2)

    print(f"Multiplication time: {multiplication_time2/(10**9)} seconds")
    print(f"Size of result x: {len(bin(gmult2.x)[2:])}")
    print(f"Size of result y: {len(bin(gmult2.y)[2:])}")


if __name__ == "__main__":
    main()
