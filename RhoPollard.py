import math
import random
from random import randint
from binaryFieldCurve import BinaryFieldCurve
from mathops import modInv
from math import gcd

def func_f(X_i, P, Q, curve):
    try:
        assert curve.doesPointBelongToCurve(P) == True
        assert curve.doesPointBelongToCurve(Q) == True
    except AssertionError as e:
        print("Podane punkty nie naleza do krzywej")
        return None

    if int(X_i.x,2) % 3 == 2:
        return curve.pointAdd(X_i, Q)
    if int(X_i.x,2) % 3 == 0:
        return curve.pointMult(X_i, 2)
    if int(X_i.x,2) % 3 == 1:
        return curve.pointAdd(X_i, P)
    else:
        print("Error")
        return -1


def func_g(a, P, X_i, curve, n):
    try:
        assert curve.doesPointBelongToCurve(P) == True
    except AssertionError as e:
        print("Podane punkt nie nalezy do krzywej")
        return None

    if int(X_i.x, 2) % 3 == 2:
        return a
    if int(X_i.x, 2) % 3 == 0:
        return 2 * a % n
    if int(X_i.x, 2) % 3 == 1:
        return (a + 1) % n
    else:
        print("Error")
        return None

def func_h(b, P, X_i, curve, n):
    try:
        assert curve.doesPointBelongToCurve(P) == True
    except AssertionError as e:
        print("Podane punkty nie naleza do krzywej")
        return None

    if int(X_i.x, 2) % 3 == 2:
        return (b+1) % n
    if int(X_i.x, 2) % 3 == 0:
        return 2*b % n
    if int(X_i.x, 2) % 3 == 1:
        return (b + 1) % n
    else:
        print("Error")
        return None

def pollardRho(curve, P, Q, n):
    try:
        assert curve.doesPointBelongToCurve(P) == True
        assert curve.doesPointBelongToCurve(Q) == True
    except AssertionError as e:
        print("Podane punkty nie naleza do krzywej")
        return None


    for j in range(3):
        #random.seed(j)
        a_i = randint(0, n-1)
        b_i = randint(0, n-1)
        a_2i = randint(0, n-1)
        b_2i = randint(0, n-1)

        X_i = curve.pointAdd(curve.pointMult(P,a_i), curve.pointMult(Q,b_i))
        X_2i = curve.pointAdd(curve.pointMult(P,a_2i),curve.pointMult(Q,b_2i))

        i = 1
        while i <= n:
            print(f"Iteracja: {i}")
            a_i = func_g(a_i, P, X_i, curve, n)
            b_i = func_h(b_i, P, X_i, curve, n)
            X_i = func_f(X_i, P, Q, curve)

            a_2i = func_g(func_g(a_i, P, X_2i, curve, n), P, func_f(X_2i, P, Q, curve), curve, n)
            b_2i = func_h(func_h(a_i, P, X_2i, curve, n), P, func_f(X_2i, P, Q, curve), curve, n)
            X_2i = func_f(func_f(X_2i, P, Q, curve), P, Q, curve)

            if X_i == X_2i:
                print("Ding! Ding! Ding!")
                if b_i == b_2i:
                    break
                assert gcd(b_2i - b_i, n) == 1, f"gcd z ({b_2i - b_i}) i {n} nie jest rowne 1"
                return ((a_i - a_2i) * modInv(b_2i - b_i, n)) % n


            else:
                i +=1
                continue