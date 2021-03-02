import numpy as np
from sklearn import linear_model

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])


model = linear_model.LinearRegression().fit(x,y)

r_sq = model.score(x, y)
print('coefficient of determination: %.2f' %r_sq)
print('intercept: %.2f' %model.intercept_)
print('slope: %.2f' %model.coef_)


