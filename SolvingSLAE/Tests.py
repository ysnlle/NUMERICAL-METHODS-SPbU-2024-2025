from numpy.ma.core import array

from Methods import *
from numpy import linalg


def test(n):
    N = 18

    if n == 0:
        A = Matrix([[0., 2., 3.],
                    [1., 2., 4.],
                    [4., 5., 6.]])
        b = Matrix([[13.], [17.], [32.]])

    if n == 1:
        A = Matrix([[N + 2, 1, 1],
                    [1, N + 4, 1],
                    [1, 1, N + 6]])

        b = Matrix([[N + 4], [N + 6], [N + 8]])

    if n == 2:
        A = Matrix([[-N - 2, 1, 1],
                    [1, -N - 4, 1],
                    [1, 1, - N- 6]])

        b = Matrix([[-N - 4], [-N - 6], [-N - 8]])

    if n == 3:
        A = Matrix([[-N - 2, N + 3, N + 4],
                    [N + 5, -N - 4, N + 1],
                    [N + 4, N + 5, -N - 6]])

        b = Matrix([[N + 4], [N + 6], [N + 8]])

    if n == 4:
        A = Matrix([[N + 2, N + 1, N + 1],
                    [N + 1, N + 4, N + 1],
                    [N + 1, N + 1, N + 6]])

        b = Matrix([[N + 4], [N + 6], [N + 8]])


    ans = []

    ans.append(SIM(A.copy(), b.copy()))
    ans.append(SeidelM(A.copy(), b.copy()))
    ans.append(LUP(A.copy(), b.copy()))
    ans.append(QR(A.copy(), b.copy()))

    return ans

def test5(n, eps):
    N = 18
    A, b  = [], []
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp.append(1 + eps * N)
            if i < j:
                temp.append(-1 - eps * N)
            if i > j:
                temp.append(eps * N)
        A.append(temp)

        if i < n - 1: b.append([-1])
        else: b.append([1])
    
    A = Matrix(A)
    b = Matrix(b)

    ans = []

    ans.append(SIM(A, b))
    ans.append(SeidelM(A, b))
    ans.append(LUP(A, b))
    ans.append(QR(A, b))

    return ans

def answers(n):
    N = 18

    if n == 0:
        A = array([[0., 2., 3.],
                    [1., 2., 4.],
                    [4., 5., 6.]])
        b = array([[13.], [17.], [32.]])

    if n == 1:
        A = array([[N + 2, 1, 1],
                    [1, N + 4, 1],
                    [1, 1, N + 6]])

        b = array([[N + 4], [N + 6], [N + 8]])

    if n == 2:
        A = array([[-N - 2, 1, 1],
                    [1, -N - 4, 1],
                    [1, 1, - N - 6]])

        b = array([[-N - 4], [-N - 6], [-N - 8]])

    if n == 3:
        A = array([[-N - 2, N + 3, N + 4],
                    [N + 5, -N - 4, N + 1],
                    [N + 4, N + 5, -N - 6]])

        b = array([[N + 4], [N + 6], [N + 8]])

    if n == 4:
        A = array([[N + 2, N + 1, N + 1],
                    [N + 1, N + 4, N + 1],
                    [N + 1, N + 1, N + 6]])

        b = array([[N + 4], [N + 6], [N + 8]])

    return linalg.solve(A, b)

def answer5(n, eps):
    N = 18
    A, b = [], []
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j:
                temp.append(1 + eps * N)
            if i < j:
                temp.append(-1 - eps * N)
            if i > j:
                temp.append(eps * N)
        A.append(temp)

        if i < n - 1:
            b.append([-1])
        else:
            b.append([1])

    A = array(A)
    b = array(b)

    return linalg.solve(A, b)
