from math import *

def f(x): # моя функция 
    return x**2 - 1 - log(x)

def nodes(a, b, n): # узлы на равном расстоянии
    return [a + (b - a) * i / (n - 1) for i in range(n)]

def opt_nodes(a, b, n): # оптимальные узлы
    l = [0] * n
    for i in range(n):
        l[i] = 0.5 * ((b - a) * cos((pi*(2*i+1))/(2*n+2)) + (b + a))
    return l

def terms(x, k, a, b, n, opt): # множители лагрнжа, умноженные на значение в точке
    lk = 1
    nodeList = nodes(a, b, n) if not(opt) else opt_nodes(a, b, n)

    for i in range(n):
        if i != k:
            lk *= (x - nodeList[i]) / (nodeList[k] - nodeList[i])
    return lk * f(nodeList[k])

def max_dev(f, interp):
    return max(abs(f[i] - interp[i]) for i in range(len(interp)))

def div_diff(n, nodes):
    l = [f(x) for x in nodes]

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            l[j] = (l[j] - l[j-1]) / (nodes[j] - nodes[j-i])
    return l

def abs_error(f_values, approx, n):
    return  [abs(f_values[i] - approx[i]) for i in range(n)]