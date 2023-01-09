import mathops
from Point import Point

point_inf = Point(0, 0)


class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def doesPointBelongToCurve(self, point):
        if (point.y**2 - point.x**3 - self.a*point.x - self.b) % self.p == 0:
            print(f"The point ({point.x}, {point.y}) belongs to the curve y^2 = x^3 + {self.a}x + {self.b}.")
        else:
            print(f"The point ({point.x}, {point.y}) doesn't belong to the curve y^2 = x^3 + {self.a}x + {self.b}.")

    def pointNegation(self, point):
        return Point(point.x, -point.y)
        x1 = pointP.x

    def pointAddition(self, pointP, pointQ):
        y1 = pointP.y
        x1 = pointP.x
        
        x2 = pointQ.x
        y2 = pointQ.y
        
        if pointP != pointQ:
            if pointP == self.pointNegation(pointQ):
                return point_inf
            elif pointP == point_inf:
                return pointQ
            elif pointQ == point_inf:
                return pointP
            else:
                m = ((y2 - y1) % self.p) * mathops.modInv(x2 - x1, self.p)
        else:
            m = ((3 * x1 ** 2) % self.p) * mathops.modInv(2 * y1, self.p)

        x3 = m**2-x1-x2
        y3 = y1+m*(x3-x1)

        result = Point(x3 % self.p, -y3 % self.p)

        return result

    def pointMultiplication(self, point, n):
        n_bin = bin(n)[2:]
        q = point_inf

        for i in range(len(n_bin)-1, -1, -1):
            if n_bin[i] == '1':
                q = self.pointAddition(q, point)
            point = self.pointAddition(point, point)

        return q