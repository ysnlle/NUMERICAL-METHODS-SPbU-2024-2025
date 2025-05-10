from ClassMatrix import Matrix

def SIM(A, b, eps = 1e-6):
     k = 0
     mu = 1 / A.InfNorm()
     B = A.E() - mu * A
     Bnorm = B.InfNorm()

     if Bnorm >= 1:
          T = A.Transp()
          A = T * A
          b = T * b
          mu = 1 / A.InfNorm()
          B = A.E() - mu * A
          Bnorm = B.InfNorm()

     c = mu * b
     x0 = c

     while True:
          k += 1
          x1 = B * x0 + c
          if Bnorm <= 1 and (Bnorm/(1 - Bnorm)) * (x1-x0).VecNorm() <= eps:
               return x1, k

          elif Bnorm >= 1 and (A * x1 - b).VecNorm() <= eps:
               return x1, k
          x0 = x1

def SeidelM(A, b, eps = 1e-6):
     k = 0
     if A.IsDiagDom() == False or A.PosDef() == False:
          T = A.Transp()
          A = T * A
          b = T * b

     C = Matrix([[0 for _ in range(A.dim['col'])] for _ in range(A.dim['str'])])
     d = Matrix([[0] for _ in range(b.dim['str'])])

     for i in range(A.dim['str']):
          for j in range(A.dim['col']):
               if i == j: pass
               else:
                    C.matrix[i][j] = -(A.matrix[i][j] / A.matrix[i][i])
          d.matrix[i][0] = b.matrix[i][0] / A.matrix[i][i]

     x0 = d

     while True:
          k += 1
          x1 = Matrix([[0] for _ in range(b.dim['str'])])

          for i in range(C.dim['str']):
               for j in range(C.dim['col']):
                    if j < i:
                         x1.matrix[i][0] += C.matrix[i][j] * x1.matrix[j][0]

                    elif j != i:
                         x1.matrix[i][0] += C.matrix[i][j] * x0.matrix[j][0]
               x1.matrix[i][0] = x1.matrix[i][0] + d.matrix[i][0]

          approx = (A * x1 - b).VecNorm()

          if approx <= eps:
               return x1, k
          x0 = x1

def LUP(A: Matrix, b: Matrix):
     M, P = A.copy(), A.copy().E()
     n = len(A.matrix)
     for i in range(n-1):
          m = i
          for j in range(i, n):
               if abs(M.matrix[m][i]) < abs(M.matrix[j][i]):
                    m = j

          if m != i:
               M.matrix[i], M.matrix[m] = M.matrix[m], M.matrix[i]
               P.matrix[i], P.matrix[m] = P.matrix[m], P.matrix[i]

          for j in range(i + 1, n):
               M.matrix[j][i] = M.matrix[j][i] / M.matrix[i][i]

               for k in range(i + 1, n):
                    M.matrix[j][k] -= M.matrix[j][i] * M.matrix[i][k]

     L, U = A.E(), A.E()
     for i in range(n):
          for j in range(n):
               if i == j:
                    L.matrix[i][j] = 1
                    U.matrix[i][j] = M.matrix[i][j]

               if i > j:
                    L.matrix[i][j] = M.matrix[i][j]
                    U.matrix[i][j] = 0

               if i < j:
                    U.matrix[i][j] = M.matrix[i][j]

     #Ly = Pb Ux = y
     Pb = P * b
     y = Matrix([[0] for i in range(n)])

     for i in range(n):
          y.matrix[i][0] = Pb.matrix[i][0]
          for j in range(i):
               y.matrix[i][0] -= L.matrix[i][j] * y.matrix[j][0]

     x = Matrix([[0] for i in range(n)])
     for i in reversed(range(n)):
          x.matrix[i][0] = y.matrix[i][0] / U.matrix[i][i]

          for j in range(i+1,n):
               x.matrix[i][0] -= U.matrix[i][j] * x.matrix[j][0] / U.matrix[i][i]

     return x
def QR(A, b):
     Q, R = A.E(), A.copy()
     s, c = A.dim['str'], A.dim['col']

     for i in range(s - 1):
          y = Matrix([[R.matrix[j][i]] for j in range(i,s)])
          a, z = y.VecNorm(), y.Ort()
          p = (y - a * z)
          w = p * (1 / p.VecNorm())

          Q1 = A.E()
          Q_ = (w * w.Transp()).E() - 2 * w * w.Transp()
          for j in range(i, s):
               for k in range(i, s):
                    Q1.matrix[j][k] = Q_.matrix[j - i][k - i]

          Q = Q * Q1.Transp()
          R = Q1 * R

     y = Q.Transp() * b
     x = Matrix([[0] for i in range(s)])

     for i in reversed(range(s)):
          x.matrix[i][0] = y.matrix[i][0] / R.matrix[i][i]
          for j in range(i + 1, s):
               x.matrix[i][0] -= R.matrix[i][j] * x.matrix[j][0] / R.matrix[i][i]

     return x