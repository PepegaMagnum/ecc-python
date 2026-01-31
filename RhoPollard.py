import math
import random
import time
from random import randint
from binaryFieldCurve import BinaryFieldCurve
import mathops
from math import gcd

from mathops import binReduc


def func_f(X_i, P, Q, curve):
    try:
        assert curve.doesPointBelongToCurve(P) == True
        assert curve.doesPointBelongToCurve(Q) == True
    except AssertionError as e:
        print("Podane punkty nie naleza do krzywej")
        return None

    if int(X_i.x,2) % 3 == 0:
        return curve.pointAdd(X_i, Q)
    if int(X_i.x,2) % 3 == 1:
        return curve.pointMult(X_i, 2)
    if int(X_i.x,2) % 3 == 2:
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
        return mathops.binAdd(a, bin(1))
    if int(X_i.x, 2) % 3 == 1:
        return binReduc(mathops.binMult(bin(2), a), curve.f, curve.m)
    if int(X_i.x, 2) % 3 == 0:
        return binReduc(mathops.binAdd(a, bin(1)), curve.f, curve.m)
    else:
        print("Error")
        return None

def func_h(b, P, X_i, curve, n):
    try:
        assert curve.doesPointBelongToCurve(P) == True
    except AssertionError as e:
        print("Podane punkty nie naleza do krzywej")
        return None

    if int(X_i.x, 2) % 3 == 0:
        return mathops.binAdd(b, bin(1)[2:])
    if int(X_i.x, 2) % 3 == 1:
        return binReduc(mathops.binMult(b, bin(2)[2:]), curve.f, curve.m)
    if int(X_i.x, 2) % 3 == 2:
        return binReduc(mathops.binAdd(b, bin(1)[2:]), curve.f, curve.m)
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

    start = time.time()
    for j in range(3):
        #random.seed(j)
        a_i = bin(randint(0, n-1))[2:]
        b_i = bin(randint(0, n-1))[2:]
        a_2i = bin(randint(0, n-1))[2:]
        b_2i = bin(randint(0, n-1))[2:]

        X_i = curve.pointAdd(curve.pointMult(P, int(a_i, 2)), curve.pointMult(Q,int(b_i, 2)))
        X_2i = curve.pointAdd(curve.pointMult(P, int(a_2i,2)),curve.pointMult(Q,int(b_2i),))

        i = 1
        while i <= math.floor(math.sqrt(n)):
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
                stop = time.time()
                print(f"Algorithm took {stop - start} seconds")
                assert gcd(int(b_2i,2) - int(b_i,2), n)== 1, f"gcd z ({int(b_2i,2) - int(b_i,2)}) i {n} nie jest rowne 1"
                return (int(a_i, 2) - int(a_2i, 2)) * mathops.modInv(int(b_2i, 2) - int(b_i, 2), n) % n


            else:
                i +=1
                continue