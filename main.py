from binaryFieldCurve import BinaryFieldCurve
from Point import Point


def main():
    bincurve = BinaryFieldCurve(m=4, a="1000", b="1001", f="10011")
    p1 = Point("10", "1111")
    p1neg = bincurve.pointNeg(p1)

    bincurve.doesPointBelongToCurve(p1neg)

    print(f"Point negation ({p1.x}, {p1.y}) = ({p1neg.x}, {p1neg.y})")

    p2 = Point("1100", "1100")
    p3 = Point("0000", "0001")


    bincurve.doesPointBelongToCurve(p1)
    bincurve.doesPointBelongToCurve(p2)
    bincurve.doesPointBelongToCurve(p3)

    p4 = bincurve.pointAdd(p1, p2)

    p5 = bincurve.pointDoubling(p1)


    twop1 = bincurve.pointMult(p1, 2)
    p1double = bincurve.pointDoubling(p1)
    print(f"2p1 = ({twop1.x}, {twop1.y})")
    print(f"2p1 = ({p1double.x}, {p1double.y})")


if __name__ == "__main__":
    main()
