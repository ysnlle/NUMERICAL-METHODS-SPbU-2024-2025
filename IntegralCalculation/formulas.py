import helpers
import numpy as np
import matplotlib.pyplot as plt

# отрезок интегрирования
a = 1.1
b = 2.3
alpha = 0.8
betta = 0

# функция
def f(x):
    return 3.5 * np.cos(0.7*x) * np.exp(-5*x/3) + 2.4 * np.sin(5.5*x) * np.exp(-3*x/4) + 5

# КФ левого, правого и среднего треугольников
def rect_qf(a, b, n=10, type='medium'):
    h = (b - a) / n
    xi = np.linspace(a, b, n)

    # составная формула левых прямоугольников
    if type == 'left':
        return h * np.sum(f(xi[:n-1]))
    # составная формула правых прямоугольников
    if type == 'right':
        return h * np.sum(f(xi[1:]))
    
    # составная формула средних прямоугольников
    if type == 'medium':
        return h * np.sum(f(xi[:n-1] + h/2)) 
            
# КФ трапеции
def trap_qf(a, b, n=10):
    h = (b - a) / n
    xi = np.linspace(a, b, n)

    return h * (f(a)/2 + np.sum(f(xi[1:n-1])) + f(b)/2)

# КФ Симпсона
def simpson_qf(a, b, n=10):
    h = (b - a) / (2*n)
    xi = np.linspace(a, b, n)

    return h/3 * (f(a) + f(b) + 4 * np.sum(f(xi[1:])) + 2 * np.sum(f(xi[1:n-1]+h)))

def gauss_qf(a, b, parts=100):
    t, f_ = a, lambda x: x**alpha*f(x+t)
    a, b = 0, b - a

    h = (b - a) / parts
    n = 3
    I = 0

    for i in range(parts):
        z1 = a + i * h
        z2 = a + (i + 1) * h

        mu_vec = np.array(([helpers.moment(z1, z2, alpha=alpha, betta=betta, s=j) for j in range(2*n)]))
        mu_mat = np.array([mu_vec[j:j+n] for j in range(n)])
        a_coeffs = np.linalg.solve(mu_mat, -mu_vec[n:]).flatten()
        
        a_coeffs = np.append([1], a_coeffs[::-1])
        nodes = helpers.cardano_roots(a_coeffs)

        nodes_mat = np.array([nodes ** s for s in range(n)])
        A = np.linalg.solve(nodes_mat, mu_vec[:n])

        I += A @ f_(nodes)
    
    return I
        

# ньютон-котс
def newton_cotes_qf(a, b, parts=100):
    t, f_ = a, lambda x: x**alpha*f(x+t)
    a, b = 0, b - a

    h = (b - a) / parts
    I = 0
    n = 3

    for i in range(parts):
        nodes = np.array([a + i * h,
                          a + (i+0.5) * h,
                          a + (i+1) * h])
        
        mu_vec = np.array([helpers.moment(nodes[0], nodes[2], alpha=alpha, betta=betta, s=s) for s in range(n)])

        nodes_mat = np.array([nodes ** s for s in range(n)])
        A = np.linalg.solve(nodes_mat, mu_vec)

        I += A @ f_(nodes)
    
    return I