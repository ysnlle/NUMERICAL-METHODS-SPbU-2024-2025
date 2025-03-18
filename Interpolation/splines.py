from ClassMatrix import Matrix
from Methods import LUP
from help import *

def LS(a, b, n):
    values = nodes(a,b,n)
    f_values = [f(values[i]) for i in range(n)]
    coefs = [0] * 2*n
    for i in range(n-1):
        X = Matrix([[values[i],1],[values[i+1],1]])
        y = Matrix([[f_values[i]], [f_values[i+1]]])
        ans = LUP(X,y)
        coefs[2*i],coefs[2*i+1] = ans.matrix[0][0],ans.matrix[1][0]
    return coefs

def LinearSpline(x, coefs, values, n):
    for i in range(n):
        if values[i] <= x <= values[i+1]:
            return coefs[2*i]*x + coefs[2*i+1]


def SqS(a,b,n):
    values = nodes(a,b,n)
    f_values = [f(values[i]) for i in range(n)]
    coefs = [0] * 3 * (n-1)
    X = []
    y = []
    for i in range(n-1):
        row1 = [0] * 3 * (n-1)
        row2 = [0] * 3 * (n-1)
        row1[3*i] = values[i] ** 2
        row1[3*i+1] = values[i]
        row1[3*i+2] = 1
        row2[3*i] = values[i+1] ** 2
        row2[3*i+1] = values[i+1]
        row2[3*i+2] = 1
        X.append(row1)
        X.append(row2)
        y.append([f_values[i]])
        y.append([f_values[i+1]])
        if i < n-2:
            row = [0] * 3 * (n-1)
            row[3*i] = 2 * values[i+1]
            row[3*i+1] = 1
            row[3*i+3] = -2 * values[i+1]
            row[3*i+4] = -1
            X.append(row)
            y.append([0])
    row = [0] * 3 * (n-1)
    row[0] = 0.4
    row[1] = 1
    X.append(row)
    y.append([-5.6])
    
    X = Matrix(X)
    y = Matrix(y)
    ans = LUP(X,y).matrix
    for i in range(n-1):
        coefs[3*i] = ans[3*i][0]
        coefs[3*i+1] = ans[3*i+1][0]
        coefs[3*i+2] = ans[3*i+2][0]
    return coefs


def SquareSpline(x, coefs, values, n):
    for i in range(n):
        if values[i] <= x <= values[i+1]:
            return coefs[3*i] * (x**2) + coefs[3*i+1] * x + coefs[3*i+2]

def CbS(a, b, n):
    values = nodes(a, b, n)
    f_values = [f(values[i]) for i in range(n)]
    hx = [values[i+1] - values[i] for i in range(n-1)]
    hy = [f_values[i+1] - f_values[i] for i in range(n-1)]
    gamma = []
    for i in range(1, n-1):
        gamma.append([6*(hy[i]/hx[i] - hy[i-1]/hx[i-1])])
    H = []
    for i in range(n-2):
        mas = [0] * (n-2)
        if i == 0:
            mas[i] = 2 * (hx[i] + hx[i+1])
            mas[i+1] = hx[i+1]
        elif i == n - 3:
            mas[i-1] = hx[i]
            mas[i] = 2 * (hx[i] + hx[i+1])
        else:
            mas[i-1] = hx[i]
            mas[i] = 2 * (hx[i] + hx[i+1])
            mas[i+1] = hx[i+1]
        H.append(mas)
    
    H = Matrix(H)
    gamma = Matrix(gamma)
    sec_diffs = LUP(H, gamma)
    sec_diffs = [0] + [sec_diffs.matrix[i][0] for i in range(n-2)] + [0]
    fir_diffs = [hy[i]/hx[i] - sec_diffs[i+1]*hx[i]/6 - sec_diffs[i]*hx[i]/3 for i in range(n-1)]
    
    coefs = [0] * (4*n-4)
    for i in range(n-1):
        coefs[4*i] = f_values[i]
        coefs[4*i+1] = fir_diffs[i]
        coefs[4*i+2] = sec_diffs[i] / 2
        coefs[4*i+3] = (sec_diffs[i+1] - sec_diffs[i])/(6*hx[i])
    return coefs

def CubicSpline(x, coefs, values, n):
    for i in range(n-1):
        if values[i] <= x <= values[i+1]:
            return coefs[4*i] + coefs[4*i+1] * (x - values[i]) + coefs[4*i+2] * (x - values[i])**2 + coefs[4*i+3] *(x - values[i])**3
