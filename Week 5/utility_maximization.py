# utility maximization using scipy 
import numpy as np

# defining utiltiy function
def utility_func(x, y):
          return x * y

# defining budget_constraint 
def budget_constraint(income, p_x, p_y, x):
          return (income - (p_x * x)) / p_y 

from scipy.optimize import minimize_scalar

# defining objective function for maximization (-ive as scipy has minimization)
f = lambda x: -x * budget_constraint(10, 10, 10, x)

res = minimize_scalar(f, method = 'brent')
print(res.x)