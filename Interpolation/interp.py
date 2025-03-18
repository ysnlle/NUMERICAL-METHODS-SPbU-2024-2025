from help import *

def Ln(x, a, b, n):
    s = sum(terms(x, i, a, b, n, False) for i in range(n))
    return s
def Loptn(x, a, b, n):
    s = sum(terms(x, i, a, b, n, True) for i in range(n))
    return s

def Nn(x, a, b, n):
    values = nodes(a, b, n)
    l = div_diff(n, values)
    s = l[-1]
    for i in range(n-2,-1,-1):
        s = s * (x - values[i]) + l[i]
    return s

def Noptn(x, a, b, n):
    values = opt_nodes(a, b, n)
    l = div_diff(n, values)
    s = l[-1]
    for i in range(n-2,-1,-1):
        s = s * (x - values[i]) + l[i]
    return s