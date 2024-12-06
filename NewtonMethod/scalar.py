#1. x^2 - 1 = lnx

import math
def f(x):
    return x * x - 1 - math.log(x)

def df(x):
    return (2 * x * x - 1) / x

def posl_per(a, b):
    N = 1
    while True:
        h = (b - a) / N
        x0 = a
        for k in range(N + 1):
            x1 = a + k*h
            if f(x0) * f(x1) < 0:
                return x0, x1

            x0 = x1
        N *= 2

def newton(a, b):
    eps = 1e-4
    a0, b0 = posl_per(a, b)
    x0 = a0
    while True:
        if df(x0) == 0:
            if x0 == a0: x0 += eps
            else: x0 -= eps

        x1 = x0 - f(x0) / df(x0)

        if not(a0 <= x1 <= b0):
            x1 = (a0 + b0) / 2

        if f(a) * f(x1) < 0: b0 = x1
        else: a0 = x1

        if abs(x1 - x0) < eps:
            return x1
        x0 = x1




