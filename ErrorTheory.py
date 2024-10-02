from math import sin, atan, sqrt, pi
from prettytable import PrettyTable

# вычисленные значения допустимых погрешностей
eps = 1e-6
eps_f = eps / 3
eps_u = eps / 1.608
eps_v = eps / 3.198

#факториал
def fact(x):
    ans = 1
    for i in range(1,int(x + 1)):
        ans *= i
    return ans

# знак числа
def sgn(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

# функция корня
def my_sqrt(arg):
    if arg > 1:
        p0 = arg
    else:
        p0 = 1
    while True:
        p = 1/2 * (p0 + arg/p0)
        if abs(p - p0) < eps_u:
            return p
        p0 = p

# функция синуса
def my_sin(arg):
    p0 = 0
    k = 0
    while True:
        p = p0 + (((-1) ** k) * (arg ** (2 * k + 1)) / fact(2 * k + 1))
        if abs(p - p0) < eps_v:
            return p
        p0 = p
        k += 1

# функция арктангенса
def my_atan(arg):
    p0 = 0
    k = 0
    if abs(arg) < 1:
        while True:
            p = p0 + (((-1) ** k) * (arg ** (2 * k + 1)) / (2 * k + 1))
            if abs(p - p0) < eps_f:
                return p
            p0 = p
            k += 1
    else:
        while True:
            p = p0 + (((-1) ** k) * (arg ** (-(2 * k + 1))) / (2 * k + 1))
            if abs(p - p0) < eps_f:
                return (pi / 2 * sgn(arg)) - p
            p0 = p
            k+=1

# функция, вычисляющая значение функции с помощью "моих" функций и встроенных
# в качестве ответа выдает таблицу ( как в примере )
def all_values(a, h, b):
    arr = PrettyTable()
    arr.field_names = ['x', 'u_', 'eps_u', 'u', 'delta_u', 'v_', 'eps_v', 'v', 'delta_v', 'f_', 'eps_f', 'f', 'delta_f']

    while a <= b:
        a = round(a,3)

        u_ = my_sqrt(1 + 0.6 * a)
        u = sqrt(1 + 0.6 * a)

        v_ = my_sin(1 + 0.4 * a)
        v = sin(1 + 0.4 * a)

        f_ = my_atan(u_) / v_
        f = atan(u) / v

        delta_u = abs(u_ - u)
        delta_v = abs(v_ - v)
        delta_f = abs(f_ - f)
        
        arr.add_row([a, u_, eps_u, u, delta_u, v_, eps_v, v, delta_v, f_, eps_f, f, delta_f])

        a += h
    return arr

a = 0.2
b = 0.3
h = 0.01

ans = PrettyTable()
ans = all_values(a,h,b)

print(ans)



