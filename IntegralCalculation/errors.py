from formulas import *
import numpy as np
import pandas as pd
from scipy import integrate

exact_value1 = integrate.quad(f, a, b)[0]
exact_value2 = integrate.quad(F, a, b)[0]

def abs_error(n = [10, 20, 40, 80, 100, 150, 200]):
    errors_df1 = pd.DataFrame(index=n, columns=['Left Rectangles', 'Right Rectangles', 'Medium Rectangles', 
                                              'Trapezoid', 'Simpson'])

    errors_df2 = pd.DataFrame(index=n, columns=['Gauss', 'Newton-Cotes'])
    
    errors_df1['Left Rectangles'] = [abs(rect_qf(a, b, ni, type='left') - exact_value1) for ni in n]
    errors_df1['Right Rectangles'] = [abs(rect_qf(a, b, ni, type='right') - exact_value1) for ni in n]
    errors_df1['Medium Rectangles'] = [abs(rect_qf(a, b, ni, type='medium') - exact_value1) for ni in n]

    errors_df1['Trapezoid'] = [abs(trap_qf(a, b, ni) - exact_value1) for ni in n]
    errors_df1['Simpson'] = [abs(simpson_qf(a, b, ni) - exact_value1) for ni in n]

    errors_df2['Gauss'] = [abs(gauss_qf(a, b, parts=ni) - exact_value2) for ni in n]
    errors_df2['Newton-Cotes'] = [abs(newton_cotes_qf(a, b, parts=ni) - exact_value2) for ni in n]
    return errors_df1, errors_df2

def richardson(quad, min_part: int = 2, max_part: int = np.inf, eps=1e-6):
    r, R = 2, np.inf
    best_step, best_part = 0, 0
    int_len = b - a

    while R > eps and 2**r * min_part <= max_part:
        vals = [quad(a, b, parts=2**i * min_part) for i in range(r+1)]
        m = -np.log((vals[-1] - vals[-2]) / (vals[-2] - vals[-3])) / np.log(2)

        steps = [int_len / (2**i*min_part) for i in range(r+1)]

        steps_mat = np.array([[-1] + [steps[j]**(m+i) for i in range(r)] for j in range(r+1)])
        vals_vec = np.array(vals[:r+1])

        J, *_ = np.linalg.solve(steps_mat, -vals_vec)

        curR = abs(J - exact_value2)
        if curR < R:
            best_part = int(int_len / steps[-1])
            best_step = steps[-1]
            R = curR
        
        r += 1  
    return R, best_part, best_step

def opt_h_calc(quad, parts_list, eps=1e-6):
    vals = [quad(a, b, parts=parts) for parts in parts_list]
    m = -np.log(abs(vals[-1] - vals[-2]) / abs(vals[-2] - vals[-3])) / np.log(2)
    h = (b - a) / parts_list[0]

    h_opt = h * (eps * (1 - 2 ** (-m)) / abs(vals[0] - vals[1])) ** (1 / m)

    return h_opt