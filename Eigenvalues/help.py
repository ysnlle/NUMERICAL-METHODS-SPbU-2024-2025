from random import randint
from ClassMatrix import Matrix
from math import sqrt

def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def randmat(n):
    maxV = 10
    minV = 0
    matrix = [[randint(minV, maxV) for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] += n
    return Matrix(matrix)

def randdiag(n):
    maxV = 10
    minV = 1
    matrix = [[randint(minV, maxV) if i == j else 0 for i in range(n)] for j in range(n)]
    return Matrix(matrix)

def Hessenberg(A: Matrix):
    n = len(A.matrix)
    He = A.copy()
    E = A.E()
    for i in range(n-2):
        v = Matrix([[0] for i in range(n)])

        for j in range(n):
            v.matrix[j][0] = He.matrix[j][i]
        for j in range(i+1):
            v.matrix[j][0] = 0
        s = -sgn(v.matrix[i+1][0]) * v.VecNorm()
        mu = 1/sqrt(2*s*(s - v.matrix[i+1][0]))
        v.matrix[i+1][0] = v.matrix[i+1][0] - s
        v = mu * v

        H = E.copy() - 2 * v * v.Transp() 
        He = H * He * H
    return He
'''
def Hessenberg(A: Matrix):
    n = len(A.matrix)
    Hess = A.copy()
    for i in range(n - 2):
        H=A.E()
        w=Matrix([[0] for i in range(n)])
        for j in range(i+1, n):
            w.matrix[j-i][0]=Hess.matrix[j][i]
        norm =(-1 if w.matrix[i+1][0] >= 0 else 1)* sqrt(sum([w.matrix[j][0]**2 for j in range(1, n - i)]))
        if norm != 0:
            H=A.E()
            nu = 1 / sqrt((2 * norm * (norm - w.matrix[i+1][0])))
            w.matrix[i+1][0]-=norm
            w = w*nu
            block = A.E() - 2 * (w * w.Transp())
            for j in range(i, n):
                for k in range(i, n):
                    H.matrix[j][k] = block.matrix[j][k]
        Hess = H * Hess * H
    return Hess
'''
def HQR(A: Matrix):
    n = len(A.matrix)
    Q = A.E()
    R = A.copy()
    
    for j in range(n - 1):  
        for i in range(j + 1, n):
            if abs(R.matrix[i][j]) > 1e-8:

                x = R.matrix[j][j]
                y = R.matrix[i][j]
                r = sqrt(x**2 + y**2)
                c = x/r if r != 0 else 1.0
                s = -y/r if r != 0 else 0.0
                
                G = A.E()  
                G.matrix[j][j] = c
                G.matrix[i][j] = s
                G.matrix[j][i] = -s
                G.matrix[i][i] = c
                
                R = G * R
                Q = Q * G.Transp()  
    
    return Q, R