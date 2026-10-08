import sympy as sp

x = sp.symbols('x')

equation = input("Enter f(x): ")

f = sp.lambdify(x, sp.sympify(equation), 'math')

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tol = float(input("Enter tolerance: "))

if f(a) * f(b) >= 0:
    print("Bisection method cannot be applied.")
else:
    while True:
        c = (a + b) / 2
        error = (b - a) / 2

        if error <= tol:
            break

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Root = {:.5f}".format(c))
    print("Error = {:.8f}".format(error))