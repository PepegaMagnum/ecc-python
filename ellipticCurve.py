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

    def pointAddition(self, pointP, pointQ):
        x1 = pointP.x
        y1 = pointP.y
        
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
        result = point

        if n == 1:
            return result

        for x in range(1, n):
            result = self.pointAddition(result, point)

        return result


if __name__ == '__main__':
    curve = EllipticCurve(0, 7, 17)
    point1 = Point(15, 13)
    point2 = Point(1, 1)

    curve.doesPointBelongToCurve(point1)
    curve.doesPointBelongToCurve(point2)

    point3 = curve.pointAddition(point1, point1)

    print(f"Point doubling: ({point3.x},{point3.y})")

    curve.doesPointBelongToCurve(point3)

    point4 = curve.pointMultiplication(point1, 2)

    print(f"Point multiplication: ({point4.x},{point4.y})")
    curve.doesPointBelongToCurve(point4)

