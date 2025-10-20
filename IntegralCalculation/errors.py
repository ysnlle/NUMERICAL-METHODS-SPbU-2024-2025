from formulas import *
import numpy as np
import pandas as pd

n = [10, 20, 40, 80, 100, 150, 200]
exact_value = 6.238982679027518

def abs_error():
    errors_df = pd.DataFrame(index=n, columns=['Left Rectangles', 'Right Rectangles', 'Medium Rectangles', 
                                              'Trapezoid', 'Simpson', 'Gauss', 'Newton-Cotes'])
    
    errors_df['Left Rectangles'] = [abs(rect_qf(a, b, ni, type='left') - exact_value) for ni in n]
    errors_df['Right Rectangles'] = [abs(rect_qf(a, b, ni, type='right') - exact_value) for ni in n]
    errors_df['Medium Rectangles'] = [abs(rect_qf(a, b, ni, type='medium') - exact_value) for ni in n]

    errors_df['Trapezoid'] = [abs(trap_qf(a, b, ni) - exact_value) for ni in n]
    errors_df['Simpson'] = [abs(simpson_qf(a, b, ni) - exact_value) for ni in n]

    errors_df['Gauss'] = [abs(gauss_qf(a, b, ni) - exact_value) for ni in n]
    errors_df['Newton-Cotes'] = [abs(newton_cotes_qf(a, b, ni) - exact_value) for ni in n]
    return errors_df
