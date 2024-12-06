from math import sqrt

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.dim = {'col' : len(self.matrix[0]),'str' : len(self.matrix)}

    def __add__(self, other):
        ans = [[] for _ in range(self.dim['str'])]

        for i in range(self.dim['str']):
            for j in range(self.dim['col']):
                ans[i].append(self.matrix[i][j] + other.matrix[i][j])

        return Matrix(ans)

    def __sub__(self, other):
        return self.__add__(-1 * other)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.dim['col'] != other.dim['str']:
                raise ValueError(
                    "Невозможно умножить матрицы")

            ans = [[0 for _ in range(other.dim['col'])] for _ in range(self.dim['str'])]
            for i in range(self.dim['str']):
                for j in range(other.dim['col']):
                    for k in range(self.dim['col']):
                        ans[i][j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix(ans)

        else:
            return self.__rmul__(other)

    def __rmul__(self,scalar):
        ans = [[0 for _ in range(self.dim['col'])] for _ in range(self.dim['str'])]

        for i in range(self.dim['str']):
            for j in range(self.dim['col']):
                ans[i][j] = self.matrix[i][j] * scalar

        return Matrix(ans)

    def copy(self):
        ans = [[0 for _ in range(self.dim['col'])] for _ in range(self.dim['str'])]
        for i in range(self.dim['str']):
            for j in range(self.dim['col']):
                ans[i][j] = self.matrix[i][j]

        return Matrix(ans)

    def Transp(self):
        ans = []

        for j in range(self.dim['col']):
            temp = []
            for i in range(self.dim['str']):
                temp.append(self.matrix[i][j])
            ans.append(temp)

        return Matrix(ans)

    def InfNorm(self): #макс значение по строкам(бесконечная норма)
        ans = []
        for i in range(self.dim['str']):
            temp = 0
            for j in range(self.dim['col']):
                temp += abs(self.matrix[i][j])
            ans.append(temp)
        return max(ans)

    def OneNorm(self): #макс значение по столбцам(еденичная норма)
        ans = []
        for i in range(self.dim['col']):
            temp = 0
            for j in range(self.dim['str']):
                temp += abs(self.matrix[j][i])
            ans.append(temp)
        return max(ans)

    def VecNorm(self):
        ans = 0
        if self.dim['str'] == 1:
            for i in range(self.dim['col']):
                ans += self.matrix[0][i] ** 2
            return sqrt(ans)
        if self.dim['col'] == 1:
            for i in range(self.dim['str']):
                ans += self.matrix[i][0] ** 2
            return sqrt(ans)

    def IsDiagDom(self):
        for i in range(self.dim['str']):
            diag_el = abs(self.matrix[i][i])
            other_sum = -1 * diag_el

            for j in range(self.dim['col']):
                other_sum += abs(self.matrix[i][j])

            if diag_el < other_sum:
                return False

        return True

    def PosDef(self):
        ln = len(self.matrix)
        for k in range(1, ln + 1):
            B = Matrix([self.matrix[i][:k] for i in range(0, k)])
            if B.Det() <= 0: return False

        return True

    def Det(self):
        det = 0
        ln = len(self.matrix)

        if ln == 1: return self.matrix[0][0]
        elif ln == 2: return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            for k in range(ln):
                B = Matrix([self.matrix[i][:k] + self.matrix[i][k+1:] for i in range(1,ln)])
                det += self.matrix[0][k] * (-1) ** k * B.Det()

        return det

    def E(self):
        ans = [[0 for _ in range(self.dim['col'])] for _ in range(self.dim['str'])]
        for i in range(self.dim['str']):
            ans[i][i] += 1
        return Matrix(ans)

    def Ort(self):
        ans = [[0] for _ in range(self.dim['str'])]
        ans[0][0] = 1
        return Matrix(ans)

    def PrintM(self):
        for i in range(self.dim['str']):
            print(*self.matrix[i])

