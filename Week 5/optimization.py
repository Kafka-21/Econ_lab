# utility maximization using user defined optimization function
import numpy as np
from sympy import Symbol

# defining utiltiy function U(x, y) = x * y
def utility_func(x, y):
          return x*y

# defining budget_constraint income = p_x * x + p_y * y
def budget_constraint(income, p_x, p_y, x):
          return (income - (p_x * x)) / p_y 

# defining objective function for maximization
f = lambda x: -x * budget_constraint(100, 10, 10, x)

from scipy.optimize import minimize_scalar
res = minimize_scalar(f, method = 'brent')
print(res.x)

def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

g = lambda x: x * budget_constraint(100, 10, 10, x)
print(g(1), g(2), g(3), g(4), g(5), g(6), g(7), g(8), g(9), g(10))

from sympy import *

# g = symbols('g', cls = Function)

x = Symbol('x')

# function = x**4 + 7*x**3 + 8

g_prime = Derivative(x * budget_constraint(100, 10, 10, x), x)
print(g_prime.doit())

approx_phi = bisection(g_prime, 4, 6, 30)
print(approx_phi)

# approx_phi = bisection(g_prime, 4, 6, 30)
# print(approx_phi)

f_prime = lambda x : 10 - 2 * x

approx_phi = bisection(f_prime, 4, 6, 30)
print(approx_phi)


