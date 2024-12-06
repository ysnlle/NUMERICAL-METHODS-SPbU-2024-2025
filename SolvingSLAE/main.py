from Tests import *
from prettytable import PrettyTable

print('Simple Iterations Method(0 - 4)')
table = PrettyTable()
table.field_names = ['№', 'x_', 'eps', 'x', 'delta', 'k']

x_ = Matrix(answers(0))

for i in range(5):
    num = i
    x_ = Matrix(answers(i))
    eps = 1e-6
    x, k = test(i)[0]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
            table.add_row([i, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0], k])
        else:
            table.add_row(['', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0], ''])
    table.add_row(['---','-' * 20,'---','-' * 20,'-' * 20,'-----'])

print(table)

print('Simple Iterations Method test 5')
table = PrettyTable()
table.field_names = ['n','e','x_','eps','x','delta','k']

for n in range(3,7):
    x_ = Matrix(answer5(n,1e-3))
    x,k = test5(n,1e-3)[0]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    eps = 1e-6

    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
                table.add_row([n, 1e-3, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0], k])
        else:
            table.add_row(['','', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0], ''])
    table.add_row(['---', '---','-' * 20, '---', '-' * 20, '-' * 20, '-----'])
print(table)

print('Seidel Method(0 - 4)')

table = PrettyTable()
table.field_names = ['№', 'x_', 'eps', 'x', 'delta', 'k']

x_ = Matrix(answers(1))

for i in range(5):
    num = i
    x_ = Matrix(answers(i))
    eps = 1e-6
    x, k = test(i)[1]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
            table.add_row([i, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0], k])
        else:
            table.add_row(['', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0], ''])
    table.add_row(['---','-' * 20,'---','-' * 20,'-' * 20,'-----'])

print(table)

print('Seidel Method test 5')
table = PrettyTable()
table.field_names = ['n','e','x_','eps','x','delta','k']

for n in range(3,7):
    x_ = Matrix(answer5(n,1e-3))
    x,k = test5(n,1e-3)[1]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    eps = 1e-6

    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
                table.add_row([n, 1e-3, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0], k])
        else:
            table.add_row(['','', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0], ''])
    table.add_row(['---', '---','-' * 20, '---', '-' * 20, '-' * 20, '-----'])
print(table)

print('LUP(0 - 4)')
table = PrettyTable()
table.field_names = ['№', 'x_', 'eps', 'x', 'delta']

x_ = Matrix(answers(2))

for i in range(5):
    num = i
    x_ = Matrix(answers(i))
    eps = 1e-6
    x = test(i)[2]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
            table.add_row([i, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0]])
        else:
            table.add_row(['', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0]])
    table.add_row(['---','-' * 20,'---','-' * 20,'-' * 20,])

print(table)

print('LUP test 5')
table = PrettyTable()
table.field_names = ['n','e','x_','eps','x','delta']

for n in range(3,7):
    x_ = Matrix(answer5(n,1e-3))
    x = test5(n,1e-3)[2]
    delta = Matrix([[abs(x_.matrix[i][0] - x.matrix[i][0])] for i in range(x_.dim['str'])])
    eps = 1e-6

    for j in range(x_.dim['str']):
        if j == int(x_.dim['str'] / 2):
                table.add_row([n, 1e-3, x_.matrix[j][0], eps, x.matrix[j][0], delta.matrix[j][0]])
        else:
            table.add_row(['','', x_.matrix[j][0], '', x.matrix[j][0], delta.matrix[j][0]])
    table.add_row(['---', '---','-' * 20, '---', '-' * 20, '-' * 20])
print(table)