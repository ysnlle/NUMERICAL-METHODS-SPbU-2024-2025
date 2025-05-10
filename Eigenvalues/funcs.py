from ClassMatrix import Matrix
import help
from Methods import LUP
import numpy as np

def PM(A: Matrix):
    n = len(A.matrix)
    delta, rtol = 1e-8, 1e-6
    y = Matrix([[1] for i in range(n)])
    z = y * (1/y.VecNorm())
    lam = Matrix([[0] for i in range(n)])

    while True:
        y = A * z
        countI = 0
        lam_k = Matrix([[0] for i in range(n)])
        
        for i in range(n):
            if abs(z.matrix[i][0]) > delta:
                countI += 1 
                lam_k.matrix[i][0] = y.matrix[i][0] / z.matrix[i][0]
        
        z = y * (1/y.VecNorm())
        if (lam_k - lam).VecNorm() <= rtol * max(lam_k.VecNorm(), lam.VecNorm()):
            res = 0
            for i in range(n):
                res += lam.matrix[i][0]
            res /= countI
            return res, z
        
        lam = lam_k.copy()

def InvertedPM(A: Matrix, sigma):
    delta, rtol = 1e-8, 1e-6
    n = len(A.matrix)
    y = Matrix([[1] for i in range(n)])
    z = y * (1/y.VecNorm())

    while True:
        M = (A - sigma * A.E())
        y = LUP(M, z)
        lam_k = Matrix([[0] for i in range(n)])

        countI = 0
        for i in range(n):  
            if abs(y.matrix[i][0]) > delta:
                countI += 1
                lam_k.matrix[i][0] = z.matrix[i][0] / y.matrix[i][0]
        z = y * (1/y.VecNorm())        

        if countI != 0:
            res = sigma + sum([lam_k.matrix[i][0] for i in range(n)]) / countI
            if abs(sigma - res) < rtol:
                return res, z
            sigma = res
        else: 
            return 'ойойойойой'

def AlgQR(A: Matrix):
    eps=1e-8
    n=len(A.matrix)
    E=A.E()
    H=help.Hessenberg(A)
    eigs=[]
    prev_bnn=None
    while True:
        bn=H.matrix[n-1][n-1] if n > 0 else 0
        Q,R = help.HQR(H-bn*E.copy())
        H = R*Q+bn*E.copy()
        if prev_bnn is not None and abs(H.matrix[-1][-1] - prev_bnn) < (1 / 3) * abs(prev_bnn):
            if abs(H.matrix[n-1][n-2]) < eps:
                if n>2:
                    eigs.append(H.matrix[n-1][n-1])
                    H = Matrix([[H.matrix[k][j] for k in range(n-1)] for j in range(n-1)])
                    n -= 1
                if n==2:
                    eigs.append(H.matrix[0][0]) 
                    eigs.append(H.matrix[1][1])
                    return sorted(eigs)
        prev_bnn = bn
            

 