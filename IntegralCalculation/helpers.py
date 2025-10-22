import numpy as np

def moment(z1, z2, alpha, betta, s=0):
    deg = alpha
    return z2**(s - deg + 1) / (s - deg + 1) - z1**(s - deg + 1) / (s - deg + 1)

def cardano_roots(poly: np.ndarray):
    a, b, c, d = poly
    
    q = (2*b**3) / (54*a**3) - (b*c) / (6*a**2) + d / (2*a)
    p = (3*a*c - b**2) / (9 * a**2)

    r = np.sign(q) * np.sqrt(abs(p))
    phi = np.arccos(q / (r**3))
    
    y = np.array([-2*r*np.cos(phi/3),
                  2*r*np.cos(np.pi/3 - phi/3),
                  2*r*np.cos(np.pi/3 + phi/3)])
    x = y - b / (3*a)
    return x