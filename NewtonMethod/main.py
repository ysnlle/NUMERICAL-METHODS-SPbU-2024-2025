import scalar
import system

print("Newton's method\n")

print("Scalar Equation")
a, b = 10e-4, 10
a, b = scalar.posl_per(a, b)
print(f'    Localisation: [{a},{b}]')
print(f'    Answer: {scalar.newton(a, b)}')
print(f'    AbsError: {scalar.f(scalar.newton(a, b))}','\n')

print("System of Equations")
ans = system.newton()
approx = system.posl_per()
print(f'    Approximation: ({approx.matrix[0][0]}, {approx.matrix[1][0]})')
print(f'    Answer: ({ans.matrix[0][0]}, {ans.matrix[1][0]})')
print(f'    AbsError: ({system.f(ans.matrix[0][0], ans.matrix[1][0]).matrix[0][0]}, {system.f(ans.matrix[0][0], ans.matrix[1][0]).matrix[1][0]})')