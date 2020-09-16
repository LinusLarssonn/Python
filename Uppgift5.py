import math

def derivative(f, x, h):
    return(1/2*h) * (f(x+h) - f(x-h))

def solve(f, x0, h):
    x0 = f/derivative(f, 0, h)

def mathFunc(x):
    return 2*x**2



print(derivative(mathFunc, 0.5, 1))