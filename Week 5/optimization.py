# utility maximization using user defined optimization function
import numpy as np

# defining utiltiy function
def utility_func(x, y):
          return x*y

# defining budget_constraint 
def budget_constraint(income, p_x, p_y, x):
          return (income - (p_x * x)) / p_y 


# defining objective function for maximization
f = lambda x: -x * budget_constraint(10, 10, 10, x)

