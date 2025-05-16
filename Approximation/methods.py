import numpy as np

def normEqCoefs(xn, fn, n):
    m = len(xn) # формируем E
    E = [[0 for _ in range(n+1)] for __ in range(m)]
    for i in range(m):
        for j in range(n+1):
            E[i][j] = xn[i] ** j

    E = np.array(E)
    fs = np.array(fn)
    ETE, f =  E.transpose() @ E, E.transpose() @ fs # находим a 
    a = np.linalg.solve(ETE, f)
    a = a.tolist()
    return a

def normEq(xs, a):
    n = len(a)
    mas = []
    for i in range(len(xs)):
        pValue = sum(xs[i]**j * a[j] for j in range(n))
        mas.append(pValue)

    return mas

def ortPol(xs, xm, n):
    m = len(xm)
    q = np.zeros((n+1, len(xs)))
    qi = np.zeros((n+1, m))
    q[0, :] = 1
    qi[0, :] = 1
    
    q[1, :] = xs - np.mean(xm)
    qi[1, :] = xm - np.mean(xm)
    
    for j in range(1, n):
        alpha = np.sum(xm * qi[j] ** 2) / np.sum(qi[j] ** 2)
        beta = np.sum(xm * qi[j] * qi[j - 1]) / np.sum(qi[j - 1] ** 2)
        q[j + 1, :] = xs * q[j, :] - alpha * q[j, :] - beta * q[j - 1, :]
        qi[j + 1, :] = xm * qi[j, :] - alpha * qi[j, :] - beta * qi[j - 1, :]
    return q, qi


def ortPolCoef(f, qi):
    n = len(qi)
    a = np.zeros(n)
    for k in range(n):
        a[k] = np.sum(qi[k] * f) / np.sum(qi[k]**2)
    return a

def approx(xs, xm, ym, n):
    qs, qm = ortPol(xs, xm, n)
    a = ortPolCoef(ym, qm)
    y_approx = a @ qs
    return y_approx.tolist()
