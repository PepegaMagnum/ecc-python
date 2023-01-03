import mathops
from Point import Point

point_inf = Point("0", "0")


class BinaryFieldCurve:
    def __init__(self, m, a, b, f):
        self.m = m
        self.a = a
        self.b = b
        self.f = f

    def doesPointBelongToCurve(self, point):
        y2 = mathops.binReduc(mathops.binSquare(point.y), self.f, self.m)
        x3 = mathops.binReduc(mathops.binMult(mathops.binSquare(point.x), point.x), self.f, self.m)
        xy = mathops.binReduc(mathops.binMult(point.x, point.y), self.f, self.m)

        x2 = mathops.binReduc(mathops.binSquare(point.x), self.f, self.m)

        ax2 = mathops.binReduc(mathops.binMult(self.a, x2), self.f, self.m)

        equation = mathops.binAdd(mathops.binAdd(mathops.binAdd(mathops.binAdd(y2, xy), x3), ax2), self.b)

        if equation == '0':
            print(f"Point ({point.x},{point.y}) belongs to the curve: y^2 + xy = x3 + ({self.a})x^2 + ({self.b})")
        else:
            print(f"Point ({point.x},{point.y}) does not belongs to the curve: y^2 + xy = x3 + ({self.a})x^2 + ({self.b})")

    def pointNeg(self, p):
        result = mathops.binAdd(p.x, p.y)
        return Point(p.x, result)

    def pointAdd(self, p, q):
        x1 = p.x
        y1 = p.y

        x2 = q.x
        y2 = q.y
        f = self.f
        a = self.a
        m = self.m

        if p != q:
            if p == self.pointNeg(q):
                return point_inf
            elif p == point_inf:
                return q
            elif q == point_inf:
                return p
            else:
                Lambda = mathops.binMult(mathops.binAdd(y1, y2), mathops.binInv(mathops.binAdd(x1, x2), f))

                x3 = mathops.binAdd(
                    mathops.binAdd(mathops.binAdd(mathops.binAdd(mathops.binSquare(Lambda), Lambda), a), x1), x2)
                y3 = mathops.binAdd(mathops.binAdd(mathops.binMult(mathops.binAdd(x1, x3), Lambda), x3), y1)

                x3 = mathops.binReduc(x3, f, m)
                y3 = mathops.binReduc(y3, f, m)

                return Point(x3, y3)
        else:
            return self.pointDoubling(p)

    def pointDoubling(self, p):
        x1 = p.x
        y1 = p.y

        f = self.f
        a = self.a
        m = self.m

        Lambda = mathops.binAdd(x1, mathops.binMult(y1, mathops.binInv(x1, f)))

        x3 = mathops.binAdd(mathops.binAdd(mathops.binSquare(Lambda), Lambda), a)
        y3 = mathops.binAdd(mathops.binAdd(mathops.binSquare(x1), mathops.binMult(Lambda, x3)), x3)

        x3 = mathops.binReduc(x3, f, m)
        y3 = mathops.binReduc(y3, f, m)

        return Point(x3, y3)

    def pointMult(self, p, n):
        n_bin = bin(n)[2:]
        q = point_inf

        for i in range(len(n_bin)-1, -1, -1):
            if n_bin[i] == '1':
                q = self.pointAdd(q, p)
            p = self.pointDoubling(p)
        return q