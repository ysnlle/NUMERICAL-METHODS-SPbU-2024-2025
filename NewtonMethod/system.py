#2. sin(x + 1) - y = 1
#   2x + cosy = 2

import math
from ClassMatrix import Matrix
from Methods import LUP

def f(x, y, l = 1):
    return Matrix([[l * math.sin(x + 1) - y - 1], [2 * x + l * math.cos(y) - 2]])

def df(x, y, l = 1):
    return Matrix([[l * math.cos(x + 1), -1], [2, -l * math.sin(y)]])

def posl_per():
    N = 10
    i = 1
    data = Matrix([[0],[0]])
    while i <= 20:
        data += LUP(df(data.matrix[0][0], data.matrix[1][0], i / N), -1 * f(data.matrix[0][0], data.matrix[1][0], i / N))
        i += 1
    return data

def newton():
    eps = 1e-4
    x0 = posl_per()
    while True:
        delta = LUP(df(x0.matrix[0][0], x0.matrix[1][0]), -1 * f(x0.matrix[0][0], x0.matrix[1][0]))
        if delta.VecNorm() < eps:
            return delta + x0
        x0 = delta + x0
