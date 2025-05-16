import numpy as np

def f(x):
    return (x+3) * np.cos(x)

def nodes(n, a=-1, b=1):
    return np.linspace(a, b, n)

def randNodes(m, a=-1, b=1):
    return [a+(b-a)*np.random.random() for i in range(m)]

def generator(xs, repeats = 3):
    xs = np.repeat(xs, repeats)
    data = [f(x) - (np.random.random() - 0.5)/5 for x in xs]
    return data, xs

def loss(real, approx):
    return sum((real[i] - approx[i])**2 for i in range(len(real)))

